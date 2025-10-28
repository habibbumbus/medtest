import unittest
import io
import json
import datetime

def run_all_tests():
    """Discover and run all tests under ./tests and summarize results."""
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)

    total = result.testsRun
    fails = len(result.failures)
    errs  = len(result.errors)
    passed = total - fails - errs

    summary = {
        "timestamp": datetime.datetime.now().isoformat(timespec='seconds'),
        "total": total,
        "passed": passed,
        "failures": fails,
        "errors": errs,
        "details": stream.getvalue()
    }

    with open("last_results.json", "w") as f:
        json.dump(summary, f, indent=2)

    return summary

if __name__ == "__main__":
    print(run_all_tests())
