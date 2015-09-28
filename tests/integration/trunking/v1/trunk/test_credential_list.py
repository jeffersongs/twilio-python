# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.http.response import Response


class CredentialListTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response({status}, {content}))
        
        self.twilio.trunking.v1.trunks.get(sid=None) \
                               .credentials_lists.get(sid=None).fetch()
        
        self.holodeck.assert_has_request(Request('get', 'https://trunking.twilio.com/v1/Trunks/{trunk_sid}/CredentialLists/{sid}'))
