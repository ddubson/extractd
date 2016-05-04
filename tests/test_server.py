import unittest
from extractd.server import Server


class TestExtractd(unittest.TestCase):
    def test_server(self):
        server = Server("tests", "test2", "test3")
        self.assertEqual(server.host, 'tests')
        self.assertEqual(server.username, 'test2')
        self.assertEqual(server.password, 'test3')
