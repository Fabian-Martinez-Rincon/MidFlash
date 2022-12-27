import os
PATH_BASE = os.getcwd()
PATH_SOURCE = os.path.join(PATH_BASE, "base_images")
PATH_PROSSED = os.path.join(PATH_BASE, "processed_images")
PATH_PROSSED_RESOLUTION = os.path.join(PATH_BASE, "processed_resolution_images")

files = os.listdir(PATH_PROSSED_RESOLUTION)
for i, file in enumerate(files):
  old_path = os.path.join(PATH_PROSSED_RESOLUTION, file)
  new_path = os.path.join(PATH_PROSSED_RESOLUTION, "nomadiix_{}.jpg".format(i+1))
  os.rename(old_path, new_path)