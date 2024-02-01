import os
import shutil

PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, "resources")
TMP_PATH = os.path.join(PROJECT_ROOT_PATH, "tmp")
NAME_FILES= 'пдф.pdf', 'эксель.xlsx', 'это_csv.csv'

os.makedirs(RESOURCES_PATH, exist_ok=True)
os.makedirs(TMP_PATH, exist_ok=True)








# def reader_archive(archive_path, archive_file_name):
#     archive_file_path = os.path.join(archive_path, archive_file_name)
#     with zipfile.ZipFile(archive_file_path, 'r') as reader:
#         text_csv = reader.read('это csv.csv').decode()
#         text_excel = load_workbook(archive_path'эксель.xlsx'))
#         print(reader.namelist())
#         print (text_csv)
#         print(F"eto exel {text_xlsx[0]}")