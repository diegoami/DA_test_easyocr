# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import easyocr
SCRENSHOT_DIR = "/home/diego/Pictures/Screenshots"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ## loop trought all the files in the directory
    reader = easyocr.Reader(['en'])
    for filename in os.listdir(SCRENSHOT_DIR):
        if filename.endswith(".png"):
            full_file_name = os.path.join(SCRENSHOT_DIR, filename)
            result = reader.readtext(full_file_name)
            print(full_file_name)
            print(result)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
