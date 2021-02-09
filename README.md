cookiecutter-ansible-role
=========================
[![Build Status](https://github.com/nephelaiio/cookiecutter-ansible-role/workflows/CI/badge.svg)](https://github.com/nephelaiio/cookiecutter-ansible-role/actions)

A cookiecutter template for ansible role generation

Test Requirements
-----------------
Your environment must comply with the following requirements in order to successfully test the cookiecutter
  * You must be running under Linux
  * Use a python interpreter or virtualenv
  * Have docker installed
  * Install `cookiecutter` package. E.g. `pip install cookiecutter`.
  * Install `docker-py` package. E.g. `pip install docker-py`.

A sample procedure to meet requirements under Arch Linux is provided below:
```
sudo pacman -S python-virtualenvwrapper docker
mkvirtualenv ansible -p /usr/bin/python2
pip install cookiecutter docker-py
```

Usage
-----
You may use the following procedure as a guide for creating an ansible role in the current directory
```
cookiecutter gh:nephelaiio/cookiecutter-ansible-role
```

License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
