from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.users import UserRegistration
from resources.Items import Item, Items_list
from resources.stores import Store, Store_list


app = Flask(__name__)
api = Api(app)
app.secret_key = 'satish_key'
jwt = JWT(app,authenticate,identity) #creates an end point "/auth"
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Store_list,'/stores')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items_list,'/items')
api.add_resource(UserRegistration,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug= True)




