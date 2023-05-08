from bson.objectid import ObjectId
from typing import Dict, List
from datetime import timedelta

class MinhaCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "minhaCollection"
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents


    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            filter, # Filtro
            { "endereco": 0, "_id": 0 } # Opcoes de retorno
        )

        response = []
        for elem in data: response.append(elem)

        return response

    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, { "_id": 0 })
        return response

    def select_if_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "cpf": { "$exists": True } })
        for elem in data: print(elem)

    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            { "name": "Lhama" }, # Filtro
            { "endereco": 0, "_id": 0 } # Opcoes de retorno
        ).sort([("pedidos.pizza", 1)])

        for elem in data: print(elem)

    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "$or": [{ "name": "Lhama" }, { "ola": { "$exists": True } }] })
        for elem in data:
            print(elem)
            print()

    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({ "_id": ObjectId("642c9643dac681ba1fc5a8e7") })
        for elem in data: print(elem)

    def edit_registry(self, name) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_one(
            { "_id": ObjectId("645585c1ddbce431b3c82d9e") }, #Filtro
            { "$set": { "name": name } } # Campo de edição
        )
        print(data.modified_count)

    def edit_many_registries(self, filtro, propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            filtro, #Filtro
            { "$set": propriedades }
        )
        print(data.modified_count)

    def edit_many_increment(self, num) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.update_many(
            { "_id": ObjectId("645585c1ddbce431b3c82d9e") }, #Filtro
            { "$inc": { "idade": num } }
        )
        print(data.modified_count)

    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many({ "profissao": "Programador" })
        print(data.deleted_count)
    
    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one({ "_id": ObjectId("645585c1ddbce431b3c82d9e") })
        print(data.deleted_count)

    def create_index_ttl(self):
        collection = self.__db_connection.get_collection(self.__collection_name)
        tempo_de_vida = timedelta(seconds=10)
        collection.create_index("data_de_criacao", expireAfterSeconds=tempo_de_vida.seconds)
