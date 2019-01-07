Java
====


[![Build Status](https://travis-ci.org/openmicroscopy/ansible-role-java.svg)](https://travis-ci.org/openmicroscopy/ansible-role-java)
[![Ansible Role](https://img.shields.io/ansible/role/14303.svg)](https://galaxy.ansible.com/openmicroscopy/java/)

Install Java JREs and optionally JDKs.


Role Variables
--------------

Optional variables:
- `java_jre_versions`: A list of JRE versions to install, default `[1.8.0]`
- `java_jdk_install`: If `True` install JDKs corresponding to the JRE versions, default `False`


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: openmicroscopy.java }


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk

License
-------

BSD
