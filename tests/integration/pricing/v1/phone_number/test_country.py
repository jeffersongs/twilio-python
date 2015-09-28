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


class CountryTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response({status}, {content}))
        
        self.twilio.pricing.v1.phone_numbers \
                              .countries.get(iso_country=None).fetch()
        
        self.holodeck.assert_has_request(Request('get', 'https://pricing.twilio.com/v1/PhoneNumbers/Countries/{iso_country}'))
