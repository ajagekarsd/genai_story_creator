import os
from dotenv import load_dotenv
from langchain_classic.chains.summarize.refine_prompts import prompt_template
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY environment variable not set")

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=1,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)

messages = [
    (
        "system",
        "Write a short story about a cat, write max 5 lines",
    ),
    ("human", "I love black cat."),
]

template_string = "Write a short story about a {topic}, write max 5 lines"
prompt_template = PromptTemplate.from_template(template_string)
final_prompt = prompt_template.format(topic="chickens")

ai_msg = llm.invoke(final_prompt)
ai_msg
print(ai_msg.content)