import unittest
import time

class TestAPIResponse(unittest.TestCase):
    def test_response_time_under_threshold(self):
        """API responds under 150 ms (should PASS)."""
        simulated_response_time_ms = 120
        time.sleep(0.5)
        self.assertLessEqual(simulated_response_time_ms, 150)

    def test_status_code_ok(self):
        """API returns 200 OK (we FORCE a failure here)."""
        simulated_status_code = 503
        time.sleep(0.5)
        self.assertEqual(simulated_status_code, 200,
                         "Service returned 503 instead of 200")

if __name__ == "__main__":
    unittest.main()
