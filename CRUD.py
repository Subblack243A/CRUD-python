#Librería mysql-conecctor-python
import mysql.connector
from mysql.connector import Error

#Conexion con el servidor
def connection ():
    try:
        con = mysql.connector.connect(
            host = "localhost",
            user = "Subblack",
            password = "1234",
            port = 3306
        )
    except Error as e:
        print("Ha ocurrido un error: "+e)
    return con

#Método para crear la una base de datos y una tabla
def createDbTable(con):
    c = con.cursor()
    #Crea una base de datos dentro del servidor
    c.execute("CREATE DATABASE IF NOT EXISTS felipe")
    #Usa la base de datos que se creo
    c.execute("USE felipe")
    #Comando para crear una tabla en la  base de datos
    tableCreate = "CREATE TABLE IF NOT EXISTS students(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, semester INT NOT NULL);"

#Metodo para leer la tabla students
def readStudents(con):
    c = con.cursor()
    #Query para leer la tabla
    que = "SELECT * FROM students"
    c.execute(que)
    est = c.fetchall()
    for i in est:
        print(i)

#Método para crear un estudiante
def createStudent(con, name, semester):
    c = con.cursor()
    #Comando para hacer un insert en la tabla students
    que = "INSERT INTO students (name, semester) VALUES (%s, %s);" 
    c.execute(que, (name, semester))
    con.commit()

#Método para borrar un estudiante
def deleteStudent(con, id):
    c = con.cursor()
    que = "DELETE FROM students WHERE id = %s;"
    c.execute(que, (id,))
    con.commit()
    
#Método para actualizar un estudiante
def updateStudent(con, id, name, semester):
    c = con.cursor()
    que = "UPDATE students SET name = %s, semester = %s WHERE id = %s"
    c.execute(que, (name, semester, id))
    con.commit()


con = connection()
#Ejecución del método de creacion de la base de datos y la tabla
createDbTable(con)

#Ejecución del método crear estudiante
createStudent(con, "Felipe Valcarcel", 7)

#Ejecución del método de lectura
print("----------Tabla Actual----------")
readStudents(con)
print("--------------------------------")

#Ejecución método actualizar
updateStudent(con, 1, "Laura Latorre", 3)

#Ejecución del método de lectura
print("----------Tabla Actualizada----------")
readStudents(con)
print("--------------------------------------")

#Ejecución método eliminar
deleteStudent(con, 1)

#Ejecución del método de lectura
print("----------Tabla Final----------")
readStudents(con)
print("-------------------------------")

print("Hecho")