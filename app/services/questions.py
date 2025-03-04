from app.models import Question
from config import db
from flask import abort

def create_question(title,sqe,image_id,is_active=True):
    try:
        new_question=Question(title=title, sqe=sqe, image_id=image_id,is_active=is_active)
        db.session.add(new_question)
        db.session.commit()
        return new_question.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(400,str(e))
def get_question_list():
    questions=Question.query.all()
    return [question.to_dict() for question in questions]
def get_question_by_id(id):
    question=Question.query.get_or_404(id)
    return question.to_dict()