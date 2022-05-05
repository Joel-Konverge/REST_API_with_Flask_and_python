from re import L
from flask_restful import Resource
from models.store import Storemodel

class Store(Resource):
    def get(self, name):
        store=Storemodel.find_by_name(name)
        if store:
             return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if Storemodel.find_by_name(name):
            return {f'message': "A store with name {name} already exists."}, 400
        store=Storemodel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating the store.'}, 500
        return {'message':'stored added'}, 201

    def delete(self, name):
        store=Storemodel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}

class Storelist(Resource):
    def get(self):
        return {"stores":[x.json() for x in Storemodel.find_all()]}
