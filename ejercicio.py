import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")

#Obteniendo los 10 productos mas rentables

query = ''' 
    SELECT ProductName, SUM(Price * Quantity) as Revenue 
    FROM OrderDetails od 
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10    
'''
#Con la suma de la multiplicacion del precio por las cantidades vendidas obtenemos el total recaudado por cada producto

top_products = pd.read_sql_query(query, conn) #Esta funcion de pandas nos permite leer consultas sql automaticamente, en los parentesis ponemos (consulta,conexion)

top_products.plot(x="ProductName",y="Revenue", kind="bar",figsize=(10,5),legend=False) #Con este metodo hacemos un garfico de los resultados obtenidos

plt.title("10 productos mas rentables") #Le ponemos nombre al titulo

plt.xlabel("Products") #Le ponemos nombre al eje x

plt.ylabel("Revenue") #Le ponemos nombre al eje y

plt.xticks(rotation=90) #Rotamos los nombres de las variables del eje x para que sean mas visibles

plt.show() #Mostramos el grafico

#Obteniendo los 10 empleados mas efectivos

query2 = ''' 
    SELECT FirstName || " " || LastName as Empleado, COUNT(*) as Ventas
    FROM Employees e
    JOIN Orders o ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Ventas DESC
    LIMIT 10   
''' 

top_employees = pd.read_sql_query(query2, conn)

top_employees.plot(x="Empleado", y="Ventas", kind = "bar", figsize= (10,5), legend=False)

plt.title("10 empleados mas rentables") #Le ponemos nombre al titulo

plt.xlabel("Empleados") #Le ponemos nombre al eje x

plt.ylabel("Ventas") #Le ponemos nombre al eje y

plt.xticks(rotation=90) #Rotamos los nombres de las variables del eje x para que sean mas visibles

plt.show()

#Empleados que mas recaudaron

query3 = ''' '''