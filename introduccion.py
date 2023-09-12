import streamlit as st

st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-**********"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-KXFEBBX96W');
        </script>
    """, unsafe_allow_html=True)


st.title("Flujos Migratorios América")
st.markdown("***")
st.markdown("### Primer subtitulo")

st.sidebar.markdown("Navegación dashboard")

