import sqlite3
from turtle import update
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class Items(Resource):
    def get(self):
        connection=sqlite3.connect ('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM items"
        result=cursor.execute(query)
        items=result.fetchall()
        connection.close() 
        return {"items":items}      

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument ('price',
    type=float,
    required=True,
    help="This field cannot be left blank!")
    
    @jwt_required()
    def get(self,name):
        item=self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection=sqlite3.connect ('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM items WHERE name=?"
        result=cursor.execute(query, (name,))
        row=result.fetchone()
        connection.close()
        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
 
    def post(self,name):
        if self.find_by_name(name):
            return {'message':f"The given name {name} already exists"}
        data=Item.parser.parse_args()
        item={'name': name, 'price': data['price']}
        try:
            self.insert(item)
            return {'message':"item added sucessfully"}
        except:
           return {"message":"An error occured"},500 #internal server error


    @classmethod
    def insert(cls,item):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()
        return {'message':"item added successfully"},201
    
    def delete(self,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message':f'{name} deleted successfully'}


    def put(self,name):
        data=Item.parser.parse_args()
        item=self.find_by_name(name)
        updated_item={'name':name,'price':data['price']}
        if item:
            try:
                self.update(updated_item)
            except:
                {"message":"An error occured"},500
        else:
            try:
                self.insert(updated_item)
            except:
                {"message":"An error occured"},500

        return {"message":"Update successful"}

    
    @classmethod
    def update(cls,item):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'],item['name']))
        connection.commit()
        connection.close()       