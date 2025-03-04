from app.models import User
from config import db
from flask import abort

def create_user(name, age, gender, email):
    try:
        new_user=User(name=name,age=age,gender=gender,email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(400,str(e))
def get_user_list():
    users=User.query.all()
    return [user.to_dict() for user in users]
    