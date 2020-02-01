#  Created by Sofiia Tesliuk at 2020-02-01.
import tkinter as tk

from desktop_application.file_dialog import FileDialog
from image import UnImage


class SaveIconWindow:
    def __init__(self, title, width, height, bg_color, image_filename):
        self._w = tk.Toplevel()
        self._w.title(title)
        self._w.configure(background=bg_color)
        self._w.geometry("{}x{}".format(width, height))
        self._w.minsize(width=width, height=height)

        self._image_filename = image_filename

        self._setup_window()

    def _setup_window(self):
        self._save_button = tk.Button(self._w, text="Choose directory",
                                              command=self._save_icon)
        self._save_button.pack()

        self._save_icon_error = None

    def _save_icon(self):
        directory = FileDialog.select_directory()
        if directory:
            try:
                UnImage.create_icns(directory, self._image_filename, UnImage.cut_image_name(self._image_filename))
                self._w.destroy()
            except Exception as err:
                print(err)
                self._remove_icon_error()
                self._setup_icon_error("Wrong path")
        else:
            self._remove_icon_error()
            self._setup_icon_error("Directory is not selected")

    def _setup_icon_error(self, message):
        self._save_icon_error = tk.Label(self._w, text="Error: {}.".format(message))
        self._save_icon_error.pack()

    def _remove_icon_error(self):
        if self._save_icon_error:
            self._save_icon_error.destroy()
