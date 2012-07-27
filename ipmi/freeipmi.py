"""PowerManager driver using freeimpi package"""

from common import PowerManagerCommon

import utils


class FreeIPMIPowerManager(PowerManagerCommon):
    """External commands used:

ipmi-chassis-config -h 10.5.43.111 -u root -p root -c -e Chassis_Boot_Flags:Boot_Device=HARD-DRIVE
ipmi-chassis -h 10.5.43.113 -u root -p root --chassis-control=POWER-CYCLE
"""

    def __init__(self, *args, **kwargs):
        self._host = kwargs['host']
        self._username = kwargs['username']
        self._password = kwargs['password']

        self._cmd_prefix = {}
        self._cmd_prefix["config"] = \
            ('/usr/sbin/ipmi-chassis-config -h %s -u %s -p %s ' % \
                (self._host, self._username, self._password))
        self._cmd_prefix["control"] = \
            ('/usr/sbin/ipmi-chassis -h %s -u %s -p %s ' % \
                (self._host, self._username, self._password))

    def _execute(self, cmdtype, command):
        cmd = self._cmd_prefix[cmdtype] + ' '.join(command)
        return utils.execute(cmd, shell=True)

    def power_status(self):
        output, _ = self._execute("control", ["--get-chassis-status"])

        return output.split("\n")[0].split(":")[-1].strip()

    def power_on(self):
        return self._execute('control', ['--chassis-control=POWER-UP'])

    def power_off(self):
        return self._execute('control', ['--chassis-control=POWER-DOWN'])

    def reboot(self, hard=False):
        return self._execute('control', ['--chassis-control=POWER-CYCLE'])

    def set_boot_device(self, device):
        assert device in ('pxe', 'disk')
        device_map = {"pxe": "PXE", "disk": "HARD-DRIVE"}

        return self._execute("config", ["-c", "-e",
            "Chassis_Boot_Flags:Boot_Device=%s" % device_map[device]])


if __name__ == "__main__":
    import sys

    powermgr = FreeIPMIPowerManager(host='10.5.43.113', username='root',
            password='root')
    print powermgr.power_status()
    powermgr.set_boot_device(sys.argv[1])
    powermgr.reboot()
