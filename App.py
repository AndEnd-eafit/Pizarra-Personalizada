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
    </style>
    """, unsafe_allow_html=True)

# Título de la aplicación
st.title("Pizarra personalizada")

# Parámetros en barra lateral
with st.sidebar:
    st.subheader('Escoger el tamaño del pincel')
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)

    st.subheader('Escoge el color del pincel')
    stroke_color = st.color_picker("Selecciona el color del pincel", '#000000')
    
    st.subheader('Colores predeterminados')
    stroke_color = st.radio('Selecciona un color:', 
                            ['#FF0000', '#FFA500', '#FFFF00', '#008000', '#40E0D0', 
                             '#0000FF', '#FF00FF', '#800080', '#FFFFFF'], 
                            index=0,
                            format_func=lambda x: {
                                '#FF0000': 'Rojo',
                                '#FFA500': 'Naranja',
                                '#FFFF00': 'Amarillo',
                                '#008000': 'Verde',
                                '#40E0D0': 'Turquesa',
                                '#0000FF': 'Azul',
                                '#FF00FF': 'Magenta',
                                '#800080': 'Púrpura',
                                '#FFFFFF': 'Blanco'
                            }[x])

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
