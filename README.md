cookiecutter-ansible-role
=========================
[![Build Status](https://travis-ci.org/nephelaiio/cookiecutter-ansible-role.svg?branch=master)](https://travis-ci.org/nephelaiio/cookiecutter-ansible-role.svg?branch=master)

A cookiecutter template for ansible role generation

Requirements
------------
Your environment must comply with the following requirements in order to successfully generate and use a new role:
  * You must be running under Linux
  * Use a python2 interpreter or virtualenv
  * Have docker installed
  * Install `cookiecutter` package. E.g. `pip install cookiecutter`.
  * Install `docker-py` package. E.g. `pip install docker-py`.

A sample procedure to meet requirements under Arch Linux is provided below:
```
sudo pacman -S python-virtualenvwrapper docker
mkvirtualenv ansible -p /usr/bin/python2
pip install cookiecutter docker-py
```

Docker images for Ubuntu, CentOS and Arch will be automatically registered on your system if required.

Usage
-----
You may use the following procedure as a guide for creating an ansible role in the current directory
```
cookiecutter gh:nephelaiio/ansible-role .
pip install -r requirements.txt
```

License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
