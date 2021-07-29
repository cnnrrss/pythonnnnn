import unittest

from network import Network


class TestNetwork(unittest.TestCase):
    def setUp(self):
        self.network = Network()

    def test_network_get_ip(self):
        self.assertNotEqual(self.network.get_ip(), '127.0.0.1')

    def test_network_print_ip(self):
        self.assertIsNone(self.network.print_ip())


if __name__ == '__main__':
    unittest.main()
