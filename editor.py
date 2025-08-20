rom langchain_google_genai import ChatGoogleGenerativeAI

from langchain.agents import Tool
from dotenv import load_dotenv 
load_dotenv()
llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
) 

def grammar_fix(text:str)->str:
    prompt=f"Fix all grammar and punctuation issues in the text below: \n\n{text}" 
    return llm.predict(prompt) 

def adjust_tone(text:str,tone:str="formal")->str:
    prompt = f"Rewrite the following text in a more {tone} tone, keeping the meaning intact:\n\n{text}"
    return llm.predict(prompt) 

def structure_check(text:str)->str:
    prompt = f"""Analyze and improve the structure and flow of the article below.
Keep the Title, Introduction, Body, and Conclusion format intact, but improve transitions and clarity.

{text}
"""
    return llm.predict(prompt)


editor_tools=[
    Tool(
        name="GrammarFixTool",
        func=grammar_fix,
        description="Fix gramar,punctuation,and sentence clarity"

    ),
    Tool(
        name="ToneAdjustTool",
        func=lambda x: adjust_tone(x,tone="formal"),
        description="adjust the tone of the article to be more formal"
    ),
    Tool(
        name="StructureCheckTool",
        func=structure_check,
        description="check and improve the structure and flow of the article"
    )
]
