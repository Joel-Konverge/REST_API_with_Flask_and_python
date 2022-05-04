from werkzeug.security import hmac
from models.user import Usermodel

def authenticate(username, password):
    user=Usermodel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
         return user

def identity(payload):
    user_id=payload['identity']
    return Usermodel.find_by_id(user_id)