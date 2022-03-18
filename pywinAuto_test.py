
from pywinauto import application
from pywinauto.keyboard import send_keys


app = application.Application()
app.start("Notepad.exe")
#app.print_control_identifiers()

dlg_spec = app.window()
dlg_spec.move_window(x=None, y=None, width=400, height=400, repaint=True)
#dlg_spec.print_control_identifiers()
app.Edit.send_keys("test")
