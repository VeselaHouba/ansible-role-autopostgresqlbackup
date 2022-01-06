import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_file(host):
    f = host.file('/backups')
    assert f.exists


def test_pgpass_exists(host):
    f = host.file('/var/lib/postgresql/.pgpass')
    assert f.exists
    assert f.contains('supersecure')


def test_values_propagated(host):
    f = host.file('/etc/default/autopostgresqlbackup')
    assert f.contains('127.0.0.1')


def test_creating_backup(host):
    cmd = "/usr/sbin/autopostgresqlbackup"
    bkprun = host.run(cmd)
    assert bkprun.rc == 0
    f = host.file('/backups/daily/postgres/')
    assert 'sql.gz' in f.listdir()[0]
