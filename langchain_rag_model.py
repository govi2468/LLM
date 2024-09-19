import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
# from langchain.vectorstores import faiss
from read_documents import process_pdfs_in_directory
from pdf_file_directory import directory
from add_delay import get_embeddings_with_delay
from openai import OpenAI
#  Reading the API key from env
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# extracting all raw text from all pdf files
raw_text = process_pdfs_in_directory(directory=directory)
join_text = ''.join(raw_text)
# print(type(join_text))
# split the text using Character text split such that token size will not increase
text_splitter = CharacterTextSplitter(
    separator='\n',
    chunk_size = 800,
    chunk_overlap= 200,
    length_function=len,
)
text = text_splitter.split_text(join_text)
# for texts in text:
#     print(texts, '\n')

# Downloading embeddings from OpenAI
embeddings = OpenAIEmbeddings(model = 'text-embedding-3-small')
# embeddings = get_embeddings_with_delay(text, delay=2.0)
# print(embeddings)
# # faiss = VectorStore
vectorstore = FAISS.from_texts(text, embeddings)
# # document_search = FAISS.from_texts(text, embeddings)
#
from langchain.chains.question_answering import load_qa_chain
from langchain.llms.openai import openai

chain = load_qa_chain(openai(), chain_type= "stuff")

# Extract model into pickle format to use for creation of RAG app
# import pickle
# pickle.dump(chain,open('langchain_model.pkl','wb'))
query = "What is the power consumption of latestXYZ corp smartphone?"
docs = vectorstore.similarity_search(query)
chain.run(input_documents = docs, question = query)

# if __name__ == '__main__':
#     chain.run(input_documents = docs, question = query)