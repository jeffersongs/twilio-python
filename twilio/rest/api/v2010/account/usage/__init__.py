# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.api.v2010.account.usage.record import RecordList
from twilio.rest.api.v2010.account.usage.trigger import TriggerList
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class UsageList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the UsageList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: UsageList
        :rtype: UsageList
        """
        super(UsageList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Usage.json'.format(**self._kwargs)
        
        # Components
        self._records = None
        self._triggers = None

    @property
    def records(self):
        """
        Access the records
        
        :returns: RecordList
        :rtype: RecordList
        """
        if self._records is None:
            self._records = RecordList(self._version, **self._kwargs)
        return self._records

    @property
    def triggers(self):
        """
        Access the triggers
        
        :returns: TriggerList
        :rtype: TriggerList
        """
        if self._triggers is None:
            self._triggers = TriggerList(self._version, **self._kwargs)
        return self._triggers

    def get(self):
        """
        Constructs a UsageContext
        
        :returns: UsageContext
        :rtype: UsageContext
        """
        return UsageContext(self._version, **self._kwargs)

    def __call__(self):
        """
        Constructs a UsageContext
        
        :returns: UsageContext
        :rtype: UsageContext
        """
        return UsageContext(self._version, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.UsageList>'


class UsageContext(InstanceContext):

    def __init__(self, version):
        """
        Initialize the UsageContext
        
        :param Version version
        
        :returns: UsageContext
        :rtype: UsageContext
        """
        super(UsageContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {}
        self._uri = 'None'.format(**self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.UsageContext {}>'.format(context)


class UsageInstance(InstanceResource):

    def __init__(self, version, payload, account_sid):
        """
        Initialize the UsageInstance
        
        :returns: UsageInstance
        :rtype: UsageInstance
        """
        super(UsageInstance, self).__init__(version)
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: UsageContext for this UsageInstance
        :rtype: UsageContext
        """
        if self._instance_context is None:
            self._instance_context = UsageContext(
                self._version,
            )
        return self._instance_context

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.UsageInstance {}>'.format(context)
