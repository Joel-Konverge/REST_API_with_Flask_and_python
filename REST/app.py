from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required

from security import authenticate,identity


app=Flask(__name__)
api=Api(app)
app.secret_key="joel"

jwt=JWT(app,authenticate,identity) #/auth

items=[{'name':"chair",'price':15}]

class Items(Resource):
    def get(self):
        return {'items':items}

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument ('price',
    type=float,
    required=True,
    help="This field cannot be left blank!")
    
    @jwt_required()
    def get(self,name):
        item=next(filter(lambda item:item['name']==name,items),None)
        return {'items':item},200 if item  else 404
    '''
    as the above code has a decorator jwt_required the get will throw this error without the access token.
    {
    "description": "Request does not contain an access token",
    "error": "Authorization Required",
    "status_code": 401
    }
    we need to add the access token in the header the get the data 
    '''
    def post(self,name):
        if next(filter(lambda x:x['name']==name,items),None):
            return {'message':f"The given name {name} already exists"}
        data=Item.parser.parse_args()
        items.append({'name':name,'price':data['price']})
        return {'message':"item added successfully"}
    
    def delete(self,name):
        global items
        items=list(filter(lambda x:x['name']!=name,items))
        return {'message':f'{name} deleted successfully'}


    def put(self,name):
        data=Item.parser.parse_args()
        item=next(filter(lambda item:item['name']==name,items),None)
        if item:
            item.update(data)
        else:
            items.append({'name':name,'price':data['price']})
        return {"message":"Update successful"}


api.add_resource(Items,"/items")
api.add_resource(Item,"/item/<string:name>")



if __name__=="__main__":
    app.run(debug=True)