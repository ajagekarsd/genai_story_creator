import streamlit as st
from story_creator import create_story

st.set_page_config(page_title="GenAI Story Creator", layout="centered")

st.title("GenAI Story Creator")
st.write("Enter a topic (max 5 letters) and click Submit to generate a short story.")

# Input with frontend validation (Streamlit doesn't provide max_length directly for text_input)
topic = st.text_input("Topic", value="", max_chars=5)

if len(topic) > 5:
    st.error("Topic must be at most 5 characters long.")

submitted = st.button("Submit")

if submitted:
    # Server-side validation
    if not topic:
        st.error("Please enter a topic (1-5 characters).")
    elif len(topic) > 5:
        st.error("Topic exceeds 5 characters. Shorten it and try again.")
    else:
        with st.spinner("Generating story..."):
            try:
                story = create_story(topic)
                st.markdown("**Generated story:**")
                st.write(story)
            except Exception as e:
                st.error(f"Failed to generate story: {e}")
