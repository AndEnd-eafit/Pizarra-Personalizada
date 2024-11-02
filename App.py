import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title='Mi pizarra personalizada', layout='wide', initial_sidebar_state="collapsed")

# Estilos de tipografía
st.markdown("""
    <style>
    .titulo {
        font-family: 'Lexend', sans-serif;
        font-size: 36px;
        text-align: center;
    }
    .subtitulo {
        font-family: 'Inter', sans-serif;
        font-size: 24px;
        text-align: center;
    }
    .contenido {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        text-align: justify;
    }
    .color-box {
        display: inline-block;
        width: 30px;
        height: 30px;
        margin-right: 5px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título de la aplicación
st.title("Pizarra personalizada")

# Parámetros en barra lateral
with st.sidebar:
    st.subheader('Escoger el tamaño del pincel')
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)

    st.subheader('Escoge el color del pincel')

    # Colores predefinidos en un diccionario
    colors = {
        'Rojo': '#FF0000',
        'Naranja': '#FFA500',
        'Amarillo': '#FFFF00',
        'Verde': '#008000',
        'Turquesa': '#40E0D0',
        'Azul': '#0000FF',
        'Magenta': '#FF00FF',
        'Púrpura': '#800080',
        'Blanco': '#FFFFFF'
    }

    # Botón de selección de color predeterminado
    selected_color = st.radio("Selecciona un color predeterminado:", list(colors.keys()))

    # Botón de selección para color personalizado
    if st.checkbox("Usar color personalizado"):
        stroke_color = st.color_picker("Selecciona el color del pincel", '#000000')
    else:
        # Color del pincel seleccionado
        stroke_color = colors[selected_color]

# Parámetros del canvas
bg_color = '#d6f0f2'
drawing_mode = "freedraw"

# Componente de canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Color de relleno fijo con algo de opacidad
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=500,
    width=600,
    key="canvas",
)
