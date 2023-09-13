import streamlit as st
import streamlit-analytics

if 'last_time' not in st.session_state:
    st.session_state.last_time = None

with streamlit-analytics.track():
    st.text_input("ver dashoard")
    st.button("Click me")

# Guardar resultados en un archivo JSON
streamlit-analytics.track(save_to_json="vistas.json")

st.title("Flujos Migratorios América")
st.markdown("***")
st.markdown("### Primer subtitulo")

st.sidebar.markdown("Navegación dashboard")

