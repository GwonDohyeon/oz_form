from app.services import get_answer_list,create_answer
from flask_smorest import Blueprint
from flask import jsonify,request,abort

answer_blp=Blueprint('answers',__name__)

@answer_blp.route('/submit',methods=['POST'])
def submit_answer():
    try:
        answers=request.get_json()
        result=[]
        user_id=""
        for answer in answers:
            user_id=answer['user_id']
            new_answer=create_answer(user_id=user_id,choice_id=answer['choice_id'])
            result.append(new_answer)
        return jsonify({"message": f"User: {user_id}'s answers Success Create"}),201
    except Exception as e:
        abort(500,str(e))
        

@answer_blp.route('/result',methods=['GET'])
def get_results():
    results=get_answer_list()
    return jsonify(results),201