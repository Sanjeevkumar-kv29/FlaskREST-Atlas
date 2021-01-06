from time import gmtime,strftime
from sys import displayhook
from flask import Flask, json
from flask import jsonify,request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from werkzeug.security import check_password_hash,generate_password_hash

app = Flask(__name__)

app.secret_key = 'secretkey'
#client = MongoClient("mongodb+srv://test:test@cluster0.gzwme.mongodb.net/CRUD?retryWrites=true&w=majority")
app.config['MONGO_URI'] = "mongodb+srv://test:test@cluster0.gzwme.mongodb.net/CRUD?retryWrites=true&w=majority" 
mongo = PyMongo(app)


@app.route('/addnewrecord',methods=['POST'])
def addrecord():

    json = request.json
    name = json['name']
    email = json['email']
    password = json['password']
    dateofadding = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    if name and email and password and request.method == 'POST':

        hashpass = generate_password_hash(password)
        datamap = {'name':name,'email':email,'password':hashpass,'date-of-adding':dateofadding}
        id = mongo.db.crud.insert_one(datamap)
        respons = jsonify('record added succesfully')
        respons.status_code = 200
        return respons
    
    else:
        errorthrow()


@app.route('/viewallrecord')
def viewallrecord():
    records = mongo.db.crud.find()
    response= dumps(records)
    return response


@app.route('/deleteDocumentbyid=<id>',methods=['DELETE'])
def deletedocument(id):
    mongo.db.crud.delete_one({'_id':ObjectId(id)})
    resp = jsonify('Document deleted successfully')
    resp.status_code = 200
    return resp


@app.route('/view-recordby-id-using-getrequest=<id>')
def viewrecordbyid(id):
    data = mongo.db.crud.find_one({'_id':ObjectId(id)})
    data = dumps(data)
    return data


@app.route('/view-recordby-id-using-postrequest',methods=['POST'])
def recordbyidusingPost():
    json = request.json
    id = json['id']

    if id and request.method == 'POST':
        resp = mongo.db.crud.find_one({'_id':ObjectId(id)})
        resp = dumps(resp)

        if resp == 'null':
            return notfounderror()
        else:
            return resp
    else:
        errorthrow()

    
@app.route('/updateRecord=<id>',methods = ['PUT'])
def updateRecord(id):
    mid =id
    json = request.json
    name = json['name']
    email = json['email']
    password = json['password']

    if name and email and password and request.method == 'PUT':
        
        updateddatamap = ({'name':name,'email':email,'password':password})
        mongo.db.crud.update_one({'_id':ObjectId(id['$oid']) if '$oid' in id else ObjectId(id)},{'$set':updateddatamap})

        resp = jsonify('updated succesfully')
        resp.status_code = 200
        return resp
    
    else:
        errorthrow()




@app.errorhandler(404)
def errorthrow(error = None):
    message = {
        'status':404,
        'message': 'not found'+request.url
            }

    resp = jsonify(message)
    resp.status_code = 404
    return resp

def notfounderror(error = None):
    message = {
        'status':404,
        'message':'document not found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    app.run(debug=True)

