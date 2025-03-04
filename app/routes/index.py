from flask_smorest import Blueprint
from flask import jsonify

index_blp=Blueprint('index',__name__)

@index_blp.route('/',methods=['GET'])
def index():
    return jsonify({"message": "Success Connect"}),200
