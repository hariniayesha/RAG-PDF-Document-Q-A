import streamlit as st
import os
import tempfile

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader

from langchain_community.vectorstores import FAISS

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_core.prompts import ChatPromptTemplate


# Load environment variables
load_dotenv()

# Load API keys
groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")


# Check API keys
if not groq_api_key or not google_api_key:
    st.error("Please check your API keys in the .env file.")
    st.stop()


# Streamlit application title
st.title("Gemma Model Document Q&A")

st.write("Upload your PDF documents and ask questions.")


# Initialize Groq LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model="openai/gpt-oss-20b",
    temperature=0
)


# Initialize Google Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=google_api_key
)


# Initialize session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None


# Upload PDF documents
uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type=["pdf"],
    accept_multiple_files=True
)


# Process PDF documents
if st.button("Process Documents"):

    if not uploaded_files:
        st.warning("Please upload at least one PDF.")

    else:

        documents = []

        with st.spinner("Loading PDF documents..."):

            for uploaded_file in uploaded_files:

                temp_path = None

                try:
                    with tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=".pdf"
                    ) as temp_file:

                        temp_file.write(uploaded_file.getvalue())
                        temp_path = temp_file.name

                    loader = PyPDFLoader(temp_path)

                    documents.extend(loader.load())

                finally:
                    if temp_path and os.path.exists(temp_path):
                        os.remove(temp_path)


        if not documents:
            st.error("No readable content found in the PDFs.")

        else:

            # Split documents into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = text_splitter.split_documents(documents)

            # Create FAISS vector database
            with st.spinner("Creating vector database..."):

                vector_store = FAISS.from_documents(
                    chunks,
                    embeddings
                )

                st.session_state.vector_store = vector_store

            st.success("Documents processed successfully!")


# Ask questions
st.subheader("Ask a Question")

question = st.text_input(
    "Enter your question about the uploaded documents:"
)


if st.button("Get Answer"):

    if st.session_state.vector_store is None:

        st.warning("Please process your documents first.")

    elif not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):

            # Retrieve relevant documents
            relevant_docs = st.session_state.vector_store.similarity_search(
                question,
                k=4
            )

            # Prepare context
            context = "\n\n".join(
                doc.page_content for doc in relevant_docs
            )

            # Create prompt template
            prompt = ChatPromptTemplate.from_template(
                """
                Answer the question based only on the
                provided context.

                If the answer is not available in the
                context, say that you don't know.

                Context:
                {context}

                Question:
                {question}

                Answer:
                """
            )

            # Generate response
            messages = prompt.format_messages(
                context=context,
                question=question
            )

            response = llm.invoke(messages)

            st.subheader("Answer")

            st.write(response.content)

            # Display source documents
            with st.expander("View source documents"):

                for i, doc in enumerate(relevant_docs):

                    st.write(f"Source {i + 1}")

                    st.write(doc.page_content)

                    st.write("---")