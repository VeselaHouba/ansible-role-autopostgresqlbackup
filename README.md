# autopostgresqlbackup

Simple role to install & setup [autopostgresqlbackup](https://github.com/k0lter/autopostgresqlbackup) tool

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

## Notes

It's expected that `autopgbkp_user` can login to DB with no password. You can achieve this by creating a file `$HOME/.pgpass` containing a line like this

```
hostname:*:*:dbuser:dbpass
```

Role is tested with [geerlingguy.postgresql](https://github.com/geerlingguy/ansible-role-postgresql) role installed. Since it's pretty simple it should work with any standard postgresql installation.


# TODO
- test passing port with DBHOST="localhost -p 5434"
