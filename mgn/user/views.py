import datetime
from flask import Blueprint, request, jsonify, json, Response
from mgn import mgn, db
from mgn.user.models import Testtable
from mgn.utils.constants import SUCCESS, ERROR, FAILURE, ADDED, DELETED, UPDATED


mod = Blueprint('user', __name__, url_prefix='')

@mod.route('/', methods=['POST'])
def addTest():
	try:
		dataRequest = request.get_json()
		name = dataRequest.get('name')
		desc = dataRequest.get('desc')
		if name != "" and desc != "":
			data = Testtable(
				name = name,
				desc = desc,
				updated = datetime.datetime.utcnow()
			)
			db.session.add(data)
			db.session.commit()
			SUCCESS["message"] = ADDED
			response = Response(json.dumps(SUCCESS), status=200, mimetype='application/json')
		else:
			response = Response(json.dumps(ERROR), status=400, mimetype='application/json')
	except:
		db.session.rollback()
		response = Response(json.dumps(FAILURE), status=500, mimetype='application/json')
	return response

@mod.route('/<int:id>', methods=['GET'])
def getTest(id=None):
	try:
		_states = Testtable.query.filter_by(id=id)
		response = jsonify(states=[i.serialize for i in _states.all()])
	except:
		response = Response(json.dumps(FAILURE), status=500, mimetype='application/json')
	return response

@mod.route('/', methods=['GET'])
def allTest():
	try:
		_states = Testtable.query
		response = jsonify(states=[i.serialize for i in _states.all()])
	except:
		response = Response(json.dumps(FAILURE), status=500, mimetype='application/json')
	return response

@mod.route('/<int:id>', methods=['PUT'])
def updateTest(id=None):
	try:
		dataRequest = request.get_json()
		name = dataRequest.get('name')
		desc = dataRequest.get('desc')
		data = Testtable.query.filter_by(id=id).update(dict(
			name = name,
			desc = desc,
			updated = datetime.datetime.utcnow()
        ))
		db.session.commit()
		SUCCESS["message"] = UPDATED
		response = Response(json.dumps(SUCCESS), status=200, mimetype='application/json')
	except:
		db.session.rollback()
		response = Response(json.dumps(FAILURE), status=500, mimetype='application/json')
	return response

@mod.route('/<int:id>', methods=['DELETE'])
def deleteTest(id=None):
	try:
		data = Testtable.query.filter_by(id=id).delete()
		db.session.commit()
		SUCCESS["message"] = DELETED
		response = Response(json.dumps(SUCCESS), status=200, mimetype='application/json')
	except:
		db.session.rollback()
		response = Response(json.dumps(FAILURE), status=500, mimetype='application/json')
	return response
