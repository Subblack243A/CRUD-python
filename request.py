import requests, json
from pymongo.mongo_client import MongoClient
from config import configuration

cliente = MongoClient(configuration['chainconnection'])
datadb = cliente[configuration['database']]
collection = datadb[configuration['collection']]

#Metodo para crear un documento
def create (data):
    r = collection.insert_one(data)
    print (f"Documento insertado con Id: {r.inserted_id}")

#Método para leer los documentos
def readAll():
    docs = collection.find()
    for doc in docs:
        print(json.dumps(doc, indent=4))

#Método para leer un documento
def readOne(campo, valor):
    doc = collection.find_one({campo:valor})
    if doc:
        print(doc)
    else:
        print("No se encontró documento")

#Método para actualizar un documento
def update (condicion, data):
    r = collection.update_one(condicion, {"$set": data})
    print(f"Documento(s) modificado(s): {r.modified_count}")

#Método para eliminar documento
def delete (campo, valor):
    r = collection.delete_one({campo:valor})
    print(f"Documento(s) eliminado(s): {r.deleted_count}")

def deleteAll ():
    res = collection.delete_many({})
    print("Se han eliminado todos los documentos")

def main ():
    response = requests.get("https://api.jikan.moe/v4/top/anime")
    anime = response.json()["data"]
    #for a in anime:
     #   create(a)
    
    readOne('title', 'Bleach: Sennen Kessen-hen')
    delete('title', 'Sousou no Frieren')
    readOne('title', 'Sousou no Frieren')

if __name__ == "__main__":
    main()