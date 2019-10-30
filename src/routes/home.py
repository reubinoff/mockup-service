import time

from flask import Flask, jsonify, Response
from flask_restful import Resource, marshal_with, abort
from .. import  api
from .helpers import expect_json_data

class Home(Resource):
	def get(self):
		return jsonify({
			"ROBOT":{
				"GET": "/robot",
				"POST": "/robot"
			},
			"PERFECTO":{
				"POST": "/perfecto",
				"DELETE": "/perfecto"
			}
		})

class Perfecto(Resource):
    def get(self):
        time.sleep(1)
        return jsonify({"status": True})
    
    @expect_json_data
    def post(self, data):
        time.sleep(2)
        res = {"action": "checked-in", "data": data, "status": True}
        return jsonify(res)

    def delete(self):
        time.sleep(1)
        return jsonify({"action": "checked-out", "status": True})

class Robot(Resource):
    def get(self):
        time.sleep(1)
        return jsonify({"status": True})
    
    @expect_json_data
    def post(self, data):
        time.sleep(2)
        res = {"data": data, "status": True}
        return jsonify(res)


api.add_resource(Home, '/')
api.add_resource(Perfecto, '/perfecto')
api.add_resource(Robot, '/robot')
