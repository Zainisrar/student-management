# from cx_Freeze import *
# import cx_Freeze
# import sys
# import os 
# includefiles=["./studentmanagement/icons.ico","./studentmanagement/logoss.jpg"]
# excludes=[]
# packages=[]
# base=None
# if sys.platform=="win32":
#     base= "Win32GUI"

# shortcut_table=[
#     ("DesktopShortcut",
#     "DestopFolder",
#     "StudentManagementSystem",
#     "TARGETDIR",
#     "[TARGETDIR]\StudentManagementSystem.exe",
#     None,
#     None,
#     None,
#     None,
#     None,
#     None,
#     "TARGETDIR",
#     )
# ]

# msi_data={"shortcut":shortcut_table}

# bdist_msi_options={"data":msi_data}
# setup(
#     version="0.1",
#     description="StudentManagementSystem by zayn malik",
#     author="zayn malik",
#     name="Student Management System",
#     options={"build_exe":{"include_files":includefiles},"bdist_msi":bdist_msi_options,},
#     executables=[
#         Executable(
#             script="login.py",
#             base=base,
#             icon=["./studentmanagement/icons.ico","./studentmanagement/logoss.jpg"]
#         )
#     ]

# )
import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base)]


cx_Freeze.setup(
    name = "Zayn Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":['tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
