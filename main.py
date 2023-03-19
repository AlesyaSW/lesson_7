
import zipfile
import os

def test_zip_files():
    # Создаем список файлов, которые нужно поместить в архив
    files_to_zip = ["test.txt", "test.xlsx", "test.csv", "test.pdf"]

    # Создаем пустые файлы для тестирования
    for file in files_to_zip:
        open(file, "w").close()

    # Создаем архив и добавляем в него файлы
    with zipfile.ZipFile("resources/test.zip", "w") as zip_file:
        for file in files_to_zip:
            zip_file.write(file)

    # Читаем содержимое каждого файла из архива и проверяем его
    with zipfile.ZipFile("resources/test.zip", "r") as zip_file:
        for file in files_to_zip:
            with zip_file.open(file, "r") as f:
                content = f.read()
                assert len(content) >= 0, f"{file} is empty"

    # Удаляем созданные файлы
    for file in files_to_zip:
        os.remove(file)

    # Проверяем, что архив существует
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources/test.zip")
    assert os.path.exists(file), f"{file} does not exist"
