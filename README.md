RAG-Based PDF Document Q&A System

Project Overview

The RAG-Based PDF Document Q&A System is an interactive application that allows users to upload PDF documents and ask questions based on their content.

It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate context-aware answers using a Large Language Model (LLM).

The application is built using Python, Streamlit, LangChain, FAISS, Google Gemini Embeddings and Groq.

Features

- Upload one or multiple PDF documents.
- Extract text from PDF files.
- Split documents into smaller text chunks.
- Generate vector embeddings using Google Gemini.
- Store document embeddings using FAISS vector database.
- Retrieve relevant information using semantic similarity search.
- Generate answers using Groq LLM.
- Display relevant source document content.
- Interactive and user-friendly Streamlit interface.

Technologies Used

Technology| Purpose
Python| Core programming language
Streamlit| User interface
LangChain| RAG application framework
FAISS| Vector database
Google Gemini Embeddings| Text embedding generation
Groq API| Large Language Model integration
PyPDF| PDF text extraction
Python-dotenv| Environment variable management

How It Works

The application follows these steps:

1. PDF Upload: Users upload PDF documents through the Streamlit interface.
2. Text Extraction: PyPDFLoader extracts text from the uploaded PDFs.
3. Text Chunking: RecursiveCharacterTextSplitter divides the extracted text into smaller chunks.
4. Embedding Generation: Google Gemini Embeddings converts text chunks into vector representations.
5. Vector Storage: FAISS stores the generated embeddings.
6. Similarity Search: When a user asks a question, the application retrieves the most relevant document chunks.
7. Answer Generation: Groq LLM generates an answer using the retrieved context.
8. Source Display: Relevant document content is displayed along with the generated answer.

Project Structure

RAG-PDF-Document-QA/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── sample-pdf-10mb.pdf
└── .env (not uploaded to GitHub)

Installation and Setup

1. Clone the Repository

git clone https://github.com/hariniayesha/RAG-PDF-Document-QA.git

2. Navigate to the Project Folder

cd RAG-PDF-Document-QA

3. Create a Virtual Environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

5. Configure API Keys

Create a ".env" file in the project folder and add your API keys:

GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key

Replace the placeholder values with your own API keys.

Important: Never upload your ".env" file or expose your API keys on GitHub.

6. Run the Application

streamlit run app.py

The application will open in your browser at:

http://localhost:8501

How to Use

1. Open the application.
2. Upload one or more PDF documents.
3. Click Process Documents.
4. Wait until document processing is completed.
5. Enter a question related to the uploaded documents.
6. Click Get Answer.
7. View the generated answer and relevant source documents.

Future Enhancements

- Support for additional document formats such as DOCX and TXT.
- Chat history and conversational memory.
- Improved document retrieval and ranking.
- Support for multiple LLM providers.
- Deployment to a cloud platform.
- Improved user interface and document management.

Learning Outcomes

Through this project, I gained practical experience in:

- Retrieval-Augmented Generation (RAG).
- Large Language Model integration.
- Vector databases and semantic search.
- Text embeddings and document chunking.
- PDF processing using Python.
- Building interactive applications using Streamlit.
- Integrating APIs and managing environment variables.

Author

Ayesha Saher

GitHub: https://github.com/hariniayesha
