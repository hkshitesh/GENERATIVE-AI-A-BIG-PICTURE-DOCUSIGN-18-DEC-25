from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from docx import Document

load_dotenv()

agreement_agent = Agent(
    name="DocuSign Agreement Assistant",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "You are an AI assistant for an electronic agreement platform.",
        "Answer only from the provided agreement text.",
        "If information is missing, say: Not mentioned in the agreement.",
        "Do not provide legal advice.",
        "Use simple and clear language."
    ],
    markdown=False
)



def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text.strip())

    return "\n".join(text)

contract_text = extract_text_from_docx("msa.docx")

agreement_text = contract_text

agreement_agent.print_response(
    f"""
Agreement Text:
{agreement_text}

User Question:
How long is the contract valid?
""",
    stream=True
)

# questions = [
#     "What is the notice period for termination?",
#     "What happens if one party breaches the agreement?",
#     "Which law governs this agreement?",
#     "Is there any auto-renewal mentioned?",
#     "Should I sign this agreement?"
# ]

# for q in questions:
#     agreement_agent.print_response(
#         f"Agreement Text:\n{agreement_text}\n\nQuestion:\n{q}",
#         stream=True
#     )
