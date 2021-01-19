## Análisis-de-datos---Examen-1Bimestre
### 1. Twitter a CouchDB 
- El script extrae datos de Twitter referentes a 'mario kart' y los envía a couchDB.
- Es necesario tener las credenciales de la API de Twitter y hacer uso de la librería 'tweepy'.
- Se conecta con la base de datos CouchDB.
- Se crea una clase y una función que extrae los datos de la API para guardarlos en la base.
### 2. Web Scraping a mongoDB
- El script extrae datos de una página web 'Mercado Libre sección vehículos' y los guarda en mongoDB.
- Es necesario importar las librerías BeautifulSoup, pandas, json y pymongo.
- Se crean dos funciones para guardar las cadenas de la página web.
- Se crean 3 arreglos vacíos.
- Se obtiene el contenido de la página con los campos: Nombre, Localización y Precio.
- Con una sentencia *for* se guardan los datos en los arreglos.
- Los datos almacenados se convierten a formato JSON. 
- Se hace la conexión a mongoDB. 
- Con una sentencia *for* se guardan los datos en la base.
### 3. Facebook a mongoDB
- El script extrae datos de facebook 'vehiculos de 100000 páginas' y los envía a mongoDB.
- Es necesario usar las librerías facebook_scraper, pymongo y time.
- Se realiza una conexión con la base
- Se usa una sentencia *for* para extraer los datos de facebook, se implementa un time para evitar problemas con la cuenta.
- Los datos se guardan en una variable objeto y se envía cada uno de los documentos a la base.
### 4. SQLite a mongoDB
- El script extrae los datos de una base presente en SQLite y los envía a mongoDB.
- Es necesario usar las librerías sqlite3, pandas y json.
- Se realiza la conexión con la base relacional y los datos se guardan en un DataFrame.
- El DataFrame almacenado es convertido a JSON.
- Se realiza la conexión con mongoDB.
- Con una sentencia *for* se guardan los datos en la base.
### 5. CouchDB a mongoDB
- El script envía los datos almacenados en CouchDB a mongoDB.
- Las librerías más importantes que se usan son: pymongo, bson, couchdb.
- Se realiza la conexión con couchDB.
- Se realiza la conexión con mongoDB.
- Con una sentencia *for* se guardan los datos con su respectivo ID.
### 6. mongoDB a CouchDB
- El script envía los datos almacenados en mongoDB a CouchDB  
- Las librerías más importantes que se usan son: pymongo, bson, couchdb y json.
- Se realiza la conexión con couchDB.
- Se realiza la conexión con mongoDB.
- Con una sentencia *for* se guardan los datos con su respectivo ID.
- Antes de guardar los datos es necesario que la data extraída se convierta en un archivo de tipo JSON.
### 7. CouchDB a mongoDB Atlas
- El script envía los datos almacenados en CouchDB a mongoDB Atlas.
- Las librerías más importantes que se usan son: pymongo, bson, couchdb.
- Se realiza la conexión con couchDB.
- Se realiza la conexión con mongoDB Atlas 'Es necesario obtener e link que permite hacer una conexión desde Python'.
- Con una sentencia *for* se guardan los datos con su respectivo ID.
### 8. mongoDB a mongoDB Atlas
- El script envía los datos almacenados en mongoDB a mongoDB Atlas.
- Las librerías más importantes que se usan son: pymongo, bson, couchdb.
- Se realiza la conexión con mongoDB.
- Se realiza la conexión con mongoDB Atlas 'Es necesario obtener e link que permite hacer una conexión desde Python'.
- Con una sentencia *for* se guardan los datos con su respectivo ID.
### 9. Datos de mongoDB Atlas en archivo examen.csv
- Los datos extraídos de todos los scripts anteriores se muestran en un archivo de tipo .csv.
- Para obtener el archivo se realizó una conexión remota con mongoDB Compass.
