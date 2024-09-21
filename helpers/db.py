from typing import Optional, Tuple

from pymongo.mongo_client import MongoClient


# def get_user_data(client: MongoClient) -> Optional[Tuple[str, str]]:
#     """
#     Retrieve the username and password for the 'admin' user from MongoDB using the provided client.
#
#     Args:
#         client: The MongoClient instance to use.
#
#     Returns:
#         A tuple of (username, password) if the user is found, else None.
#     """
#     db = client['testdb']
#     users_collection = db['users']
#     user = users_collection.find_one({'username': 'admin'})
#     if user:
#         return user['username'], user['password']
#     else:
#         print('User not found')
#         return None
