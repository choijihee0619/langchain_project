from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from stock_info import Stock

load_dotenv()

ollama_url = "http://127.0.0.1:11434"  
lmstudio_url = "http://127.0.0.1:1234/v1"

# llm = OllamaLLM(model="gemma3:1b", base_url=ollama_url)
# llm = ChatOpenAI(model="gemma-3-1b-it", base_url=lmstudio_url, api_key="dummy")
llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0.2)

def investment_report(company, symbol):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
            Want assistance provided by qualified individuals enabled with experience on understanding 
            charts using technical analysis tools while interpreting macroeconomic environment 
            prevailing across world consequently assisting customers acquire long term advantages 
            requires clear verdicts therefore seeking same through informed predictions written down 
            precisely! First statement contains following content- “Can you tell us what future stock 
            market looks like based upon current conditions ?"
        """),
        ("user", """
            {company} 주식에 투자해도 될까요? 
            아래의 기본정보, 재무제표를 참고해 마크다운 형식의 투자 보고서를 한글로 작성해 주세요.

            기본정보:
            {basic_info}
        
            재무제표:
            {financial_statement}
        """)
    ])

    output_parser = StrOutputParser()

    # 프롬프트 + 모델 + 출력 파서
    chain = prompt | llm | output_parser

    stock = Stock(symbol)

    response = chain.invoke({
        "company": company,
        "basic_info": stock.get_basic_info(),
        "financial_statement": stock.get_financial_statement()
    })

    return response
