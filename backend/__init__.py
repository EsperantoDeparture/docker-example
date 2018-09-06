from flask import Flask, request
from flask_restplus import Api, Resource
from database import Database
from swagger_models import *

app = Flask(__name__)
api = Api(app)

new_todo = api.schema_model("NewTodo", new_todo)
todo = api.schema_model("Todo", todo)


@api.route('/list')
class List(Resource):
    @api.doc(summary='Get all todos',
             description='Returns a collection of todos',
             responses={200: ('Collection of todos', [todo])})
    def get(self):
        return Database().list(), 200


@api.route('/add')
class Add(Resource):
    @api.expect(new_todo)
    def post(self):
        Database().add(request.get_json(force=True) or {})
        return {'message': 'The todo has been added successfully'}, 201


@api.route('/<string:tid>/delete')
class Delete(Resource):
    def delete(self, tid):
        Database().delete(tid)
        return {'message': 'The todo has been nuked successfully'}, 200


@api.route('/<string:tid>/edit')
class Edit(Resource):
    @api.expect(new_todo)
    def put(self, tid):
        Database().edit(request.get_json(force=True) or {}, tid)
        return {'message': 'Todo edited'}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
