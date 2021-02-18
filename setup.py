from setuptools import setup
with open("README.md","r") as fh:
  long_description = fh.read()
setup(
  name = 'asciigraphics',
  version = '0.0.1',
  description = 'Do Pixel Graphics with ascii charecters',
  py_modules = ["asciianim"],
  package_dir = {'':'src'},
  classifiers = [
    "License :: GNU Genral public license v2 or later (GPLv2+)"
    "Operating System :: Microsoft :: Windows :: Windows 10"
  ],
  long_description = long_description,
  long_description_content_type = "text/markdown",
  install_requires = [
    "cursor~=1.3",
    "pyautogui",
  ],
  extras_require = {
    "dev": [
      "pytest>=3.7",
    ]
  },
  )
