from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from pypdf import PdfReader

def process_text(text):
    """
    Process the given text by splitting it into chunks and creating a knowledge base using FAISS.

    Parameters:
    text (str): The text to be processed.

    Returns:
    FAISS: A knowledge base object containing the processed text chunks.
    """
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1024,
        chunk_overlap = 256,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    knowledgeBase = FAISS.from_texts(chunks, embeddings)
    
    return knowledgeBase

def summarizer(pdf):
    """
    Summarizes the content of a PDF file using a question-answering chain.

    Parameters:
    pdf (streamlit.uploaded_file_manager.UploadedFile): The uploaded PDF file.

    Returns:
    tuple: A tuple containing:
     - the summarized text, 
     - the query cost.
    """
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        knowledgeBase = process_text(text)
        query = 'Summarize the content of the uploaded file in 5-7 sentencies with key facts.'
        if query:
            docs = knowledgeBase.similarity_search(query)
            model = "gpt-3.5-turbo-16k"
            llm = ChatOpenAI(model = model, temperature = 0)
            chain = load_qa_chain(llm, chain_type = 'stuff')
            
            with get_openai_callback() as cost:
                response = chain.run(input_documents = docs, question = query)
                return response, cost