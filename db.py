from pymongo import MongoClient

# MongoDB connection URI
MONGO_URI = "mongodb://localhost:27017/"

# Function to connect to MongoDB
def connect_to_mongodb():
    client = MongoClient(MONGO_URI)
    return client