import sqlite3
from turtle import update
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import Itemmodel


class Items(Resource):
    def get(self):
        return {"items":list(map(lambda x:x.json(),Itemmodel.query.all()))} 

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument ('price',
    type=float,
    required=True,
    help="This field cannot be left blank!")
    
    parser.add_argument ('store_id',
    type=int,
    required=True,
    help="This field cannot be left blank!")

    @jwt_required()
    def get(self,name):
        item=Itemmodel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

 
    def post(self,name):
        if Itemmodel.find_by_name(name):
            return {'message':f"The given name {name} already exists"}
        data=Item.parser.parse_args()
        item=Itemmodel(name,**data) #data['price'],data['store_id']
        if item:
            item.save_to_db()
            return {'message':"item added sucessfully"}

    def delete(self,name):
        item=Itemmodel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message':f'{name} deleted successfully'}
        return {'message': 'Item not found.'}, 404

    def put(self,name):
        data=Item.parser.parse_args()
        item=Itemmodel.find_by_name(name)
        if item:
            item.price=data['price']
        else:
            item=Itemmodel(name,**data) #data['price'],data['store_id']
        
        item.save_to_db()

        return {"message":"Update successful"}
       