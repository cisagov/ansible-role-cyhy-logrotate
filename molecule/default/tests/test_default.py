import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["logrotate"])
def test_packages(host, pkg):
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize("file,content", [("/etc/logrotate.d/cyhy", "^/var/log/cyhy")])
def test_files(host, file, content):
    f = host.file(file)

    assert f.exists
    assert f.contains(content)
