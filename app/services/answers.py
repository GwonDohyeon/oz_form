from app.models import Answer,User,Choices
from config import db
from flask import abort

def create_answer(user_id,choice_id):
    try:
        User.query.get_or_404(user_id)
        Choices.query.get_or_404(choice_id)
        new_answer=Answer(user_id=user_id,choice_id=choice_id)
        db.session.add(new_answer)
        db.session.commit()
        return new_answer.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(400,str(e))
def get_answer_list():
    answers=Answer.query.all()
    return [answer.to_dict() for answer in answers]
    