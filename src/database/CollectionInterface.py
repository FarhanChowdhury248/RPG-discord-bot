import abc

class CollectionInterface(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def add_document(self, doc_name, doc_data = {}):
        raise NotImplementedError
    
    @abc.abstractmethod
    def update_document(self, doc_name, doc_data = {}):
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete_document(self, doc_name):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_document(self, doc_name):
        raise NotImplementedError

    @abc.abstractmethod
    def clear_document(self, doc_name):
        raise NotImplementedError

if __name__ == '__main__':
    
    class MockCollection(CollectionInterface):
        '''
        This is a mock instance using the interface above.
        Commenting out any of the below methods should raise
        a NotImplementedError upon instantiation.
        '''
        def add_document(self, col_name, doc_name, doc_data = {}):
            pass
        def update_document(self, col_name, doc_name, doc_data = {}):
            pass
        def delete_document(self, col_name, doc_name):
            pass
        def get_document(self, col_name, doc_name):
            pass
        def clear_document(self, doc_name):
            pass

    col = MockCollection()
    print(isinstance(col, CollectionInterface))