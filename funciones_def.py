import sqlite3
import pandas as pd

#cuando trabajamos con python, iniciamos una transaccion (el BEGIN se hace automatico)

def square(n):
    return n*n

print(square(10))

conn = sqlite3.connect("Northwind.db") #CREAMOS UNA VARIABLE QUE LLAME A LA BASE DE DATOS
conn.create_function("square",1,square) #CREAMOS UNA FUNCION EN SQLITE (nombre que le queremos poner a la funcion, cantidad de parametros, nombre de la funcion en python

cursor = conn.cursor() #LOS CURSORES LOS PERMITEN PODER HACER CONSULTAS DESDE PYTHON, SE ENCARGAN DE LEER LA BASE DE DATOS Y ENVIAR UNA RESPUESTA   
cursor.execute(''' 
    SELECT * FROM Products   
    ''') #CON .execute() HACEMSO UNA CONSULTA

results = cursor.fetchall() #CON .fetchall() OBTENEMOS LOS RESULTADOS DE LA CONSULTA QUE HICIMOS    
                            #LOS RESULTADOS SE MUETSRAN COMO UNA LISTA DE TUPLAS CON TODOS LOS REGISTROS
                            
results_df = pd.DataFrame(results) #CON PANDAS HACEMOS QUE NOS DEVUELVA UNA TABLA

conn.commit() #guardamos la informacion en la base de datos

cursor.close()
conn.close() #cerramos la conexion


print(results_df)

#otra manera de hacerlo con with

with sqlite3.connect("Northwind.db") as conn:
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute(''' 
    SELECT *, square(Price) FROM Products   
    ''') #para usar las funcion definidas las ponemos en la consulta
    results = cursor.fetchall()
    results_df = pd.DataFrame(results) #de esta manera no tenemos que cerrar las conexiones manualmente