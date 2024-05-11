from langchain.text_splitter import CharacterTextSplitter

def get_text_chunks(raw_text):
    text_spiltter = CharacterTextSplitter(
        separator="/n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_spiltter.split_text(raw_text)
    return text_chunks