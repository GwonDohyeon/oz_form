from app.models import Image
from config import db
from flask import abort

def create_image(url, image_type):
    try:
        new_image=Image(url=url,image_type=image_type)
        db.session.add(new_image)
        db.session.commit()
        return new_image.to_dict()
    except Exception as e:
        db.session.rollback()
        abort(400,str(e))
def get_image_list():
    images=Image.query.all()
    return [image.to_dict() for image in images]
def get_image_by_type(image_type):
    images=Image.query.filter(Image.image_type==image_type).all()
    return [image.to_dict() for image in images]