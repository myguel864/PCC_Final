# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st
import pandas as pd
from IPython.display import display_html

df_cine = pd.read_excel('PCC_BASE DE DATOS_FINAL.xlsx')

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Catálogo']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Escena Cero</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """
    \n\nBienvenid@ a Escena Cero, una nueva forma de ver películas.\n\nEscena Cero es un buscador y catálogo de películas diferente. Aquí no buscaras una película por género, director o año, si no por las palabras más repetidas en sus respectivos guiones. Al insertar una palabra la página te mostrará aquella película en la que se repite más con información relevante sobre esta en la que se incluye la relacionada con el mundo del guión cinematográfico.\n\nSi esa idea no te convence siempre puedes ir a nuestro Catálogo de películas y seleccionar la que más te llame la atención. Desde ahí también podrás visualizar toda la información anterior.\n\nEste proyecto nació de mi particular forma de ver películas. Usualmente estamos acostumbrados a ver trailers, leer sinopsis y reseñas sobre una película antes de verla. Este bombardeo de información siempre me pareció que le quitaba la emoción al ver una nueva película. Es por ello que suelo ver películas sin tener mucha información sobre ellas, a excepción de a qué género pertenecen o quienes las realizaron
    \n\nAnimate a ver películas de una manera diferente o a descubrir curiosidades sobre tus largometrajes favoritos. 
    \n\nPrueba a usar alguna de las siguientes palabras: girl, love, walks, office, something, floor, building, elevator, gun, police, ring, suddenly, fellowship, hobbits, sword, music, old, jazz, playing, smiles, mother, door, cat, father, ghost, president, general, alien, attacker, ship, detective, see, man, apartment, street, cabin, camp, lake, behind, runs, white, horse, black, nigger, slave, mr, mrs, miss, lady, sister. 
    """

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>Buscador de película</h3>", unsafe_allow_html=True)


    # Entrada de búsqueda
    busqueda = st.text_input("Escribe una palabra en inglés:")

    # Si hay una palabra de búsqueda
    if busqueda:
        encontrado = False
        for i in range(len(df_cine)):
            # Recopilamos la información de la película
            nombre = df_cine.loc[i, "TITULO"]
            guionista = df_cine.loc[i, "GUIONISTA"]
            palabras = df_cine.loc[i, "PALABRAS REPETIDAS"]
            imagen = df_cine.loc[i, "IMAGEN"]
            personajes = df_cine.loc[i, "PERSONAJE REPETIDO"]
            minutos = df_cine.loc[i, "DURACION"]
            año = df_cine.loc[i, "AÑO DE ESTRENO"]
            etiquetas = df_cine.loc[i, "ETIQUETAS"]
            certificacion = df_cine.loc[i, "CERTIFICACION"]
            clasificacion = df_cine.loc[i, "CLASIFICACION"]
            director = df_cine.loc[i, "DIRECTOR"]
            interior = df_cine.loc[i, "INT"]
            exterior = df_cine.loc[i, "EXT"]
            dia = df_cine.loc[i, "DAY"]
            noche = df_cine.loc[i, "NIGHT"]
            
            # Si la palabra de búsqueda está en las palabras repetidas
            if busqueda.lower() in palabras.lower():
                encontrado = True
                st.subheader(f"Resultados encontrados para '{busqueda}':")
                st.image(imagen, width=800)
                st.subheader(f'{nombre}')
                st.write(f"**Clasificación IMDb:** {clasificacion}")
                st.write(f"**Director(a):** {director} - **Año de estreno:** {año} - **Duración:** {minutos} minutos")
                st.write(f"**Etiquetas:** {etiquetas} - **Certificación:** {certificacion}")
                st.write(f"**Guionista(s):** {guionista}")
                st.write(f"**Palabras más utilizadas:** {palabras}")
                st.write(f"**Personajes más mencionados:** {personajes}")
                st.write(f"**Escenas en interiores:** {interior} - **Escenas en exteriores:** {exterior}")
                st.write(f"**Escenas de día:** {dia} - **Escenas de noche:** {noche}")
                break
        
        # Si no se encontró nada
        if not encontrado:
            st.write("Lo sentimos, no encontramos una película con esa palabra.")

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Catálogo</h1>", unsafe_allow_html=True)

    if 'selected_movie' not in st.session_state:
        st.session_state.selected_movie = None

    # Mostrar las portadas como botones
    col1, col2, col3 = st.columns(3)

    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>Elige una película:</div>", unsafe_allow_html=True)

    for i, row in df_cine.iterrows():
        # Usamos una columna para cada imagen de portada
        with col2:
            if st.button(f"Ver detalles de {row['TITULO']}", key=row['TITULO']):
                st.session_state.selected_movie = i
                break

      

    # Mostrar los detalles de la película seleccionada
    if st.session_state.selected_movie is not None:
        movie = df_cine.iloc[st.session_state.selected_movie]
        
        st.image(movie['IMAGEN'], width=800)
        st.subheader(movie['TITULO'])
        st.write(f"**Clasificación IMDb:** {movie['CLASIFICACION']}")
        st.write(f"**Director(a):** {movie['DIRECTOR']}")
        st.write(f"**Guionista(s):** {movie['GUIONISTA']}")
        st.write(f"**Año de estreno:** {movie['AÑO DE ESTRENO']}")
        st.write(f"**Duración:** {movie['DURACION']} minutos")
        st.write(f"**Certificación:** {movie['CERTIFICACION']}")
        st.write(f"**Etiquetas:** {movie['ETIQUETAS']}")
        st.write(f"**Palabras más utilizadas:** {movie['PALABRAS REPETIDAS']}")
        st.write(f"**Personajes más mencionados:** {movie['PERSONAJE REPETIDO']}")
        st.write(f"**Escenas en interiores:** {movie['INT']} - **Escenas en exteriores:** {movie['EXT']}")
        st.write(f"**Escenas de día:** {movie['DAY']} - **Escenas de noche:** {movie['NIGHT']}")
        
        # Opción para volver al listado de películas
        if st.button("Volver al listado"):
            st.session_state.selected_movie = None
            st.rerun()
    