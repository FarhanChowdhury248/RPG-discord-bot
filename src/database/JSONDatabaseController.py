import os
from DatabaseControllerInterface import DatabaseControllerInterface
import json

DATA_FILE_TYPE = '.json'
PATH_TO_DATABSE = './data'

def get_jsons():
    return [file[:-len(DATA_FILE_TYPE)] for file in os.listdir(PATH_TO_DATABSE) if file.endswith(DATA_FILE_TYPE)]

def get_json_file_path(file_name):
    return '{}/{}{}'.format(PATH_TO_DATABSE, file_name, DATA_FILE_TYPE)

class JSONDatabaseController(DatabaseControllerInterface):
    def create_collection(self, col_name):
        if col_name in get_jsons():
            print('ERROR: collection already exists')
            return
        with open(get_json_file_path(col_name), 'w') as f:
            json.dump({}, f)
            print('Created collection')

    def delete_collection(self, col_name):
        if col_name in get_jsons():
            os.remove(get_json_file_path(col_name))
            print('Removed collection')
        else:
            print('ERROR: collection does not exist')

    def get_collection(self, col_name):
        if col_name in get_jsons():
            with open(get_json_file_path(col_name)) as f:
                data = json.load(f)
            return data
        print('ERROR: collection does not exist')

    def clear_collection(self, col_name):
        if col_name in get_jsons():
            with open(get_json_file_path(), 'w') as f:
                json.dump({}, f)
                print('Cleared collection')
        else:
            print('ERROR: collection does not exist')

    def add_document(self, doc_name, doc_data = {}):
        pass
    def update_document(self, doc_name, doc_data = {}):
        pass
    def delete_document(self, doc_name):
        pass
    def get_document(self, doc_name):
        pass
    def clear_document(self, doc_name):
        pass

if __name__ == '__main__':
    db = JSONDatabaseController()

    # test set 1
    db.create_collection('hello')
    db.create_collection('hello')
    print(db.get_collection('hello'))
    db.delete_collection('hello')
    db.delete_collection('hello')
    print(db.get_collection('hello'))

    # test set 2
    