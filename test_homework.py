import zipfile
import os
import PyPDF2
import openpyxl
import pytest


@pytest.fixture
def zip_file():
    file_names = [os.path.abspath('file1.pdf'), os.path.abspath('file2.xlsx'), os.path.abspath('file3.csv')]

    zip_file = zipfile.ZipFile('resources/archive.zip', 'w')
    for file_name in file_names:
        if os.path.exists(file_name):
            zip_file.write(file_name, os.path.basename(file_name))
        else:
            print(f"Файл {file_name} не найден!")
    zip_file.close()


def test_read_dpf(zip_file):
    with zipfile.ZipFile('resources/archive.zip', 'r') as zip_file:
        with zip_file.open('file1.pdf', 'r') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            assert len(pdf_reader.pages) == 10, "PDF file should have 10 pages."


def test_read_csv(zip_file):
    with zipfile.ZipFile('resources/archive.zip', 'r') as zip_file:
        with zip_file.open('file3.csv', 'r') as csv_file:
            count_row = 0
            for _ in csv_file:
                count_row += 1
            assert 7 == count_row


def test_read_xlsx(zip_file):
    with zipfile.ZipFile('resources/archive.zip', 'r') as zip_file:
        with zip_file.open('file2.xlsx', 'r') as xlsx_file:
            book = openpyxl.load_workbook(xlsx_file)
            sheet = book.active
            assert 'First Name' in sheet['B1'].value
            assert 'Dulce' in sheet['B2'].value
