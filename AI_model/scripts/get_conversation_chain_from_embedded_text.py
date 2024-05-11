from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
from langchain.chat_models import ChatOpenAI


def get_conversation_chain(vectorstore):
    # llm = ChatOpenAI()
    llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

