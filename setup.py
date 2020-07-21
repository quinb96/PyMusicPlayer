from cx_Freeze import setup, Executable
from setuptools import find_packages

setup(name = "PyMusicPlayer",
      version = "1.0,
      description="A Python music player that was made with the Tkinter module in Python3.",
      author = "Quin Brown",
      author_email = "quinb96@protonmail.com,
      packages = find_packages(),
      platforms = "Linux", "Windows",
      executables = [Executable("PyMusicPlayer.py", icon=purphalfnote.ico, shortcutName="PyMusicPlayer", shortcutDir="DesktopFolder",)])
