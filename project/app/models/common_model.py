from datetime import datetime
from zoneinfo import ZoneInfo
from config import db

KST = ZoneInfo("Asia/Seoul")
class CommonModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime, default=lambda: datetime.now(tz=KST), nullable=False
    )
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(tz=KST),
        onupdate=lambda: datetime.now(tz=KST),
        nullable=False,
    )
