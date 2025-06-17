class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("singleton class")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance(self):
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

class Logger:
    __instance = None

    def __init__(self):
        if Logger.__instance is not None:
            raise Exception("This is a singleton class. Use get_instance()")
        else:
            Logger.__instance = self
            self.logs = []

    @staticmethod
    def get_instance():
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def log(self, message):
        self.logs.append(message)
        print(f"LOG: {message}")

    def show_logs(self):
        for msg in self.logs:
            print(f"> {msg}")



class StaticCache:
    __instance = None
    def __init__(self):
        if StaticCache.__instance is not None:
            raise Exception("singleton class")
        else:
            StaticCache.__instance = self
            self.cache = {}

    @staticmethod
    def get_instance():
        if StaticCache.__instance is None:
            StaticCache()
        return StaticCache.__instance
    
    def add_value(self,key,value):
        self.cache[key] = value

    def get_value(self,key):
        if key in self.cache:
            return self.cache[key]
        return None


class Client:
    def __init__(self):
        self.staticInstance = StaticCache.get_instance()
    
    def add(self):
        self.staticInstance.add_value("hi",123)



'''
PYTHONIC WAY
In Python, everything is an object, and classes themselves are instances of a class called type.
So when you create a metaclass, you are essentially customizing how classes are created, by inheriting from type.

class SingletonMeta(type):
We're telling Python to use this metaclass to control how classes (that use this metaclass) are instantiated

What are *args and **kwargs?
These are used to accept any number of positional and keyword arguments, respectively.

*args: collects all positional arguments into a tuple.

**kwargs: collects all keyword arguments into a dictionary.
'''
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__class__(*args,**kwds)
        return cls._instances[cls]

class ConfigReader(metaclass=SingletonMeta):
    def __init__(self):
        self.config = {}
        self._load_config()

    def _load_config(self):
        self.config = {
            "db_host": "localhost",
            "db_port": 5432,
            "api_key": "xyz-123",
        }

    def get(self, key):
        return self.config.get(key)

class AppService:
    def __init__(self):
        self.config = ConfigReader()

    def connect(self):
        host = self.config.get('host')
        port = self.config.get('port')
        print(f"Connecting to DB at {host}:{port}")


