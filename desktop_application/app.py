#  Created by Sofiia Tesliuk at 2020-02-01.
from desktop_application.image_picker_window import ImagePickerWindow
from desktop_application.save_icon_window import SaveIconWindow


class UnIconApp:
    WINDOW_TITLE = "UnIcon"
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 300
    BG_COLOR = "white"

    def __init__(self):
        self._p_window = ImagePickerWindow(self,
                                           self.WINDOW_TITLE,
                                           self.WINDOW_WIDTH,
                                           self.WINDOW_HEIGHT,
                                           self.BG_COLOR)

        self._ic_window = None

    def run(self):
        self._p_window.run()

    def create_icon_window(self, image_filename):
        self._ic_window = SaveIconWindow(self.WINDOW_TITLE,
                                         self.WINDOW_WIDTH,
                                         self.WINDOW_HEIGHT,
                                         self.BG_COLOR,
                                         image_filename)


if __name__ == "__main__":
    app = UnIconApp()
    app.run()

