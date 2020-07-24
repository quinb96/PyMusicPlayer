from setuptools import setup, find_packages

setup(name="PyMusicPlayer",
      author="Quin Brown",
      author_email="quinb96@protonmail.com",
      version="1.0",
      description="A music player coded in python3 using the tkinter gui toolkit.",
      install_requires=["pygame", "ttkthemes"],
      url="https://github.com/sketchyboi14/PyMusicPlayer",
      platforms=["Linux", "Windows"],
      include_package_data=True,
      zip_safe=False,
      packeges=find_packages(),
      )