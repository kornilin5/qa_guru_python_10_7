import os
from openpyxl import load_workbook
from pypdf import PdfReader
import csv


def test_read_csv(create_zip_archive):
    path = os.path.join(create_zip_archive, 'это_csv.csv')
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        names = [row['USERTEST1'] for row in reader]
        print(names)


def test_read_xlsx_file(create_zip_archive):
    path = os.path.join(create_zip_archive, 'эксель.xlsx')
    open_xlsx = load_workbook(path)
    sheet = open_xlsx.active
    text = sheet.cell(row=2, column=2).value
    text_found = "Регистрация пользователя на сайте при вводе корректного пароля"
    assert text == text_found


def test_read_pdf(create_zip_archive):
    path = os.path.join(create_zip_archive, "пдф.pdf")
    text = "Пример PDF файла"
    with open(path, 'rb') as file:
        reader = PdfReader(file)
        assert any(text in page.extract_text() for page in reader.pages)
