import os
import zipfile
import pytest


CURRENT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = os.path.join(CURRENT, 'tmp')
RESOURCES = os.path.join(CURRENT, 'resources')
ARCHIVE = os.path.join(RESOURCES, 'archive.zip')
FILES_LIST = os.listdir(TMP)

@pytest.fixture
def create_zip_archive():
    if not os.path.exists(RESOURCES):
        os.mkdir(RESOURCES)
    with zipfile.ZipFile(ARCHIVE, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in FILES_LIST:
            add_file = os.path.join(TMP, file)
            zf.write(add_file, os.path.basename(add_file))
    with zipfile.ZipFile(ARCHIVE, 'r') as zip_ref:
        zip_ref.extractall(TMP)
    yield TMP
    os.remove(ARCHIVE)