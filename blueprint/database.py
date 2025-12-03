import montydb 

def get_conn(database):
    client = montydb.MontyClient()
    return client.get_database(database)

