import os
import ctypes
import win32api

PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
   _fields_ = [("wVk", ctypes.c_ushort),
               ("wScan", ctypes.c_ushort),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
   _fields_ = [("uMsg", ctypes.c_ulong),
               ("wParamL", ctypes.c_short),
               ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
   _fields_ = [("dx", ctypes.c_long),
               ("dy", ctypes.c_long),
               ("mouseData", ctypes.c_ulong),
               ("dwFlags", ctypes.c_ulong),
               ("time", ctypes.c_ulong),
               ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
   _fields_ = [("ki", KeyBdInput),
               ("mi", MouseInput),
               ("hi", HardwareInput)]


class Input(ctypes.Structure):
   _fields_ = [("type", ctypes.c_ulong),
("ii", Input_I)]

def press_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
   extra = ctypes.c_ulong(0)
   ii_ = Input_I()

   flags = 0x0008 | 0x0002

   ii_.ki = KeyBdInput(0, key, flags, 0, ctypes.pointer(extra))
   x = Input(ctypes.c_ulong(1), ii_)
   ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def toggle_q_on():
    press_key(0x10) #q

def toggle_q_off():
    release_key(0x10)
    press_key(0x10)
    release_key(0x10)

def press_r():
    press_key(0x13) #r
    release_key(0x13)

def press_d():
    press_key(0x20) #d
    release_key(0x20) 

    
def press_laugh():
    press_key(0x1D)
    press_key(0x05)
    release_key(0x1D)
    release_key(0x05)
       
