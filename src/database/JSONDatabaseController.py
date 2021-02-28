import os
from DatabaseControllerInterface import DatabaseControllerInterface

DATA_FILE_TYPE = '.json'
PATH_TO_DATABSE = './data'

def get_jsons(path):
    return [file[:-len(DATA_FILE_TYPE)] for file in os.listdir(path) if file.endswith(DATA_FILE_TYPE)]

class JSONDatabaseController():
    def create_collection(self, col_name):
        with open('{}/{}{}'.format(PATH_TO_DATABSE, col_name, DATA_FILE_TYPE), 'a+') as f:
            f.seek(0)
            if f.read() == '':
                f.write('{}')
                print('Created new collection')
            else:
                print('ERROR: collection already exists')

    def delete_collection(self, col_name):
        if col_name in get_jsons(PATH_TO_DATABSE):
            os.remove(PATH_TO_DATABSE + '/' + col_name + DATA_FILE_TYPE)
            print('Removed collection')
        else:
            print('ERROR: collection does not exist')

db = JSONDatabaseController()

db.create_collection('hello')
db.create_collection('hello')
db.delete_collection('hello')
db.delete_collection('hello')