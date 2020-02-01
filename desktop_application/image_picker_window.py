#  Created by Sofiia Tesliuk at 2020-02-01.
import tkinter as tk
from PIL import ImageTk, Image

from desktop_application.file_dialog import FileDialog
from image import UnImage

LOGO_FILENAME = 'static/logo.png'


class ImagePickerWindow:
    def __init__(self, parent, title, width, height, bg_color):
        self._parent = parent
        self._w = tk.Tk()
        self._w.title(title)
        self._w.geometry("{}x{}".format(width, height))
        self._w.minsize(width=width, height=height)
        self._w.configure(background=bg_color)

        self._setup_window()

    def run(self):
        self._w.mainloop()

    def _setup_window(self):
        self._setup_logo()
        self._setup_image_picker()
        self._image_picker_error = None

    def _setup_logo(self):
        self._logo_image = ImageTk.PhotoImage(Image.open(LOGO_FILENAME))
        self._logo = tk.Label(image=self._logo_image)
        self._logo.pack()

    def _setup_image_picker(self):
        self._image_picker_label = tk.Label(self._w, text="Select image: ")
        self._image_picker_label.pack()
        self._image_picker_button = tk.Button(self._w, text="Browse a file",
                                              command=self._select_image)
        self._image_picker_button.pack()

    def _select_image(self):
        filename = FileDialog.select_image()
        if filename:
            if UnImage.valid_format(filename.name):
                self._remove_image_error()
                self._parent.create_icon_window(filename.name)
            else:
                self._remove_image_error()
                self._setup_image_error("Invalid image format")
        else:
            self._remove_image_error()
            self._setup_image_error("Image is not selected")

    def _setup_image_error(self, message):
        self._image_picker_error = tk.Label(self._w, text="Error: {}.".format(message))
        self._image_picker_error.pack()

    def _remove_image_error(self):
        if self._image_picker_error:
            self._image_picker_error.destroy()

