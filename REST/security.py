from werkzeug.security import hmac

#with the help of class
from user import User

users=[User(1,'joel','abcd')]
username_mapping={u.username:u for u in users}  #u is the class object
userid_mapping={u.id:u for u in users}
                  

#without class

# users=[
#     {
#         'id': 1,
#         'username': 'joel',
#         'password': 1234
#     }
# ]

# #create these so that no need to iterate over the list of user get the value directly by username_mapping['name'] or userid_mapping['id']
# username_mapping={'joel':    {
#         'id': 1,
#         'username': 'joel',
#         'password': 1234
#     }}

# userid_mapping={1:    {
#         'id': 1,
#         'username': 'joel',
#         'password': 1234
#     }}



def authenticate(username, password):
    user=username_mapping.get(username, None)
    #we can use safe_str_cmp for secure string comparison .To use it werkzeug should be of version 2.0.0 and hmac for the later versions
    #this should be a string
    if user and hmac.compare_digest(user.password, password):
        return user
    #without it
    # if user and user.password == password:
    #      return user


def identity(payload):
    user_id=payload['identity'] 
    return userid_mapping.get(user_id, None)