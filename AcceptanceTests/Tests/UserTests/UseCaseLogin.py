import unittest


class MyTestCase(unittest.TestCase):
    def test_login(self):
        self.userproxyBridge.login(True, False)


if __name__ == '__main__':
    unittest.main()
