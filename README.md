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

## Passwordless login

It's expected that `autopgbkp_user` can login to DB with no password. This is true in most of default setups, as postgres enables connections using socket without password.

But if this is not your case, this role can manage pgpass for you. All you need to do is set

```
autopgbkp_pass: <YOUR_PASSWORD>
```

## Compatibility

This Role is tested together with [geerlingguy.postgresql](https://github.com/geerlingguy/ansible-role-postgresql) role. But since it's pretty simple it should work with any standard postgresql installation.
