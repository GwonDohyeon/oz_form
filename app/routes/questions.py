from app.services import get_question_list,create_question,get_question_by_id,get_choices_by_question_id
from flask_smorest import Blueprint
from flask import jsonify,request,abort
import logging
logging.basicConfig(level=logging.DEBUG)

question_blp=Blueprint('questions',__name__)
@question_blp.route('/questions/<int:question_id>',methods=['GET'])
def get_question(question_id):
    question=get_question_by_id(question_id)
    try:
        choices=get_choices_by_question_id(question_id=question.get('id'))
    except:
        choices=[]
    return jsonify({"id":question.get('id'),
                    "title":question.get('title'),
                    "image":question.get('image').get('url'),
                    "choices":choices}),200
@question_blp.route('/questions/count',methods=['GET'])
def count_questions():
    questions=get_question_list()
    return jsonify({"total":len(questions)}),200
@question_blp.route('/question',methods=['POST'])
def post_new_question():
    try:
        question=request.get_json()
        new_question=create_question(title=question['title'],sqe=question['sqe'],
                                     image_id=question['image_id'],is_active=question.get('is_active',True))
        return jsonify({"message":f"Title: {new_question['title']} question Success Create"}),201
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        abort(500,str(e))