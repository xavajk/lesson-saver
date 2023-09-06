# PDF Chatter

# Introduction

This project is centered around a PDF chatbot that can answer questions related to user-uploaded PDF documents. The app uses only Python for the GUI (Streamlit) and LangChain for the LLM interactions and embeddings.

# Information Flow

![PDF LangChain](demo/PDF-LangChain.jpg)

_Note: This repository uses the above process outlined in https://github.com/alejandro-ao/ask-multiple-pdfs_

First the uploaded documents are parsed using PyPDF. The returned text is split into chunks using LangChains `RecursiveCharacterTextSplitter` with an overlap so that in the case that a chunk ends in the middle of a sentence or idea, minimal context is lost.

OpenAI’s embeddings are accessed via LangChain and provided to the vector store. In the diagram above, Pinecone is shown, however this repository uses Faiss (\***\*Facebook AI Similarity Search\*\***). The Faiss vector store is then initialized with the OpenAI embeddings and the text chunks.

When the user inputs a question or prompt, it is similarly embedded and semantically similar vectors are retrieved from the vector store. The results are sent to the LLM (`ChatOpenAI` from LangChain’s chat models) and the answer is returned to the user.

# Usage

The GUI that the user is presented with is intuitive and simple. The collapsible sidebar contains the file uploader where users can upload their PDFs. Once they have been uploaded, they must click ‘Process’ in order for the PDFs to be loaded into the vector store. That’s all that’s needed before the user can simply input questions in the chat box and query information that is given to the LLM as context.

Below is a video demoing example usage:

https://github.com/xavajk/lesson-saver/assets/95323308/c90ec204-1d2d-4d5c-8489-a280c13f7557
