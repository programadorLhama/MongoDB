from models.connection_options.connection import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()


minha_collection_repository = MinhaCollectionRepository(db_connection)


#filtro = { "profissao": "Programador" }
#propriedades = {
#    "endereco": {
#        "cep": "a18548",
#        "rua": "das ruas",
#        "bairro": "lalala"
#    }
#}

#minha_collection_repository.edit_many_registries(filtro, propriedades)

#minha_collection_repository.edit_many_increment(-10)

minha_collection_repository.delete_registry()
