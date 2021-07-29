"""
Main module
"""

import requests


class Network:
    """
    Network class
    """

    def __init__(self, ip='127.0.0.1'):
        self._ip = ip

        res = requests.get('https://httpbin.org/ip')

        if res.status_code == 200:
            self._ip = res.json()['origin']

    def get_ip(self) -> str:
        """
        get_ip
        :rtype: str
        """
        return self._ip

    def print_ip(self) -> None:
        """
        print_ip
        :rtype: None
        """
        print(f"IP is {self._ip}")
