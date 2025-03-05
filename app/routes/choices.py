from app.services import get_choice_list,create_choice,get_choices_by_question_id
from flask_smorest import Blueprint
from flask import jsonify,request,abort
import logging
logging.basicConfig(level=logging.DEBUG)

choice_blp=Blueprint('choices',__name__,url_prefix='/choice')
@choice_blp.route('/<int:question_id>',methods=['GET'])
def get_choices(question_id):
    try:
        choices=get_choices_by_question_id(question_id=question_id)
    except:
        choices=[]
    return jsonify({"choices":choices}),200
@choice_blp.route('',methods=['POST'])
def post_new_choice():
    try:
        choice=request.get_json()
         # 필수 필드 검증
        if not all(key in choice for key in ['content', 'sqe', 'question_id']):
            return jsonify({"message": "필수 필드가 누락되었습니다: 'content', 'sqe', 또는 'question_id'"}), 400
       
        new_choice=create_choice(content=choice['content'],sqe=choice['sqe'],
                                 question_id=choice['question_id'],is_active=choice.get('is_active',True))
        return jsonify({"message":f"Content: {new_choice['content']} choice Success Create"}),201
    except KeyError as e:
        logging.error(f"Missing field: {str(e)}")
        return jsonify({"message": f"필드 누락: {str(e)}"}), 400
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        abort(500,str(e))