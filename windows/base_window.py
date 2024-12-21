from dataclasses import dataclass
from customtkinter import CTk

@dataclass
class BaseWindow:
    '''
    A class that represents a base window.
    This class must be extended to add custom functionality.

    Attributes:
        title (str): The title that will be shown in the top of the window.
        width (int): The width of the window.
        height (int): The height of the window.
    '''
    title: str
    width: int
    height: int
    _window: CTk = CTk()

    def show(self):
        '''
        A function that shows the window.

        Arguments:
            This function does not take any arguments.

        Returns:
            This function is not supposed to return anything.
        '''
        pass
