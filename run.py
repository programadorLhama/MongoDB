from models.connection_options.connection import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepository
from datetime import datetime, timedelta

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

# minha_collection_repository.delete_registry()

# minha_collection_repository.create_index_ttl()

documento = { "nome": "Arnaldo", "idade": 30, "data_de_criacao": datetime.utcnow() -timedelta(hours=3) }
minha_collection_repository.insert_document(documento)
