import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de la página
st.set_page_config(page_title='Mi pizarra personalizada', layout='wide', initial_sidebar_state="collapsed")

# Estilos de fuente personalizados
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
    st.subheader('Escoge el tamaño del pincel')
    stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
    
    st.subheader('Escoge el color del pincel')
    stroke_color = st.color_picker("Selecciona el color del pincel", '#000000')
    
# Fondo de la pizarra
bg_color = '#d6f0f2'

# Crear el componente de lienzo
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Color de relleno fijo con opacidad
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=500,
    width=600,
    drawing_mode="freedraw",
    key="canvas",
)

# Mostrar resultado del lienzo (opcional)
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data, caption="Tu dibujo")
