import time


class PowerManagerCommon(object):

    def wait_for_status(self, expected_status, tries=20, timeout=3):
        """
        Waits while the machine reaches the specified status.

        :param expected_status: status the machine should turn to
        :param tries: how many times to check status
        :param timeout: timeout in seconds before attempts
        :return: True if node moves to the specified status,
            False otherwise
        """

        _tries = 0
        while self.power_status() != expected_status and _tries < tries:
            _tries += 1
            time.sleep(timeout)

        if self.power_status() == expected_status:
            return True
        else:
            return False
