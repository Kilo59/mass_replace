# mass_replace

[![PyPI version](https://badge.fury.io/py/mass-replace.svg)](https://badge.fury.io/py/mass-replace) [![PyPi](https://img.shields.io/pypi/pyversions/Django.svg)](https://pypi.org/project/mass-replace/) [![Build Status](https://travis-ci.org/Kilo59/mass_replace.svg?branch=master)](https://travis-ci.org/Kilo59/mass_replace) [![Coverage Status](https://coveralls.io/repos/github/Kilo59/mass_replace/badge.svg?branch=master)](https://coveralls.io/github/Kilo59/mass_replace?branch=master) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Use case

`mass_replace` "Walkthrough" through a specified `root_folder` and perform find and replace operations on every file of the specified type.

* If `Python 3` is installed on your system it can be run as `mass_replace.py` Python script
* Can be run as a standalone Window Executable (`.exe`)

--------------------------------------------

## ⚠️ **WARNING** ⚠️
EVERY FILE OF THE SPECIFIED TYPE NESTED UNDERNEATH THE `root_folder` WILL BE SUBJECT TO FIND AND REPLACE OPERATIONS

------------------------------------------------

## Installation and usage

### Install with pip

```
pip install mass-replace
```

### To run as a standalone `.exe`

1. Download `mass_replace_windows_executable.zip`
2. Extract zip file.
3. Set configuration settings
    - from `mass_replace/` open `config.yaml` with any text editor.
    - set `filetypes` to control which filetypes will be "operated on".
    - set `replacement_paris` to control the find and replace operations to be performed on each file.
    - set 'root_folder' to set the parent folder under which the operations will be performed.
4. Run `mass_replace.exe`
     - Double click `mass_replace.exe`
     - or run from command line/powershell ✔️

```yaml
# mass_replace config file
root_folder: C:\Users\username\Documents\docs_go_here_folder
filetypes:
  - csv
  - xml
  - txt
replacement_pairs:
  old_text1: new_text1
  old_text2: new_text2
  puff_daddy: diddy
```

### Ease of Use suggestions

To make the use of `mass_replace.exe` easier.
Create shortcuts of `mass_replace.exe` and `config.yaml` and place them somewhere easy to get to.
Do not move the actual files or the application will not work.

![image](https://user-images.githubusercontent.com/13108583/39159212-5f284ca0-4732-11e8-8014-dbedd0f349c0.png)
