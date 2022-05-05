import sqlite3
from turtle import update
from flask_restful import Resource,reqparse
from flask_jwt_extended import jwt_required,get_jwt_claims,get_jwt_identity,jwt_optional,fresh_jwt_required
from models.item import Itemmodel


class Items(Resource):
    @jwt_optional
    def get(self):
        user_id=get_jwt_identity()
        items=[item.json() for item in Itemmodel.find_all()]
        if user_id:
            return {"items": items}, 200
        return {"items": [item["name"] for item in items],"message": "More data available if you log in.",}, 200

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

    @jwt_required
    def get(self,name):
        item=Itemmodel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    @fresh_jwt_required
    def post(self,name):
        if Itemmodel.find_by_name(name):
            return {'message':f"The given name {name} already exists"}
        data=Item.parser.parse_args()
        item=Itemmodel(name,**data) #data['price'],data['store_id']
        if item:
            item.save_to_db()
            return {'message':"item added sucessfully"}

    # @jwt_required()
    def delete(self,name):
        claims=get_jwt_claims()
        if not claims["is_admin"]:
            return {"message": "Admin privilege required."}, 401

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
       