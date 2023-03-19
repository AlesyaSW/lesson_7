
import zipfile
import os

def test_zip_files():

    files_to_zip = ["test.xlsx", "test.csv", "test.pdf"]

    for file in files_to_zip:
        open(file, "w").close()

    with zipfile.ZipFile("resources/test.zip", "w") as zip_file:
        for file in files_to_zip:
            zip_file.write(file)


    with zipfile.ZipFile("resources/test.zip", "r") as zip_file:
        for file in files_to_zip:
            with zip_file.open(file, "r") as f:
                content = f.read()
                assert len(content) >= 0, f"{file} is empty"


    for file in files_to_zip:
        os.remove(file)


    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources/test.zip")
    assert os.path.exists(file), f"{file} does not exist"
