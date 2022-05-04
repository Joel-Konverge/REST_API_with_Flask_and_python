from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,Items
from resources.store import Store, Storelist

from db import db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app)
app.secret_key="joel"

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity) #/auth

api.add_resource(Items,"/items")
api.add_resource(Item,"/item/<string:name>")
api.add_resource(UserRegister,"/register")
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Storelist, '/stores')


if __name__=="__main__":
    db.init_app(app)
    app.run(debug=True)