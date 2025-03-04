from services import get_image_list,create_image,get_image_by_type
from flask_smorest import Blueprint
from flask import jsonify,request,abort

image_blp=Blueprint('images',__name__,url_prefix='/image')
@image_blp.route('/main',methods=['GET'])
def get_main_image():
    image=get_image_by_type("main")
    if not image or len(image)==0:
        abort(404, "No images found")
    return jsonify({"url": image[0]['url']}), 200
@image_blp.route('',methods=['POST'])
def post_new_image():
    try:
        image=request.get_json()
        new_image=create_image(url=image['url'],image_type=image['image_type'])
        return jsonify({"message":f"ID: {new_image['id']} Image Success Create"}),201
    except Exception as e:
        abort(500,str(e))