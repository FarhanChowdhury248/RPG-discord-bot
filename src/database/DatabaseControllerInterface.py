import abc

class DatabaseControllerInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_collection(self, col_name):
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete_collection(self, col_name):
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_collection(self, col_name):
        raise NotImplementedError

    @abc.abstractmethod
    def clear_collection(self, col_name):
        raise NotImplementedError
    
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

    class MockDatabaseController(DatabaseControllerInterface):
        '''
        This is a mock controller using the interface above.
        Commenting out any of the below methods should raise
        a NotImplementedError upon instantiation.
        '''
        def create_collection(self, col_name):
            pass
        def delete_collection(self, col_name):
            pass
        def get_collection(self, col_name):
            pass
        def clear_collection(self, col_name):
            pass
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

    db = MockDatabaseController()
    print(isinstance(db, DatabaseControllerInterface))