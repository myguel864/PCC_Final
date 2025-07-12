# importo las librerias necesarias
import streamlit as st
import pandas as pd
from IPython.display import display_html

# transformo mi base de datos en un dataframe
df_cine = pd.read_excel('PCC_BASE DE DATOS_FINAL.xlsx')

# configuro una fuente especifica para la página
st.markdown("""
    <style>
                            
        html, h1, h2, h3 {
            font-family: 'Courier New', Courier !important; 
        }
            
        p, div, span {
            font-family: 'Courier New', Courier;
        }
            
    </style>
""", unsafe_allow_html=True)

# creo 2 páginas en Streamlit
# creo una página principal donde se encontrará el buscador y otra donde se encontrará el catálogo de películas.

# creo una lista de páginas
paginas = ['Inicio', 'Catálogo']

# creo botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# creo condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # creo un título y lo centro
    st.markdown("<h1 style='text-align: center; '>Escena Cero</h1>", unsafe_allow_html=True)

    # creo una cadena de texto que luego mostraré 
    texto = """
    \n\nBienvenid@ a Escena Cero, una nueva forma de ver películas.\n\nEscena Cero es un buscador y catálogo de películas diferente. Aquí no buscaras una película por género, director o año, si no por las palabras más repetidas en sus respectivos guiones. Al insertar una palabra la página te mostrará aquella película en la que se repite más con información relevante sobre esta en la que se incluye la relacionada con el mundo del guión cinematográfico.\n\nSi esa idea no te convence siempre puedes ir a nuestro Catálogo de películas y seleccionar la que más te llame la atención. Desde ahí también podrás visualizar toda la información anterior.\n\nEste proyecto nació de mi particular forma de ver películas. Usualmente estamos acostumbrados a ver trailers, leer sinopsis y reseñas sobre una película antes de verla. Este bombardeo de información siempre me pareció que le quitaba la emoción al ver una nueva película. Es por ello que suelo ver películas sin tener mucha información sobre ellas, a excepción de a qué género pertenecen o quienes las realizaron
    \n\nAnimate a ver películas de una manera diferente o a descubrir curiosidades sobre tus largometrajes favoritos. 
    """

    # muestro el texto
    st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # creo un subtítulo
    st.markdown("<h3 style='text-align: center;'>Buscador de película</h3>", unsafe_allow_html=True)

    # creo un buscador
    busqueda = st.text_input("Escriba una palabra en inglés:")

    # si se inserta una palabra la página recopila información sobre las películas en el data frame
    if busqueda:
        # creo una variable para 
        encontrado = False 
        for i in range(len(df_cine)):
            # recopilo la información de las películas
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
            
            # si la palabra de búsqueda está en las palabras repetidas muestro toda la información sobre la película
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
        
        # si la palabra no es encuentra en la columna PALABRAS REPETIDAS muestro un texto
        if not encontrado:
            st.write("Lo sentimos, no encontramos una película con esa palabra.\n\nPrueba a usar alguna de las siguientes palabras: girl, love, walks, office, something, floor, building, elevator, gun, police, ring, suddenly, fellowship, hobbits, sword, music, old, jazz, playing, smiles, mother, door, cat, father, ghost, president, general, alien, attacker, ship, detective, see, man, apartment, street, cabin, camp, lake, behind, runs, white, horse, black, nigger, slave, mr, mrs, miss, lady, sister.")

# si la página seleccionada no es Inicio, es decir el Catálogo, paso al siguiente código
else:

    # creo un título para la página
    st.markdown("<h1 style='text-align: center;'>Catálogo</h1>", unsafe_allow_html=True)

    # creo un condicional que crea una variable para controlar la película que seleccionen los usuarios
    if 'selected_movie' not in st.session_state:
        st.session_state.selected_movie = None

    # creo un texto explicativo
    st.markdown(f"<div style='text-align: center; font-size: 15px;'>Elige una película:</div>", unsafe_allow_html=True)

    # creo tres columnas iguales en la página donde se encontraran los botones para seleccionar películas
    cols = st.columns(3)

    # recorro cada fila del dataframe
    for idx, row in df_cine.iterrows():

        # reparto los botones en las columnas
        col = cols[idx % 3]

        # creo los botones
        with col:
            if st.button(f"{row['TITULO']}", key=row['TITULO']):

                # guardo el índice de la película seleccionada
                st.session_state.selected_movie = idx

                # recargo la página pero con la película seleccionada
                st.rerun()

    # muestro los datos de la película seleccionada si se selecciona una
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
        
        # creo un botón para volver al catálogo
        if st.button("Volver al listado"):
            st.session_state.selected_movie = None
            st.rerun()
    