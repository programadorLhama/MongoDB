from models.connection_options.connection import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()


minha_collection_repository = MinhaCollectionRepository(db_connection)


order = {
    "name": "Lhama",
    "endereco": "Rua do Limao",
    "pedidos": {
        "pizza": 1,
        "hamburguer": 5,
        "pizza doce": 4
    },
    "cpf": 'abc45'
}

minha_collection_repository.insert_document(order)

list_of_documents = [
    {"eric": "cartman"},
    {"stan": "march"},
    {"kenny": "mcCormick"},
    {"kyle": "Broflovski"}
]
minha_collection_repository.insert_list_of_documents(list_of_documents)