from common_model import CommonModel
from config import db
from flask import abort
class Image(CommonModel):
    __tablename__ = "images"
    url = db.Column(db.TEXT, nullable=False)
    type = db.Column(db.String(10), nullable=False)

    __table_args__ = (
        db.CheckConstraint("type IN ('main', 'sub')", name="check_image_type"),
    )

    def __init__(self, url, image_type):
        allowed_type = {"main", "sub"}
        if image_type not in allowed_type:
            abort(400, f"Invalid type: {type}. Allowed values: {allowed_type}")

        self.url = url
        self.type = type

    questions = db.relationship("Question", back_populates="image")

    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "type": self.type.value if hasattr(self.type, "value") else self.type,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }