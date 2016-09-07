Role Name
=========

A brief description of the role goes here.

Requirements
------------

Please make sure your environment has [docker](https://www.docker.com) installed to run role validation tests

Role Variables
--------------

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.
An additional list of reserved parameters is available in the [commons file](/defaults/reserved.yml); overriding these is strongly discouraged.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: {{ cookiecutter.role_name }} {{ cookiecutter.role_name }}_packages: {{ cookiecutter.role_name }} }

License
-------

This project is licensed under the terms of the [{{ cookiecutter.license }} License](/LICENSE)
