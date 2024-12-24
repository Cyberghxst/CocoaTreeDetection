from windows.base_window import BaseWindow
from customtkinter import CTkLabel, CTkButton, CTk

class ErrorDialog(BaseWindow):
    '''
    Represents an error dialog window.

    Attributes:
        title (str): The title for the error dialog.
        error_message (str): The message to show in the error dialog.
    '''
    def __init__(self, title: str, error_message: str, master: CTk | None = None):
        super().__init__(
            title=title,
            width=400,
            height=70
        )

        # Assign the master window to a class attribute.
        self._master = master

        # Assign the error message to a class attribute.
        self.error_message = error_message

        # Create the label to place the error message.
        self._label = CTkLabel(
            master=self._window,
            text=self.error_message
        )

        # Create a button to close the dialog.
        self._close_button = CTkButton(
            master=self._window,
            text='Cerrar',
            fg_color='#D22B2B',
            hover_color='#D2042D',
            command=self.close
        )

    def close(self) -> None:
        '''
        Closes the error dialog.

        Arguments:
            This function is not supposed to receive any arguments.

        Returns:
            (None): This function is not supposed to return anything.
        '''
        # Quit the master window if any.
        if self._master != None:
            self._master.quit()

        # Quit the error dialog.
        self._window.quit()

    def show(self) -> None:
        '''
        Show the error dialog.

        Arguments:
            This function is not supposed to receive any arguments.

        Returns:
            (None): This function is not supposed to return anything.
        '''
        # Set the width and height for the error dialog.
        self._window.geometry(f'{self.width}x{self.height}')

        # Marking the window as no-resizable.
        self._window.resizable(False, False)

        # Set the window title.
        self._window.title(self.title)

        # Packing the label and button to the error dialog.
        self._label.pack()
        self._close_button.pack()

        # Show the error dialog.
        self._window.mainloop()
        ...

