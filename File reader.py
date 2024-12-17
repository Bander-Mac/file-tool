import os
import datetime
import shutil
import time
from ctypes import create_string_buffer

# Assign times to different folders
x = datetime.datetime.now()

schedule = {
    "WORK": (20, 22),
    "DAY": ("Mon", "Wed", "Fri", "Sun")
}


# Switch working directory to root.
os.chdir('../../')
os.chdir('pictures/')
cwd = os.getcwd()
list_dirs = os.listdir(cwd)
os.chdir('../')
print(os.getcwd())
os.chdir('Work/')
user_path = os.getcwd()

file_types = {
    "PICTURES": ('.svg', '.jpg', '.jpeg', '.png', '.HEIC'),
    "DOCUMENTS": ('.docx', '.pdf', '.txt', '.html')
}

Schedule = {
    "Work": None,
    "Coding": None,
    "School": None
}

def file_type(file):
    if file.endswith(file_types["PICTURES"]):
        final_path = user_path + '/Pictures'
        return final_path
    elif file.endswith(file_types["DOCUMENTS"]):
        final_path = user_path + '/Documents'
        return final_path
    else:
        return None

def creation_time(file_dir):
    creation_time = os.path.getctime(file_dir)
    creation_date = time.ctime(creation_time)
    return creation_date

def process_date(string, index):
    # Indexes: 0 = day (week), 1 = month, 2 = day (month), 3 = time, 4 = year.
    parts = string.split()
    return parts[index]




