import os
from PIL import Image
from werkzeug.utils import secure_filename
from flask import current_app

def add_profile_pic(pic_upload,username):
    try:
        filename = secure_filename(pic_upload.filename or "")
        if not filename:
            return None

        _, ext_type = os.path.splitext(filename)
        ext_type = ext_type.lower()
        if not ext_type:
            return None

        safe_username = secure_filename(str(username))
        if not safe_username:
            return None

        storage_filename = f"{safe_username}{ext_type}"
        filepath = os.path.join(current_app.root_path,'static','profile_pics',storage_filename)

        output_size = (200,200)

        pic = Image.open(pic_upload)
        pic.thumbnail(output_size)
        pic.save(filepath)

        return storage_filename
    except Exception as e:
        print(f"Error processing profile picture: {e}")
        return None
