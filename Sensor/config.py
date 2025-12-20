from dataclasses import dataclass
import os
import pymongo

#The @dataclass decorator automatically generates all these methods like __init__(), __repr__() (print-friendly representation)
# for you.
@dataclass   # this is a decorator

class EnvironmentVariable:
    mongo_db_url: str=os.getenv('MONGO_DB_URL')

env_obj=EnvironmentVariable()

client = pymongo.MongoClient(env_obj.mongo_db_url)