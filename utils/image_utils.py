import os

def save_image(image_file, upload_folder):
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    filepath = os.path.join(upload_folder, image_file.filename)
    image_file.save(filepath)
    return filepath