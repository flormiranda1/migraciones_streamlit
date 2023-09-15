import streamlit as st

try:
    import streamlit_analytics
except ImportError:
    # Install streamlit-analytics on first run (not included in requirements.txt).
    import subprocess
    import sys

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "streamlit_analytics"]
    )
    import streamlit_analytics

with streamlit_analytics.track():
    st.title(
        "Flujo migratorio introduccion"
    )
    name = st.text_input("Write your name")
    clicked = st.button("Click me")
    if clicked:
        st.write(
            f"Hello {name}"
        )

    st.write("")
    st.write(
        "...and now add `?analytics=on` to the URL to see the analytics dashboard 👀"
    )
    
