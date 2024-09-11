#Importación de librerías
from pymongo.mongo_client import MongoClient
#Para buscar por Id un documento
#from bson.objectid import ObjectId

#Cadena de conección
uri = "mongodb+srv://Subblack243A:N4ru70243A#@subblack.iqz1vmz.mongodb.net/?retryWrites=true&w=majority&appName=Subblack"

#Conección con el servidor
try:
    client = MongoClient(uri)
    dataBase = client["sample_mflix"]
    collection = dataBase["users"]
except Exception as e:
    print("Hubo un error: "+e)
    
#Método para crear un usuario
def createUser (dato):
    r = collection.insert_one(dato)
    print (f"Documento insertado con Id: {r.inserted_id}")

#Método para leer los usuarios
def readUsers():
    docs = collection.find()
    for doc in docs:
        print(doc)

#Método para actualizar un usuario
def updateUser (condicion, data):
    r = collection.update_one(condicion, {"$set": data})
    print(f"Documento(s) modificado(s): {r.modified_count}")

#Método para eliminar usuario(s)
def deleteUser (condicion):
    r = collection.delete_one(condicion)
    print(f"Documento(s) eliminado(s): {r.deleted_count}") 

#Método main donde ejecutamos todo
def main():
    #Llamada a los métodos
    dato = {"name": "Santiago Matallana", "email": "trampasloks@gmail.com", "password": "tr4mp4slok45"}
    createUser(dato)
    print("--------------------------USERS----------------------")
    readUsers()
    print("--------------------------USERS----------------------")
    updateUser({"name": "Daniel Hincapie"}, {"password": "amoAgeofEmpires"})
    print("--------------------------USERS----------------------")
    readUsers()
    print("--------------------------USERS----------------------")
    deleteUser({"nombre": "Santiago Matallana"})
    print("--------------------------USERS----------------------")
    readUsers()
    print("--------------------------USERS----------------------")
    print("Listo")
    client.close()

if __name__ == "__main__":
    main()