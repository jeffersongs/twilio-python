# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import Domain
from twilio.rest.pricing.v1 import V1


class Pricing(Domain):

    def __init__(self, twilio):
        """
        Initialize the Pricing Domain
        
        :returns: Domain for Pricing
        :rtype: Pricing
        """
        super(Pricing, self).__init__(twilio)
        
        self.base_url = 'https://pricing.twilio.com'
        
        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of pricing
        :rtype: V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def phone_numbers(self):
        """
        :rtype: PhoneNumberList
        """
        return self.v1.phone_numbers

    @property
    def voice(self):
        """
        :rtype: VoiceList
        """
        return self.v1.voice

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing>'
