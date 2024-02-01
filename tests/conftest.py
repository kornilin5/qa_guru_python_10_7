import os
import shutil

PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, "resources")
TMP_PATH = os.path.join(PROJECT_ROOT_PATH, "tmp")
NAME_FILES= 'пдф.pdf', 'эксель.xlsx', 'это_csv.csv'

os.makedirs(RESOURCES_PATH, exist_ok=True)
os.makedirs(TMP_PATH, exist_ok=True)








