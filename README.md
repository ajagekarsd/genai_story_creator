# GenAI Story Creator

Simple GenAi Lang Chain - Streamlit app that takes a short topic (max 5 letters) and generates a short story.
Its main purpose is to demonstrate how to integrate a GenAI LLM (Groq) using Lang Chain.

Requirements
- Python 3.8+
- Set the environment variable `GROQ_API_KEY` before running if you want the LLM integration to work.

Quick start
1. (Optional) Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install the essentials:

```bash
pip install -r requirements.txt
```

3. Add your API key to .env fie at root folder:

```properties
GROQ_API_KEY="your_api_key_here"
```

4. Run the Streamlit app:

```bash
streamlit run streamlit_main.py
```

Notes
- The code uses lazy imports for the LLM-related packages so the UI can load without those dependencies installed; however, to actually generate a story you must install the LLM client packages (see `requirements.txt`) and set `GROQ_API_KEY`.
- If you don't have the LLM packages or the API key, the UI will show an error when trying to generate a story, but the app will start normally.
- login to groq and create an API key here: https://console.groq.com/keys
- refer - lang chain example here: https://docs.langchain.com/oss/python/integrations/chat/groq

