from services import get_question_list,create_question,get_question_by_id
from flask_smorest import Blueprint
from flask import jsonify,request,abort

question_blp=Blueprint('questions',__name__)
@question_blp.route('/questions/<int:question_id>',methods=['GET'])
def get_question(question_id):
    question=get_question_by_id(question_id)
    return jsonify(question),200
@question_blp.route('/questions/count',methods=['GET'])
def count_questions():
    questions=get_question_list()
    return jsonify({"total":len(questions)}),200
@question_blp.route('/question',methods=['POST'])
def post_new_question():
    try:
        question=request.get_json()
        new_question=create_question(question)
        return jsonify({"message":f"Title: {new_question['title']} question Success Create"}),201
    except Exception as e:
        abort(500,str(e))