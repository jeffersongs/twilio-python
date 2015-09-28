# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class TokenList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the TokenList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: TokenList
        :rtype: TokenList
        """
        super(TokenList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Tokens.json'.format(**self._kwargs)

    def create(self, ttl=values.unset):
        """
        Create a new TokenInstance
        
        :param str ttl: The duration in seconds the credentials are valid
        
        :returns: Newly created TokenInstance
        :rtype: TokenInstance
        """
        data = values.of({
            'Ttl': ttl,
        })
        
        return self._version.create(
            TokenInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def get(self):
        """
        Constructs a TokenContext
        
        :returns: TokenContext
        :rtype: TokenContext
        """
        return TokenContext(self._version, **self._kwargs)

    def __call__(self):
        """
        Constructs a TokenContext
        
        :returns: TokenContext
        :rtype: TokenContext
        """
        return TokenContext(self._version, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TokenList>'


class TokenContext(InstanceContext):

    def __init__(self, version):
        """
        Initialize the TokenContext
        
        :param Version version
        
        :returns: TokenContext
        :rtype: TokenContext
        """
        super(TokenContext, self).__init__(version)
        
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
        return '<Twilio.Api.V2010.TokenContext {}>'.format(context)


class TokenInstance(InstanceResource):

    def __init__(self, version, payload, account_sid):
        """
        Initialize the TokenInstance
        
        :returns: TokenInstance
        :rtype: TokenInstance
        """
        super(TokenInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'ice_servers': payload['ice_servers'],
            'password': payload['password'],
            'ttl': payload['ttl'],
            'username': payload['username'],
        }
        
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
        
        :returns: TokenContext for this TokenInstance
        :rtype: TokenContext
        """
        if self._instance_context is None:
            self._instance_context = TokenContext(
                self._version,
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def ice_servers(self):
        """
        :returns: An array representing the ephemeral credentials
        :rtype: str
        """
        return self._properties['ice_servers']

    @property
    def password(self):
        """
        :returns: The temporary password used for authenticating
        :rtype: str
        """
        return self._properties['password']

    @property
    def ttl(self):
        """
        :returns: The duration in seconds the credentials are valid
        :rtype: str
        """
        return self._properties['ttl']

    @property
    def username(self):
        """
        :returns: The temporary username that uniquely identifies a Token.
        :rtype: str
        """
        return self._properties['username']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.TokenInstance {}>'.format(context)
