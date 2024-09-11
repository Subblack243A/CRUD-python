#Librería mysql-conecctor-python
import mysql.connector
from mysql.connector import Error
#Conexion con el servidor
try:
    con = mysql.connector.connect(
        host = "localhost",
        user = "Subblack",
        password = "1234",
        port = 3306
    )
except Error as e:
    print("Ha ocurrido un error: "+e)
#Cursor es el que permite usar el lenguaje SQL
c = con.cursor()
#Crea una base de datos dentro del servidor
c.execute("CREATE DATABASE IF NOT EXISTS felipe")
#Usa la base de datos que se creo
c.execute("USE felipe")
#Comando para crear una tabla en la  base de datos
tableCreate = "CREATE TABLE IF NOT EXISTS students(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, semester INT NOT NULL);"
#Comando para hacer un insert en la tabla students
insertTable = "INSERT INTO students (name, semester) VALUES ('Santiago Naranjo', 3);" 
#Ejecuta el comando de crear tabla
c.execute(tableCreate)
#Ejecuta el comando de insertar en la tabla
c.execute(insertTable)
#Muestra contenido de la tabla
print("-----------------ANTES---------------")
selectTable = "SELECT * FROM students;"
c = con.cursor()
c.execute(selectTable)
res = c.fetchall()
for i in res:
    print(i)
#Elimina los registros que tengan por id 2
delete = "DELETE FROM students WHERE id = 2;"
#Ejecuta la eliminación
c.execute(delete)
#Muestra contenido de la tabla
print("-----------------DESPUES---------------")

selectTable = "SELECT * FROM students;"
c = con.cursor()
c.execute(selectTable)
res = c.fetchall()
for i in res:
    print(i)
#Cierra el cursor
c.close()
#Gurada los cambios y cierra la conexion con el servidor
con.commit()
con.close()