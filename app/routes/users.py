from app.services import get_user_list,create_user
from flask_smorest import Blueprint
from flask import jsonify,request,abort
import logging
logging.basicConfig(level=logging.DEBUG)

user_blp=Blueprint('users',__name__)
@user_blp.route('/signup',methods=['POST'])
def signup():
    try:
        data=request.get_json()
        new_user=create_user(name=data['name'], age=data['age'], gender=data['gender'], email=data['email'])
        return jsonify({"message": f"{new_user['name']}님 회원가입을 축하합니다", 
                        "user_id": new_user['id']}),201
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        abort(500,str(e))