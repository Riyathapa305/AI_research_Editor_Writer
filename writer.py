from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv 
load_dotenv()
llm=ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
) 



def write_article(topic: str, research_notes: str) -> str:
    prompt = f"""
You are a professional content writer.

Your task is to write a high-quality article based on the research notes below on the topic: "{topic}".

Research Notes:
{research_notes}

Instructions:
- Title the article appropriately.
- Start with an engaging introduction.
- Write 2-3 body paragraphs expanding the ideas.
- Conclude with a strong closing paragraph.
- Keep the tone informative and fluent.
- Do NOT repeat the bullet points exactly; rewrite them into a narrative.
- Maintain a logical flow and paragraph structure.

Write the complete article below:
"""
    return llm.predict(prompt)
