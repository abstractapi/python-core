import unittest
import os, sys
from dotenv import load_dotenv

load_dotenv()

PHONE_VAL_API_KEY = os.getenv('PHONE_VAL_API_KEY')

from python_core import HttpEndpoint

class TestHttpEndpoint(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(TestHttpEndpoint, self).__init__(*args, **kwargs)
        self.http_endpoint = HttpEndpoint(
            "https://phonevalidation.abstractapi.com/v1/", {'lang' : 'python'}
        )

    def test_default_endpoint(self):

        endpoint = HttpEndpoint(
            endpoint_subdomain='phonevalidation',
            global_req_params={
                'lang' : 'python'
            }
        )
        self.assertEqual(endpoint.endpoint, 'https://phonevalidation.abstractapi.com/v1/')

    def test_endpoint_with_path(self):

        endpoint = HttpEndpoint(
            endpoint_subdomain='phonevalidation',
            global_req_params={
                'lang' : 'python'
            },
            path='sub-dir/'
        )
        self.assertEqual(endpoint.endpoint, 'https://phonevalidation.abstractapi.com/v1/sub-dir/')

    def test_no_config(self):

        try:
            # Some tests can change this to test with a wrong endpoint
            # make sure it's right here
            self.http_endpoint.endpoint = "https://phonevalidation.abstractapi.com/v1/"

            self.http_endpoint.get({
                "api_key" : PHONE_VAL_API_KEY,
                "phone" : "14154582468",

            })
        except Exception as e:
            self.fail(sys.exc_info())

    def test_wrong_endpoint(self):

        with self.assertRaises(Exception):
            self.http_endpoint.endpoint = "https://www.google.com"

            self.http_endpoint.get({
                "api_key" : PHONE_VAL_API_KEY,
                "phone" : "14154582468"
            })


    def test_wrong_get_param(self):

        with self.assertRaises(Exception):
            self.http_endpoint.endpoint = "https://phonevalidation.abstractapi.com/v1/"

            self.http_endpoint.get({
                "api_key" : PHONE_VAL_API_KEY,
                "not_phone" : "14154582468"
            })


if __name__ == '__main__':
    unittest.main()