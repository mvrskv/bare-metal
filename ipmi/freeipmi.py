"""PowerManager driver using freeimpi package"""

from common import PowerManagerCommon

import os


class FreeIPMIPowerManager(PowerManagerCommon):
    """
    FreeIPMI wrapper
    """

    def __init__():
        pass 
    
    def power_status(self, ipmi_host, ipmi_username, ipmi_password):
        command = " ".join("ipmi-chassis ",
                               "-h", ipmi_host,
                               "-u", ipmi_username,
                               "-p", ipmi_password,
                               "--get-chassis-status | grep 'System Power' | cut -d ':' -f2")

#===============================================================================
#    def power_on(self):
#        command = " ".join("$(ipmi-chassis ",
#                               "-h", ipmi_host,
#                               "-u", ipmi_username,
#                               "-p", ipmi_password,
#                               "--get-chassis-status | grep 'System Power' | cut -d ':' -f2)")
# 
#    def power_off(self):
#        command = " ".join("$(ipmi-chassis ",
#                               "-h", ipmi_host,
#                               "-u", ipmi_username,
#                               "-p", ipmi_password,
#                               "--get-chassis-status | grep 'System Power' | cut -d ':' -f2)")
# 
#    def reboot(self, hard=False):
#        return self._execute('control', ['--chassis-control=POWER-CYCLE'])
# 
#    def set_boot_device(self, device):
#        assert device in ('pxe', 'disk')
#        device_map = {"pxe": "PXE", "disk": "HARD-DRIVE"}
# 
#        return self._execute("config", ["-c", "-e",
#            "Chassis_Boot_Flags:Boot_Device=%s" % device_map[device]])
#===============================================================================

def chk_power():
    from etc import config
    
    pm = FreeIPMIPowerManager()
    for h in config.ipmi.bmnodes:
        print h['name'],
        pm.power_status(h['ipmi_host'], h['ipmi_username'], h['ipmi_password'])

if __name__ == "__main__":
    chk_power()
