import unittest
from metrics_tracker_client import track


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(DeployEventTestCase('deploy_event_test'))
    return test_suite

###########################
#        Unit Tests       #
###########################


class DeployEventTestCase(unittest.TestCase):
    """Tests for `cf_deployment_tracker/__init__.py - track()`."""

    def deploy_event_test(self):
        """Send a sample test event to the dev deployment tracker"""

        dev_deployment_tracker_url = 'https://metrics-tracker.mybluemix.net/api/v1/track'
        self.assertTrue(track(dev_deployment_tracker_url) is None)

if __name__ == '__main__':
    unittest.main()
