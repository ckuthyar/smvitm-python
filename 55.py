import os
dir1="Deepawali"
if not os.path.exists(dir1):
    os.makedirs(dir1)

dir2="Diwali"
os.makedirs(dir2,exist_ok=True)
