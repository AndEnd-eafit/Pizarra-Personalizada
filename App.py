
import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title='Reconocimiento de Dígitos escritos a mano', layout='wide')

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
# Add canvas component
# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = '#000000' # Set background color to white
bg_color = '#d6f0f2'

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=500,
    width=600,
    key="canvas",
)
