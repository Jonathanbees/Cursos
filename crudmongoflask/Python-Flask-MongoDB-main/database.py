from pymongo import MongoClient
import certifi
MONGO_URI="mongodb://localhost:27017/"

#MONGO_URI = 'mongodb+srv://jonathanbees:1234@cluster0.bvovu2x.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        #client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["reto3"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
