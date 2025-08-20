mport streamlit as st
from multiple_agent.research import run_research
from multiple_agent.writer import write_article
from multiple_agent.editor import edit_article
from fpdf import FPDF
import os

st.set_page_config(page_title="Research Article Generator", layout="centered")
st.title("📚 Automated Research Article Pipeline")


topic = st.text_input("🔍 Enter your research topic:")

if st.button("Start Research") and topic:
    with st.spinner("🔎 Researching..."):
        research_output = run_research(topic)

    with st.spinner("✍️ Writing the article..."):
        draft = write_article(research_output)

    with st.spinner("🛠 Editing the article..."):
        final_article = edit_article(draft)

    st.success("✅ Article Ready!")

    st.subheader("📄 Final Polished Article:")
    st.markdown(final_article)

    
    def save_to_pdf(text, filename="final_article.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        for line in text.split('\n'):
            pdf.multi_cell(0, 10, line)
        pdf.output(filename)
        return filename

    if st.button("💾 Save as PDF"):
        pdf_file = save_to_pdf(final_article)
        with open(pdf_file, "rb") as f:
            st.download_button("📥 Download PDF", f, file_name="final_article.pdf")

    
    st.subheader("💬 Ask something about the article:")
    query = st.text_input("Your question:")
    if query:
        st.info("🔧 This will soon connect to a local LLM or use embeddings to answer.")
else:
    st.info("Enter a topic above and click **Start Research**.")
