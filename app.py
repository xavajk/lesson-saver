import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text = ''
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    

def main():
    # initialize app
    load_dotenv()
    st.set_page_config(page_title='Chat with your PDFs!', page_icon=':books:')
    
    # set up header and text prompt
    st.header('PDF Chat :books:')
    st.text_input("Ask a question about your documents:")
    
    # set up file sidebar
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            "Upload your files here!", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store w/ embeddings

if __name__ == '__main__':
    main()