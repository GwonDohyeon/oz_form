from services import get_choice_list,create_choice,get_choices_by_question_id
from flask_smorest import Blueprint
from flask import jsonify,request,abort

choice_blp=Blueprint('choices',__name__,url_prefix='/choice')
@choice_blp.route('/<int:question_id>',methods=['GET'])
def get_choices(question_id):
    choices=get_choices_by_question_id(question_id=question_id)
    return jsonify({"choices":choices}),200
@choice_blp.route('',methods=['POST'])
def post_new_choice():
    try:
        choice=request.get_json()
        new_choice=create_choice(choice)
        return jsonify({"message":f"Content: {new_choice['content']} choice Success Create"}),201
    except Exception as e:
        abort(500,str(e))