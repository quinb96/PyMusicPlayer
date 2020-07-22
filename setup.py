from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pygame", "tk", "ttkthemes"]} 

setup(name = "PyMusicPlayer",
      version = "1.0",
      description="A Python music player that was made with the Tkinter module in Python3.",
      author = "Quin Brown",
      author_email = "quinb96@protonmail.com",
      executables = [Executable("PyMusicPlayer.py", icon="purphalfnote.ico", shortcutName="PyMusicPlayer", shortcutDir="DesktopFolder",)])
