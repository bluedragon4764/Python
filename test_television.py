import unittest
from television import Television
class TestTelevision(unittest.TestCase):



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
    def test_power(self):
        self.test_power(True)
        self.test_power(False)

    def test_mute(self):
        self.test_mute(True)
        self.test_power(False)

    def test_channel_up(self):
        self.test_volume_up(0)
        self.test_channel_up(1)
        self.test_channel_up(2)
        self.test_channel_up(3)
    def test_channel_down(self):
        self.test_channel_down(3)
        self.test_channel_down(2)
        self.test_channel_down(1)
        self.test_channel_down(0)
    def test_volume_up(self):
        self.test_volume_up(0)
        self.test_volume_up(1)
        self.test_volume_up(2)

    def test_volume_down(self):
        self.test_volume_down(0)
        self.test_volume_down(1)
        self.test_volume_down(2)















if __name__ == '__main__':
    unittest.main()
