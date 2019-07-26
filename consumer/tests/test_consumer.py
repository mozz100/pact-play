import os
import unittest
from unittest import mock

from pact import Consumer, Provider

from main import user

PACT_HOST = "localhost"
PACT_PORT = 2345
pact = Consumer("MyConsumer").has_pact_with(
    Provider("MyProvider"), host_name=PACT_HOST, port=PACT_PORT
)


class GetUserInfoContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pact.start_service()

    @classmethod
    def tearDownClass(cls):
        pact.stop_service()

    @mock.patch.dict(os.environ, {"SERVER_HOST": PACT_HOST, "SERVER_PORT": str(PACT_PORT)})
    def test_get_user(self):
        expected = {"username": "UserA", "id": 123, "groups": ["Editors"]}

        (
            pact.given("UserA exists and is not an administrator")
            .upon_receiving("a request for UserA")
            .with_request("get", "/users/UserA.json")
            .will_respond_with(200, body=expected)
        )

        with pact:
            result = user("UserA")

        self.assertEqual(result, expected)
