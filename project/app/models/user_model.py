from flask import abort
from common_model import CommonModel
from config import db
class User(CommonModel):
    __tablename__ = "users"
    name = db.Column(db.String(10), nullable=False)
    age = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    __table_args__ = (
        db.CheckConstraint("age IN ('teen', 'twenty', 'thirty', 'fourty', 'fifty')", name="check_age"),
        db.CheckConstraint("gender IN ('male', 'female')", name="check_gender"),
    )

    def __init__(self, name, age, gender, email):
        allowed_ages = {"teen", "twenty", "thirty", "fourty", "fifty"}
        allowed_genders = {"male", "female"}

        if User.query.filter_by(email=email).first():
            abort(400, "이미 존재하는 계정 입니다.")

        if age not in allowed_ages:
            abort(400, f"Invalid age: {age}. Allowed values: {allowed_ages}")

        if gender not in allowed_genders:
            abort(400, f"Invalid gender: {gender}. Allowed values: {allowed_genders}")

        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
