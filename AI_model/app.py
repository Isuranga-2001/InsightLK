import streamlit as st
from dotenv import load_dotenv
from scripts.get_text_from_pdfs import get_pdf_text
from scripts.get_text_chunks_from_rawtext import get_text_chunks
from scripts.get_vectorstore_from_text_chunks import get_vectorstore_OPENAI, get_vectorstore_INSTRUCTOR_L, get_vectorstore_INSTRUCTOR_XL


def main():
    load_dotenv()
    st.set_page_config(page_title="InsightLK AI Model", page_icon="🧊", layout="centered", initial_sidebar_state="auto")
    st.header("InsightLK AI Model")

    st.text_input("Ask me anything", "Type here...")
    st.button("Submit", key="submit_main")

    with st.sidebar:
        st.subheader("Your Documents")
        PDF_docs = st.file_uploader("Upload your documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)
        if st.button("Process", key="process_documents"):
            if PDF_docs is not None:
                try:
                    with st.spinner("Processing..."):
                        raw_text = get_pdf_text(PDF_docs)
                        text_chunks = get_text_chunks(raw_text)
                        embedded_text = get_vectorstore_INSTRUCTOR_XL(text_chunks)
                        st.write(embedded_text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    print(f"An error occurred: {e}")
            else:
                st.warning("Please upload at least one document.")

if __name__ == '__main__':
    main()


