""" Quick test Works on Windows 10 not 11"""

from pywinauto import application
from pywinauto.keyboard import send_keys


app = application.Application()
app.start("Notepad.exe")
dlg_spec = app.window()
dlg_spec.move_window(x=None, y=None, width=400, height=400, repaint=True)
app.Edit.send_keys("test")
