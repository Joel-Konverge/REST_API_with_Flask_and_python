from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from user import UserRegister
from item import Item,Items

app=Flask(__name__)
api=Api(app)
app.secret_key="joel"

jwt=JWT(app,authenticate,identity) #/auth

api.add_resource(Items,"/items")
api.add_resource(Item,"/item/<string:name>")
api.add_resource(UserRegister,"/register")


if __name__=="__main__":
    app.run(debug=True)