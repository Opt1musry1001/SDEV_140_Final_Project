# Python GUI program that allows the user to
# translate a message to or from Morse Code.
# Author: Ryan Moore
# Last updated: 4/28/23
# SDEV_140_FinalProject.py


from breezypythongui import EasyFrame


class MainWindow(EasyFrame):
    """Main window for GUI."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, width=300, height=200, title="Morse Code Translator")

        # Label for main window.
        self.addLabel(text="Press a button to start", row=0, column=1, sticky="NSW")

        # Buttons to convert input temperature.
        self.addButton(text="Translate to Morse Code", row=1, column=0, columnspan=2, command=self.openEnglish)
        self.addButton(text="Translate from Morse Code", row=2, column=0, columnspan=2, command=self.openMorse)

    def openEnglish(self):
        print("English")
        EnglishWindow().mainloop()

    def openMorse(self):
        print("Morse code")
        MorseWindow().mainloop()


class MorseWindow(EasyFrame):
    """Window for translating from Morse Code to English."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, width=300, height=200, title="Translate from Morse Code to English")

        # Label for Morse Code window.
        self.addLabel(text="Translate from Morse Code to English!", row=0, column=1)


class EnglishWindow(EasyFrame):
    """Window for translating from English to Morse Code."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, width=300, height=200, title="Translate from English to Morse Code")

        # Label for Morse Code window.
        self.addLabel(text="Translate from English to Morse Code!", row=0, column=1)


def main():
    """Instantiates and pops up the window."""
    MainWindow().mainloop()


if __name__ == "__main__":
    main()
