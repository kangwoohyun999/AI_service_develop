from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
# import os

load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")

prompt = ChatPromptTemplate.from_template(
    "주제 {topic}에 대해 짧은 설명을 해주세요."
)

model = ChatOpenAI(model="gpt-5-nano")

output_parser = StrOutputParser()

chain = (
    {"topic" : RunnablePassthrough()}
    | prompt
    | model
    | output_parser
)

chain.invoke("더블딥")