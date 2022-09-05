# setup for compile main with cx_freeze
#python -m Setup.py build (compile command)

import sys
import os
from cx_Freeze import setup, Executable

# example build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# base detection
base = None#means console app

#///this for gui only///#
#if sys.platform == "win32":
#    base = "Win32GUI"

# ADD Files
files = 'resize.ico'
build_exe_options = {"packages": ["os"],
                     "packages": ["art"],
                     "packages": ["glob"],
                     "packages": ["argparse"],
                     "packages": ["cv2"],
                     "packages": ["concurrent.futures"],
                     "packages": ["time"],
                     "packages": ["tqdm"],
                     "packages": ["colorama"]
                     }

# target
target = Executable(
    script='main.py',
    base=None,
    icon='resize.ico'
)
setup(
    name="ResizeFolderPics",
    version="1.0",
    description="Resize all images in folder \n ready to share in the web",
    options={"build_exe": build_exe_options},
    executables=[target],
)
