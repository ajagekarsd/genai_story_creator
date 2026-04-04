import streamlit as st

# Default profile info (edit these defaults or pass overrides to render_about_me)
DEFAULTS = {
    "user_name": "Sunil Ajagekar",
    "profile_pic": "",  # URL to profile image; leave empty to use a placeholder
    "linkedin_url": "www.linkedin.com/in/ajagekar-s198925",
    "github_url": "https://github.com/ajagekarsd",
    "bio": "With over 14 years of experience in software product development, specializing in Java and related technologies, my experience with cloud technologies and emerging fields such as Artificial Intelligence (AI) and Machine Learning (ML) positions me well to drive innovation and help build a robust, future-ready organization.",
}


def render_about_me(**overrides):
    """Render an About Me page in Streamlit.

    Usage:
        render_about_me()  # uses defaults
        render_about_me(user_name="Sunil", linkedin_url="https://...")
    """
    data = DEFAULTS.copy()
    data.update(overrides)

    st.header("About Me")

    # Profile image (use placeholder if none provided)
    if data["profile_pic"]:
        st.image(data["profile_pic"], width=150)
    else:
        st.image("https://via.placeholder.com/150", width=150)

    st.markdown(f"### {data['user_name']}")
    st.write(data["bio"])

    st.markdown("**Contact & Links**")
    st.markdown(f"- LinkedIn: [{data['linkedin_url']}]({data['linkedin_url']})")
    st.markdown(f"- GitHub: [{data['github_url']}]({data['github_url']})")
    st.markdown(f"- Email: {data['email']}")

    st.caption("Edit the `DEFAULTS` in `about_me.py` or pass keyword args to `render_about_me()` to update your profile information.")
