import sqlite3

CONNECTION = sqlite3.connect('data.db')
CURSOR = CONNECTION.cursor()

def create_table(table_name,schema):

    try:
        create_query = 'CREATE TABLE {table} {content}'.format(table=table_name, content=schema)
        CURSOR.execute(create_query)
        status = 200
    except:
        print('Fallo la creacion de la tabla {table}'.format(table=table_name))
        status = 400
    return status

create_status = create_table('workshop','(id int, firstanme text, lastname text)')

print ('CREATE STATUS', create_status)

def insert_item(table_name, item):
    try:
        inser_query = 'INSERT INTO {table} VALUES {value}'.format(table=table_name, value = item)
        CURSOR.execute(inser_query)
        status = 200
    except:
        print('Fallo insertar elemento a la table')
        status = 400
    return status

insert_status = insert_item('workshop','(2, "Roger", "Rogozo")')
print('INSERT STATUS:', insert_status)

def get_all_items(table_name):
    items = []
    try:
        for row in CURSOR.execute('SELECT * FROM {table}'.format(table = table_name)):
            items.append(row)
        status = 200
    except sqlite3.Error as error:
        print('Fallo la busqueda de elementos', error)
        status = 400
        items = []

    return status, items

status, items = get_all_items('workshop')
print(status)
print('RECORDS: ', items )