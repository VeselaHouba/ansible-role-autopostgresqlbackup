import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nginx_file(host):
    f = host.file('/backups')
    assert f.exists


def test_creating_backup(host):
    cmd = "/usr/sbin/autopostgresqlbackup"
    bkprun = host.run(cmd)
    assert bkprun.rc == 0
    f = host.file('/backups/daily/postgres/')
    assert 'sql.gz' in f.listdir()[0]
