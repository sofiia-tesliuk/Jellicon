#  Created by Sofiia Tesliuk at 2020-02-01.
from tkinter import filedialog


class FileDialog:
    @staticmethod
    def select_image():
        return filedialog.askopenfile(title="Select image: ",
                                      filetypes=(("png", "*.png"),
                                                 ("jpg", "*.jpg")))

    @staticmethod
    def select_directory():
        return filedialog.askdirectory(title="Choose directory: ")
