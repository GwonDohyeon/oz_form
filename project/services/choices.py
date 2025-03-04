from app.models import Choices
from config import db
from flask import abort

def create_question(content,sqe,question_id,is_active=True):
    try:
        new_choice=Choices(content=content,sqe=sqe, question_id_id=question_id,is_active=is_active)
        db.session.add(new_choice)
        db.session.commit()
        return new_choice.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(400,str(e))
def get_questions_list():
    choices=Choices.query.all()
    return [choice.to_dict() for choice in choices]
    