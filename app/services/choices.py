from app.models import Choices
from config import db
from flask import abort

def create_choice(content,sqe,question_id,is_active=True):
    try:
        new_choice=Choices(content=content,sqe=sqe, question_id_id=question_id,is_active=is_active)
        db.session.add(new_choice)
        db.session.commit()
        return new_choice.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(400,str(e))
def get_choice_list():
    choices=Choices.query.all()
    return [choice.to_dict() for choice in choices]
def get_choices_by_question_id(question_id):
    choices=Choices.query.filter_by(question_id=question_id).all()
    if not choices:
        abort(404,message='No choices found.')
    return [choice.to_dict() for choice in choices]