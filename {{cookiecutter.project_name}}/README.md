# {{ cookiecutter.galaxy_user }}.{{ cookiecutter.role_name }}

[![Build Status](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_name }}/actions/workflows/molecule.yml/badge.svg)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_name }}/actions/wofklows/molecule.yml)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-{{ cookiecutter.project_name }}.vim-blue.svg)](https://galaxy.ansible.com/{{ cookiecutter.galaxy_user }}/{{ cookiecutter.role_name }}/)

An [ansible role](https://galaxy.ansible.com/{{ cookiecutter.galaxy_user }}/{{ cookiecutter.role_name }}) to install and configure {{ cookiecutter.role_name }}

## Role Variables

Please refer to the [defaults file](/defaults/main.yml) for an up to date list of input parameters.

## Dependencies

By default this role does not depend on any external roles. If any such dependency is required please [add them](/meta/main.yml) according to [the documentation](http://docs.ansible.com/ansible/playbooks_roles.html#role-dependencies)

## Example Playbook

- hosts: servers
  roles:
     - role: {{ cookiecutter.galaxy_user }}.{{ cookiecutter.role_name }}
       {{ cookiecutter.role_name | replace('-', '_') }}_package_state: latest

## Testing

Please make sure your environment has [docker](https://www.docker.com) installed in order to run role validation tests. Additional python dependencies are listed in the [requirements file](https://github.com/nephelaiio/ansible-role-requirements/blob/master/requirements.txt)

Role is tested against the following distributions (docker images):

  * Ubuntu Focal
  * Ubuntu Bionic
  * Debian Buster

You can test the role directly from sources using command ` molecule test `

## License

This project is licensed under the terms of the [{{ cookiecutter.license }} License](/LICENSE)
