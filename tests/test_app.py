from streamlit.testing.v1 import AppTest
import os

pages = ["mimufs.py"]

# get all pages in the pages folder
# folder_path = "pages/"
# pages += [f for f in os.listdir(folder_path) if f.endswith(".py") and f != "__init__.py"]

for each_page in pages:
    test = AppTest(each_page, default_timeout=30)
    test.run()
    assert not test.exception
