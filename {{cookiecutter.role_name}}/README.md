{{ project_slug }}
==================

{{ project_short_description }}

Role Variables
--------------

Please refer to the [defaults](defaults/main.yml) file for a list of top level role variables and their default values. Modification of distribution specific variables defined elsewhere is strongly discouraged.

Dependencies
------------

Please refer to the [dependencies](meta/main.yml) file for an up to date list of required roles

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

{{ release year }} - {{ author_full_name }} ({{ author_email }})
