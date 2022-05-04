from flask import Flask,jsonify,request

app=Flask(__name__)

stores=[
    {
        'name': 'My Wonderful Store',
        'items':[
            {
             'name': 'My Item',
             'price': 15.99
            }
        ]
    }
]

#POST used to receive data
#GET used to send data back only

#POST /store data: (name:}
@app.route('/store', methods=['POST'])
def create_store():
   data=request.json
   stores.append({'name':data['name'],'items':[]})
   return jsonify({'message':'successfully added'})

#GET /store/<string:name>
@app.route('/store/<string:name>')#'http://127.0.0.1:5000/store/some_name
def get_store(name):
    for store in stores:
       if store['name']==name:
           return jsonify({'store':store})
    return jsonify({'message':"not found"})

#GET /store
@app.route('/store')
def get_stores ():
   return jsonify({'stores':stores})

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    data=request.json
    for store in stores:
        if store['name']==name:
            store['items'].append({'name':data['name'],'price':data['price']})
            return jsonify({'message':'item added successfully'})
    return jsonify({'message':'name not found'})


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name']==name:
           return jsonify(store['items'])
    return jsonify({'message':"not found"})
    

if __name__=="__main__":
    app.run()