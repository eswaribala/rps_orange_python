'''
Created on 18-Jul-2017

@author: BALASUBRAMANIAM
'''
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

USERS = {
    'user1': {'name': 'jersey', 'email':'jersey@gmail.com'},
    'user2': {'name': 'lalit','email':'lalit@gmail.com'},
    'user3': {'name': 'sunil','email':'sunil@gmail.com'},
}


def abort_if_user_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="User {} doesn't exist".format(user_id))

parser = reqparse.RequestParser()
parser.add_argument('user', type=str)


# User
#   show a single user and lets you delete them
class User(Resource):
    def get(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        return USERS[user_id]

    def delete(self, user_id):
        abort_if_user_doesnt_exist(user_id)
        del USERS[user_id]
        return '', 204

    def put(self, user_id):
        args = parser.parse_args()
        name = {'name': args['name'],'email':args['email']}
        USERS[user_id] = name
        return user_id, 201


# UserList
#   shows a list of all users, and lets you POST to add new users
class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        user_id = 'user%d' % (len(USERS) + 1)
        USERS[user_id] = {'name': args['name'],'email': args['email']}
        return USERS[user_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<string:user_id>')

if __name__ == '__main__':
    app.run( 
        host="127.0.0.1",
        port=int("5000")
  )