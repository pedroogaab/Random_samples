import shutil
import os

src_folder = '/folder/origin/'
dest_folder = '/folder/destiny/'

for camera_dir in os.scandir(src_folder):
    if camera_dir.is_dir():
        dest_camera_dir = os.path.join(dest_folder, camera_dir.name)
        os.makedirs(dest_camera_dir, exist_ok=True)
        for file in os.scandir(camera_dir.path):
            if file.is_file() and file.name.endswith('.json'):
                shutil.copy(file.path, os.path.join(dest_camera_dir, file.name))

