import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Lazy LLM initialization to avoid side-effects on import
_llm = None

def _get_api_key():
    return os.getenv("GROQ_API_KEY")

def _init_llm():
    global _llm
    if _llm is not None:
        return _llm
    api_key = _get_api_key()
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set. Set it before calling create_story().")

    # initialize the LLM (same params as before). If ChatGroq required the API key explicitly, adjust here.
    _llm = ChatGroq(
        model="qwen/qwen3-32b",
        temperature=1,
        max_tokens=None,
        reasoning_format="parsed",
        timeout=None,
        max_retries=2,
        # other params...
    )
    return _llm


template_string = "Write a short story about a {topic}, write max 5 lines"

def create_story(topic: str) -> str:
    if not topic:
        raise ValueError("Topic must be a non-empty string")

    try:
        llm = _init_llm()
    except Exception:
        # propagate a clear error so the UI can display it
        raise

    # Import PromptTemplate lazily to avoid import errors

    prompt_template = PromptTemplate.from_template(template_string)
    final_prompt = prompt_template.format(topic=topic)

    try:
        ai_msg = llm.invoke(final_prompt)
        # ai_msg may be an object; try to extract .content safely
        content = getattr(ai_msg, "content", None)
        if content is None:
            # fallback to string representation
            return str(ai_msg)
        return content
    except Exception:
        # Re-raise to let the caller (UI) handle/display errors
        raise
