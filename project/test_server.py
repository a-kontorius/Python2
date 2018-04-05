import server
import unittest

class TestConvertFunction(unittest.TestCase):
    def test_cel_to_far_convert(self):
        r = server.cel_to_far_convert({"min": 10, "max": 20, "step": 3})
        self.assertEqual(r, {10: 50.0, 13: 55.4, 16: 60.8, 19: 66.2})

if __name__ == "__main__":
    unittest.main()