from flask_restful import Resource,reqparse
from models.user import Usermodel
from werkzeug.security import hmac
from flask_jwt_extended import create_access_token, create_refresh_token,get_jwt_identity,jwt_refresh_token_required,get_raw_jwt,jwt_required
from blacklist import BLACKLIST


parser=reqparse.RequestParser()
parser.add_argument('username',
type=str,
required=True,
help="This field cannot be left blank!")
parser.add_argument('password',
type=str,
required=True,
help="This field cannot be left blank!")



class UserRegister(Resource): 
    def post(self):
        data=parser.parse_args()
        
        if Usermodel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user=Usermodel(**data)# instead of data['username'],data['password'] we use kwargs
        user.save_to_db()
        
        return {"message": "User created successfully."}, 201



class User(Resource):
    @classmethod
    def get(cls, user_id):
        user=Usermodel.find_by_id(user_id)
        if not user:
             return {'message':'User not found'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user=Usermodel.find_by_id(user_id)
        if not user:
             return {'message':'User not found'}, 404
        user.delete_from_db()
        return {'message': 'User deleted'}, 200


class Userlogin(Resource):
    def post(self):
        data = parser.parse_args()
        user = Usermodel.find_by_username(data['username'])
        # this is what the authenticate function did in security.py
        if user and hmac.compare_digest(user.password,data['password']):
            # identity= is what the identity function did in security.py
            access_token = create_access_token(identity=user.id, fresh=True) 
            refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200

        return {"message": "Invalid Credentials!"}, 401

class Userlogout(Resource):
    @jwt_required
    def post(self):
        jti=get_raw_jwt()["jti"]  # jti is "JWT ID", a unique identifier for a JWT.
        BLACKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200

class Tokenrefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {"access_token": new_token}, 200
