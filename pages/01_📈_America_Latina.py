<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-KXFEBBX96W"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-KXFEBBX96W');
</script>

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if st.checkbox("mostrar texto"):
    st.write("hola")
    

consolidado_latino = pd.read_csv('consolidado_latinoF.csv',sep=',', thousands=',')
canada = pd.read_csv('canadaF.csv',sep=',', thousands=',')
eeuu = pd.read_csv('eeuuF.csv',sep=',', thousands=',')
america_latina = pd.read_csv('america_latinaF.csv', sep=',', thousands=',')
consolidado_regiones = pd.read_csv("consolidado_regionesF.csv", sep=',', thousands=',')

if st.checkbox("mostrar df"):
    st.dataframe(eeuu)
    
if st.checkbox("vista de datos head o tail"):
    if st.button("mostrar_head"):
        st.write(america_latina.head())
    if st.button("mostrar_tail"):
        st.write(america_latina.tail())
        
dim = st.radio("dimension a mostrar:",("filas","columnas"),horizontal=True)

if dim == "filas":
    st.write("cantidad de filas:",america_latina.shape[0])
else:
    st.write("cantidad de columnas:",america_latina.shape[1])

fig = plt.figure(figsize=(10, 6))
sns.boxplot(data=consolidado_regiones["PIB"])
plt.title("Box Plot de PIB")
plt.xticks(rotation=45)
plt.show()
        
st.pyplot(fig)


# Años seleccionados
years_selected = [1990, 1995, 2000, 2005, 2010, 2015, 2020]

# Filtrar el DataFrame para incluir solo los años seleccionados
df_years = consolidado_regiones[consolidado_regiones['Año'].isin(years_selected)]

# Lista de nombres de indicadores en tu DataFrame consolidado_regiones
indicadores = ["PIB", "Pobreza", "Tasa de empleo", "Mortalidad"]

# Obtener la region que se quiere analizar
regiones_list = consolidado_regiones["Pais"].unique().tolist()
regiones_seleccionadas = st.multiselect("Selecciona una o varias regiones a analizar:", regiones_list)

# Obtener el valor del año mínimo desde el slider
año_minimo = st.slider("Selecciona el año mínimo", min(years_selected), max(years_selected), min(years_selected))

# Ciclo for para generar gráficos para cada indicador
for indicador in indicadores:
    # Filtrar el DataFrame según las regiones y el año mínimo seleccionados
    df_filtered = df_years[df_years['Año'] >= año_minimo]
    if regiones_seleccionadas:
        df_filtered = df_filtered[df_filtered['Pais'].isin(regiones_seleccionadas)]

    # Agrupar por año y país y obtener la suma del indicador
    grouped_data = df_filtered.groupby(["Año", "Pais"])[indicador].sum().unstack()

    # Crear gráfico de barras apiladas
    fig, ax = plt.subplots()
    grouped_data.plot(kind="bar", stacked=True, ax=ax)

    # Agregar título y etiquetas
    plt.title(f"{indicador} por región a lo largo de los años (desde {año_minimo})")
    plt.xlabel("Año")
    plt.ylabel(indicador)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)








