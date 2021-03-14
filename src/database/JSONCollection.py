import json
from database.CollectionInterface import CollectionInterface

class JSONCollection(CollectionInterface):
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path) as f:
            self.data = json.load(f)
    
    def add_document(self, doc_name, doc_data = {}):
        if doc_name not in self.data:
            self.data[doc_name] = doc_data
        else:
            print('ERROR: Document already exists')
        self.save()

    def update_document(self, doc_name, doc_data = {}):
        if doc_name in self.data:
            self.data[doc_name] = { **self.data[doc_name], **doc_data }
        else:
            print('ERROR: Document does not exists')
        self.save()
    
    def delete_document(self, doc_name):
        if doc_name in self.data:
            self.data.pop(doc_name)
        else:
            print('ERROR: Document does not exist.')
        self.save()
    
    def get_document(self, doc_name):
        if doc_name in self.data:
            return self.data[doc_name]
        else:
            print('ERROR: Document does not exist.')
    
    def clear_document(self, doc_name):
        if doc_name in self.data:
            self.data[doc_name] = {}
        else:
            print('ERROR: Document does not exist.')
        self.save()

    def __repr__(self):
        return str(self.data)

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4)

if __name__ == '__main__':
    col = JSONCollection('./src/database/data/hello.json')
    # col.add_document('hello')
    col.update_document('hello2', {'a': 1, 'b': 2})
    col.update_document('hello2', {'c': 3, 'd': 4})
    
    col.add_document('hello2')
    col.clear_document('hello')
    col.delete_document('hello')
    print(col.get_document('hello2'))