from flask_restful import Resource
from app import db, api


class MessageAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class MessageListAPI(Resource):
    def get(self):
        pass



api.add_resource(MessageAPI, '/api/v1.0/message/<int:id>', endpoint='message')
api.add_resource(MessageListAPI, '/api/1.0/message', endpoint='messages')