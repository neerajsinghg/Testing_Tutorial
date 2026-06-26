import threading

class SingleTon:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    print("Singleton constructor called")
                    cls._instance = super(SingleTon, cls).__new__(cls)
        return cls._instance

    @classmethod
    def getInstance(cls):
        return cls()

# Thread safe singleton matching class SingletonExample
class SingletonExample:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = SingletonExample()
        return cls._instance

if __name__ == "__main__":
    obj1 = SingleTon.getInstance()
    obj2 = SingleTon.getInstance()
    print(obj1 is obj2)

    obj3 = SingletonExample.getInstance()
    obj4 = SingletonExample.getInstance()
    print(obj3 is obj4)
