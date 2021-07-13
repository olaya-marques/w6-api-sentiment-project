![Portada]( https://user-images.githubusercontent.com/64830147/125401114-0fe13280-e3b3-11eb-8ee5-8783dbcf36ba.png)
*Este repositorio contiene el cuarto proyecto del Bootcamp: Data Analytics de Iron Hack. El objetivo de este proyecto es la creación de una API, la cual puede recibir datos de los usuarios a través de las llamadas post y entregar datos a través de las llamadas get. Los datos se almacenan en un MongoDB. La API se ha creado mediante Flask. Adicionalmente, se ha realizado, además, el NLP de los discursos almacenados en la base de datos y los wordclouds de los países resultantes de dicho análisis.* 

*Para la realización de este ejercicio he utilizado una base de datos de kaggle: [UN General Debates](https://www.kaggle.com/unitednations/un-general-debates) que contiene más de 70.000 líneas de discursos de los países pertenecientes a las naciones unidas desde 1970 a 2015.*

# Descripción 🥸
![Descripción](https://user-images.githubusercontent.com/64830147/125401226-2c7d6a80-e3b3-11eb-99d1-8a6728867512.png)

Cada año desde 1947, representantes de los estados miembros de la ONU se reúnen en las sesiones anuales de la Asamblea General de las Naciones Unidas. La pieza central de cada sesión es el Debate General. Este es un foro en el que líderes y otros altos funcionarios emiten declaraciones que presentan la perspectiva de su gobierno sobre los principales problemas de la política mundial. Estas declaraciones son similares a los discursos legislativos anuales sobre el estado de la unión en la política nacional. Esta API contiene el conjunto de datos, el Corpus de Debate General de la ONU (UNGDC), incluyendo el corpus de textos de las declaraciones de Debate General de 1970 (Sesión 25) a 2016 (Sesión 71).

Extra: ¿Quieres conocer que país tiene los discursos más positivos y negativos? ¿coincidirán con los países considerados “más felices” según el índice global de felicidad, informe elaborado por la propia ONU?

# Índice de contenido 📎
-	4 jupyter notebooks diferenciados en la base de datos, test de la API, análisis NLP y wordclouds.
-	Carpeta de Tools y Configuración con todas las funciones en relación con las llamadas de get y post y la configuración con la conexión a Mongo
-	Carpeta de imágenes.
-	API.md (portada de la API y explicación de su funcionamiento)

# Librerías utilizadas 📚
Durante este proyecto se emplearon las siguientes librerías:
-	Pandas
-	Numpy
-	Requests
-	Os
-	Json
-	BeautifulSoup
-	Os
-	Matplotlib
-	Seaborn
-	Wordcloud
-	NLTK
-	Regex
-	Pymongo

*La documentación oficial se encuentra en el apartado de Link&Recursos*

# Metodología 🔎
1.	Diseño y estructuración de una base de datos empleando MongoDB. Contiene 3 columnas diferenciadas en año, país (en código ISO) y el discurso (en inglés) correspondiente. 
2.	Creación de la API para recibir y almacenar datos.
3.	Leer y servir datos mediante endpoints:

**Llamadas GET**
>- `/UN`: Devuelve todos los datos contenidos en la base de datos
>- `/year`: Devuelve una lista con todos los años
>- `/country`: Devuelve una lista con todos los países 
>- `/speech`: Devuelve una lista con todos los discursos

*Dinámicas parametrizadas*
>- `/speech_country/<country>`: Devuelve todos los datos para un país concreto
>- `/speech_year/<year>`: Devuelve todos los datos para un año en econcreto
>- `/speech_yearcountry/<year>/<country>` : Devuelve todos los datos para un año y país concreto

**Llamadas POST**
>- `/speech_new` : Añade un nuevo diccionario a la colección. Deberá de seguir la misma estructura y contener la siguiente información: year, country y speech.

4.	Extraer el valor emocional de los discursos y compararlos con los países más “felices e infelices” (empleando web scrapping para la obtención de los datos en referencia al índice global de la felicidad).
5.	Visualización de los resultados obtenidos en el apartado anterior mediante WordClouds.


# Links & Resources  🖇️
- [Pandas documentation](https://pandas.pydata.org)
- [Requests documentation](https://requests.readthedocs.io/en/master/)
- [Json documentation](https://docs.python.org/3/library/json.html)
- [Pymongo documentation](https://pymongo.readthedocs.io/en/stable/)
- [Regex documentation](https://docs.python.org/3/library/re.html)
- [Numpy documentation](https://docs.python.org/3/library/re.html)
- [NLTK]( https://www.nltk.org)
- [Seaborn documentation](https://www.nltk.org)
- [Matplotlib documentation](https://matplotlib.org/stable/contents.html)
- [Os documentation](https://docs.python.org/3/library/os.html)
- [Word cloud documentation]( https://amueller.github.io/word_cloud/)
- [Beautiful documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
