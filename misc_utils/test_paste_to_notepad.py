"""Demo test clipboard into NotePad using Autoit lib by Rob Marchetti 2/20/2020
Test Pasting text from clipboard into NotePad
Requires:
pyperclip - Install on Windows: pip install pyperclip
pyperclip - Install on Linux/macOS: pip3 install pyperclip
pyautoit - Install on Windows: pip install -U pyautoit
AutoIt v3.3.14.5 Install on Windows:https://www.autoitscript.com/site/autoit/downloads/
"""

import autoit
import pyperclip
import time

notepad_txt = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique
 leo eget nibh maximus, eleifend efficitur sapien lacinia. Class aptent taciti sociosqu 
 ad litora torquent per conubia nostra, per inceptos himenaeos. Integer non scelerisque lacus.
 Cras dictum euismod nunc, in ullamcorper diam ultrices et. Mauris arcu eros, porta at lacinia 
 et, cursus id ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere 
 cubilia curae; Nam eget faucibus ligula. Vestibulum ante dui, maximus non viverra in, vestibulum eu mauris."""


def test_paste_to_notepad():
    """Paste text from clipboard into NotePad"""

    # open Notepad
    autoit.run("notepad.exe")
    autoit.win_wait_active("[CLASS:Notepad]", 3)
    # copy text into clipboard
    pyperclip.copy(notepad_txt)
    # paste text into notepad from clipboard
    autoit.control_send("[CLASS:Notepad]", "Edit1", pyperclip.paste())
    #ControlSend("[CLASS:Notepad; Title:Untitled - Notepad]", "", "[CLASS:Edit; INSTANCE:1]", "l")
    time.sleep(2)
    # Close notepad, this will bring up the save dialog
    autoit.win_close("[CLASS:Notepad]")
    time.sleep(2)
    # click the "Don't Save" button
    autoit.control_click("[CLASS:#32770]", "Button2")
    # notepad exits

    # Verify what was pasted matches
    assert notepad_txt == pyperclip.paste()


test_paste_to_notepad()