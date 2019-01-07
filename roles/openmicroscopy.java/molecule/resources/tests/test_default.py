import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_jre_version(host):
    assert host.exists('java')
    c = host.run('java -version')
    assert c.rc == 0
    assert c.stderr.startswith('openjdk version "1.8.0')


def test_jdk_version(host):
    if host.backend.get_hostname() == 'java-jdk':
        assert host.exists('javac')
        c = host.run('javac -version')
        assert c.rc == 0
        assert c.stderr.startswith('javac 1.8.0')
    else:
        assert not host.exists('javac')
