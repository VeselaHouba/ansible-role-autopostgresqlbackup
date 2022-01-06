# autopostgresqlbackup

Simple role to install & setup https://github.com/k0lter/autopostgresqlbackup tool

# Variables

Please check default variables in `defaults/main.yml`

## Example Playbook

```
---
- hosts: database
  become: true
  roles:
    - { name: veselahouba.autopostgresqlbackup, tags: autopostgresqlbackup }
```
