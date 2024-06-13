import pymongo

# MongoDB connection params
aws_mongo_host = "13.42.111.186"
aws_mongo_user = "user_345893"
aws_mongo_pwd = "ret453mFkT45d"
aws_mongo_client = pymongo.MongoClient(
    f"mongodb://{aws_mongo_user}:{aws_mongo_pwd}@{aws_mongo_host}:27017/?retryWrites=false&w=majority"
)

# db and collection names
db_name = 'opply_interview'
quote_collection_name = 'quotes_ernest'
request_collection_name = 'requests_ernest'

# Data science challenge dataframe
db = aws_mongo_client[db_name]

collection_payload = {quote_collection_name:db[quote_collection_name],
                      request_collection_name:db[request_collection_name]}