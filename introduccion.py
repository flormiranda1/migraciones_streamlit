import streamlit as st
import streamlit_analytics

with streamlit_analytics.track():
    st.text_input("ver dashoard")
    st.button("Click me")

# Guardar resultados en un archivo JSON
streamlit_analytics.track(save_to_json="vistas.json")

st.title("Flujos Migratorios América")
st.markdown("***")
st.markdown("### Primer subtitulo")

st.sidebar.markdown("Navegación dashboard")

