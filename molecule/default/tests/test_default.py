import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_swap_file(host):
    file = host.file("/swapfile")
    assert file.exists


def test_sysctl_values(host):
    assert host.sysctl("vm.swappiness") == 10
    assert host.sysctl("vm.vfs_cache_pressure") == 50
