from testinfra.utils.ansible_runner import AnsibleRunner
import pytest

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


@pytest.mark.parametrize('name', ['systemd-resolved', 'systemd-networkd'])
def test_networkd_service(Service, name):
    assert Service(name).is_enabled
    assert Service(name).is_running


def test_networkctl(Command, Sudo):
    with Sudo():
        assert Command('networkctl').rc == 0
