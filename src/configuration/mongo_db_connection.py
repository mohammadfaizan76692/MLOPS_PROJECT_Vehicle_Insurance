import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# laod there certificate authority file to avoid timeout errors when connecting to MongoDB
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to the MongoDB database.

    Attributes
    ----------

    client (class Attribute)  : MongoClient 
        A shared MongoClient instance for the class.

    database : Database
        The specific database instance that MongoDBClient connects to.

    Methods:
    -------
    __init__(database_name: str) -> None
    Initializae the MongoDB connection using the given database name

    """

    client = None # class attribute , shared MongoClient instance across all MongoDBClient instances

    def __init__(self, database_name : str =DATABASE_NAME)-> None:
        """
        Initialize a connection to the MongoDB database. if no existing connection is found, it establishes a new one

        Parameters:

        database_name: str, optional
            Name of the MongoDB database to connect to. Default is set by DATABASE_NAME constant.
        
        Raises:
        MyException
            if there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.

        """

        try:
            # check if a MongoDB client connection has already been Established: if not, creat one
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY) # Retrieve MongoDB url from environment variables

                if mongo_db_url is None:
                    raise Exception(f"Environment Variable '{MONGODB_URL_KEY}' is not set.")
                
                #Establish a new MongoDB client connection
                MongoDBClient.client  = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
            
            # use the shared MongoClient for this instance
            self.client =MongoDBClient.client
            self.database_name = database_name
            self.database=  self.client[self.database_name]

            logging.info("MongoDB connection Successful.")
        
        except Exception as e:
            # Raise a custom exception with traceback details if connection fails
            raise MyException(e, sys)
    

