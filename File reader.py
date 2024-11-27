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

def file_type(file):
    if file.endswith(file_types["PICTURES"]):
        final_path = user_path + '/Pictures'
        return final_path
    elif file.endswith(file_types["DOCUMENTS"]):
        final_path = user_path + '/Documents'
        return final_path
    else:
        return None

def creation_time(file):
    creation_time = os.path.getctime(file)
    creation_date = time.ctime(creation_time)
    return creation_date



# while True:
#
#         if schedule["WORK"][0] < x.hour < schedule["WORK"][1] and x.strftime("%a") in schedule["DAY"]:
#             print("On work schedule")
#             # Moving files based on
#             for entry in list_dirs:
#                 print("checking" + entry)
#                 destination = file_type(entry)
#                 if destination:
#                     print(destination)
#                     entry_path = cwd + '/' + entry
#                     os.chmod(entry_path, 0o666)
#                     shutil.move(entry_path, destination)
#                     print('Moved', entry, 'to', destination)
#                 else:
#                     print(entry + "Not sortable file type.")
#
#
#         time.sleep(5)

def process_date(string, index):
    # Indexes: 0 = day (week), 1 = month, 2 = day (month), 3 = time, 4 = year.
    parts = string.split()
    return parts[index]

def time_files(directory, year, month, day, time=None):
    if time is not None:
        for entry in directory:
            entry_year = process_date(entry, 4)
            entry_month = process_date(entry, 2)
            entry_day = process_date(entry, 3)

