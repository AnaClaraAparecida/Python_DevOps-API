import montydb

client = montydb.MontyClient()

db = client.get_database('pessoa')
db.users.insert_one({'username': 'ana.clara@4linux.com.br', 'nome': 'Ana Clara Oliveira','senha': '1234ana'}) 

for registro in db.users.find():
    print(registro)