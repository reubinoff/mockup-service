import time
import cloudshell.api.cloudshell_api as api


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
        results = run_test(data["host"], data["port"])
        return jsonify(res)

    def run_test(self,ip, sandboxId):
        session = api.CloudShellAPISession(ip, 'admin', 'admin', 'Global')
        resourceDict = {}
        for resource in session.GetReservationDetails(reservationId=sandboxId).ReservationDescription.Resources:
            attributeDict = {}
            for attribute in session.GetResourceDetails(resource.Name).ResourceAttributes:
                attributeDict[attribute.Name] = attribute.Value
            resourceDict[resource.Name] = attributeDict
        return resourceDict


if __name__ == '__main__':
    print returnResources('localhost', '33b2b0e4-2c69-4525-a15c-798081ad4543')



api.add_resource(Home, '/')
api.add_resource(Perfecto, '/perfecto')
api.add_resource(Robot, '/robot')
