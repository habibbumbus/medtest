import unittest
import time

class TestLogin(unittest.TestCase):
    def test_valid_login(self):
        """Simulate a valid login flow that should PASS."""
        time.sleep(0.5)
        self.assertTrue(True)

    def test_invalid_login(self):
        """Simulate an invalid login that SHOULD FAIL (defect)."""
        time.sleep(0.5)
        self.assertTrue(False, "Login accepted invalid credentials - defect")

if __name__ == "__main__":
    unittest.main()
