from backend.funcs import add_footer
import streamlit as st

# Título Principal
st.markdown("<h1 style='text-align: center;'>Simuladores de Distribuciones Muestrales (Prep. TC4)</h1>", unsafe_allow_html=True)

add_footer()

st.markdown("""
<p style='text-align: center; font-size: 18px;'>
¡Bienvenido! En esta página encontrarás simuladores y guias para ayudarte a entender conceptos claves de distribuciones muestrales. Al final de la página, encontrarás un "sandbox" donde podrás poner a practica los conceptos utilizando comandos de R!
""", unsafe_allow_html=True)

st.divider()

# --- SECCIÓN: TUTORIAL DE USO ---
st.header("🛠️ ¿Cómo usar los Simuladores?")

# Paso 1: Configuración
st.markdown("### 1. Configura tu dado trucado")

col1, col_img, col_text, col4 = st.columns([1.0, 1.0, 2.5, 0.5])

with col_img:
    # Asegúrate de que la ruta de la imagen sea la correcta
    try:
        st.image("frontend/media/config.png", caption="Panel de Probabilidades en la Barra Lateral", use_container_width=True)
    except:
        st.info("🖼️ *(Aquí va la imagen de tu menú de configuración)*")

with col_text:
    st.write("""
    En la barra lateral izquierda encontrarás los deslizadores de **Configuración del Dado**.
    
    * **¿Cómo funcionan?**: Estas barras te permiten ajustar directamente las **probabilidades** de cada cara del dado. La suma de todas las barras siempre se mantendrá exactamente en 1, así que al mover una, las demás se ajustarán progresivamente para compensar.
    * **Ejemplo**: Si la probabilidad base es cercana a `0.16` (1/6), el dado será justo. Si aumentas mucho la del número 5 a `0.80`, verás que sacar un 5 se vuelve altamente seguro.
    * **¡Experimenta!**: Prueba configuraciones extremas para ver cómo afectan los resultados teóricos y simulados.
    """)

# Paso 2: Parámetros
st.markdown("### 2. Define el tamaño de la muestra ($n$)")
st.write("""
Debajo de los pesos, verás opciones para configurar el tamaño de muestra y la cantidad de simulaciones. 
El tamaño de la muestra ($n$) es vital:
* **$n$ pequeño (1-5)**: Las distribuciones muestrales se parecerán mucho a la forma de tu dado trucado original.
* **$n$ grande (30+)**: Entra en acción la magia asintótica y verás surgir curvas normales.
""")

# Paso 3: Interpretación
st.markdown("### 3. Interpreta los resultados")
tab1, tab2 = st.tabs(["📊 Distribuciones y Gráficos", "📈 Estandarización (Z)"])

with tab1:
    st.write("""
    En los simuladores verás contrastada la **Población** (lo teórico) contra la **Muestra** (tu experimento). 
    Presta atención a las métricas superiores donde el simulador calcula el Error Estándar y los verdaderos parámetros.
    """)
    
with tab2:
    st.write("""
    Verás cómo los datos se centran en 0 utilizando el **Puntaje Z**. 
    Si las barras del histograma se ajustan a la línea roja ($N(0,1)$), significa que la aproximación normal es exitosa.
    """)


# --- SECCIÓN: EJERCICIOS ---
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>💻 Práctica con R</h3>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Al final del recorrido teórico, ve a la sección de <b>Ejercicios</b> para poner a prueba tus conocimientos analizando bases de datos reales escribiendo código R directamente desde tu navegador.</p>", unsafe_allow_html=True)

st.markdown("<br><h3 style='text-align: center; color: #1A5276;'>👈 ¡Abre el menú lateral y elige un simulador para empezar!</h3>", unsafe_allow_html=True)