import json
from CollectionInterface import CollectionInterface

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

    def update_document(self, doc_name, doc_data = {}):
        if doc_name in self.data:
            self.data[doc_name] = { **self.data[doc_name], **doc_data }
        else:
            print('ERROR: Document does not exists')
    
    def delete_document(self, doc_name):
        pass
    
    def get_document(self, doc_name):
        pass
    
    def clear_document(self, doc_name):
        pass

    def save(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.data, f, indent=4, sort_keys=True)

if __name__ == '__main__':
    col = JSONCollection('./src/database/data/hello.json')
    col.add_document('hello')
    # col.update_document('hello', {'a': 1, 'b': 2})
    col.update_document('hello', {'c': 3, 'd': 4})
    col.add_document('hello2')
    col.save()