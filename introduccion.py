import streamlit as st
import streamlit.components.v1 as components

ga_tracking_code = "G-KXFEBBX96W"

# Inserta el código de seguimiento de Google Analytics en la aplicación de Streamlit
components.html(
    f"""<script async src="https://www.googletagmanager.com/gtag/js?id={ga_tracking_code}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {{
        dataLayer.push(arguments);
      }}
      gtag('js', new Date());
    
      gtag('config', '{ga_tracking_code}');
    </script>""",
    height=0,
)


st.title("Flujos Migratorios América")
st.markdown("***")
st.markdown("### Primer subtitulo")

st.sidebar.markdown("Navegación dashboard")

