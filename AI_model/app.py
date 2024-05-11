import streamlit as st
from dotenv import load_dotenv

def main():
    st.set_page_config(page_title="InsightLK AI Model", page_icon="🧊", layout="centered", initial_sidebar_state="auto")
    st.header("InsightLK AI Model")

    st.text_input("Ask me anything", "Type here...")
    st.button("Submit", key="submit_main")

    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)

        col1, col2 = st.columns(2)
        with col1:
            st.button("Process", key="process_documents")
        with col2:
            st.button("Clear", key="clear_documents")

if __name__ == '__main__':
    main()
