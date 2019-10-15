from flask import Flask, jsonify, Response
from flask_restful import Resource, marshal_with, abort
from .. import  api

class Home(Resource):
	def get(self):
		data = {'success': True}
		return jsonify(data)

api.add_resource(Home, '/')