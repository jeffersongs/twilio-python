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
from twilio.rest.taskrouter.v1.workspace.worker.worker_statistics import StatisticsContext
from twilio.rest.taskrouter.v1.workspace.worker.workers_statistics import StatisticsContext


class WorkerList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkerList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: Contextual workspace_sid
        
        :returns: WorkerList
        :rtype: WorkerList
        """
        super(WorkerList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workers'.format(**self._kwargs)
        
        # Components
        self._statistics = None

    def stream(self, activity_name=values.unset, activity_sid=values.unset,
               available=values.unset, friendly_name=values.unset,
               target_workers_expression=values.unset, task_queue_name=values.unset,
               task_queue_sid=values.unset, limit=None, page_size=None, **kwargs):
        """
        Streams WorkerInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str activity_name: The activity_name
        :param str activity_sid: The activity_sid
        :param str available: The available
        :param str friendly_name: The friendly_name
        :param str target_workers_expression: The target_workers_expression
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'ActivityName': activity_name,
            'ActivitySid': activity_sid,
            'Available': available,
            'FriendlyName': friendly_name,
            'TargetWorkersExpression': target_workers_expression,
            'TaskQueueName': task_queue_name,
            'TaskQueueSid': task_queue_sid,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            WorkerInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, activity_name=values.unset, activity_sid=values.unset,
             available=values.unset, friendly_name=values.unset,
             target_workers_expression=values.unset, task_queue_name=values.unset,
             task_queue_sid=values.unset, limit=None, page_size=None, **kwargs):
        """
        Reads WorkerInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str activity_name: The activity_name
        :param str activity_sid: The activity_sid
        :param str available: The available
        :param str friendly_name: The friendly_name
        :param str target_workers_expression: The target_workers_expression
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            activity_name=activity_name,
            activity_sid=activity_sid,
            available=available,
            friendly_name=friendly_name,
            target_workers_expression=target_workers_expression,
            task_queue_name=task_queue_name,
            task_queue_sid=task_queue_sid,
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, activity_name=values.unset, activity_sid=values.unset,
             available=values.unset, friendly_name=values.unset,
             target_workers_expression=values.unset, task_queue_name=values.unset,
             task_queue_sid=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        """
        Retrieve a single page of WorkerInstance records from the API.
        Request is executed immediately
        
        :param str activity_name: The activity_name
        :param str activity_sid: The activity_sid
        :param str available: The available
        :param str friendly_name: The friendly_name
        :param str target_workers_expression: The target_workers_expression
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of WorkerInstance
        :rtype: Page
        """
        params = values.of({
            'ActivityName': activity_name,
            'ActivitySid': activity_sid,
            'Available': available,
            'FriendlyName': friendly_name,
            'TargetWorkersExpression': target_workers_expression,
            'TaskQueueName': task_queue_name,
            'TaskQueueSid': task_queue_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            WorkerInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, friendly_name, activity_sid=values.unset,
               attributes=values.unset):
        """
        Create a new WorkerInstance
        
        :param str friendly_name: The friendly_name
        :param str activity_sid: The activity_sid
        :param str attributes: The attributes
        
        :returns: Newly created WorkerInstance
        :rtype: WorkerInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'ActivitySid': activity_sid,
            'Attributes': attributes,
        })
        
        return self._version.create(
            WorkerInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: StatisticsContext
        :rtype: StatisticsContext
        """
        if self._statistics is None:
            self._statistics = StatisticsContext(self._version, **self._kwargs)
        return self._statistics

    def get(self, sid):
        """
        Constructs a WorkerContext
        
        :param sid: Contextual sid
        
        :returns: WorkerContext
        :rtype: WorkerContext
        """
        return WorkerContext(self._version, sid=sid, **self._kwargs)

    def __call__(self, sid):
        """
        Constructs a WorkerContext
        
        :param sid: Contextual sid
        
        :returns: WorkerContext
        :rtype: WorkerContext
        """
        return WorkerContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerList>'


class WorkerContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        """
        Initialize the WorkerContext
        
        :param Version version
        :param workspace_sid: Contextual workspace_sid
        :param sid: Contextual sid
        
        :returns: WorkerContext
        :rtype: WorkerContext
        """
        super(WorkerContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workers/{sid}'.format(**self._kwargs)
        
        # Dependents
        self._statistics = None

    def fetch(self):
        """
        Fetch a WorkerInstance
        
        :returns: Fetched WorkerInstance
        :rtype: WorkerInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            WorkerInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, activity_sid=values.unset, attributes=values.unset,
               friendly_name=values.unset):
        """
        Update the WorkerInstance
        
        :param str activity_sid: The activity_sid
        :param str attributes: The attributes
        :param str friendly_name: The friendly_name
        
        :returns: Updated WorkerInstance
        :rtype: WorkerInstance
        """
        data = values.of({
            'ActivitySid': activity_sid,
            'Attributes': attributes,
            'FriendlyName': friendly_name,
        })
        
        return self._version.update(
            WorkerInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        """
        Deletes the WorkerInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: StatisticsContext
        :rtype: StatisticsContext
        """
        if self._statistics is None:
            self._statistics = StatisticsContext(
                self._version,
                workspace_sid=self._kwargs['workspace_sid'],
                worker_sid=self._kwargs['sid'],
            )
        return self._statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.WorkerContext {}>'.format(context)


class WorkerInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        """
        Initialize the WorkerInstance
        
        :returns: WorkerInstance
        :rtype: WorkerInstance
        """
        super(WorkerInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'activity_name': payload['activity_name'],
            'activity_sid': payload['activity_sid'],
            'attributes': payload['attributes'],
            'available': payload['available'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_status_changed': deserialize.iso8601_datetime(payload['date_status_changed']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'workspace_sid': workspace_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: WorkerContext for this WorkerInstance
        :rtype: WorkerContext
        """
        if self._instance_context is None:
            self._instance_context = WorkerContext(
                self._version,
                self._kwargs['workspace_sid'],
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def activity_name(self):
        """
        :returns: The activity_name
        :rtype: str
        """
        return self._properties['activity_name']

    @property
    def activity_sid(self):
        """
        :returns: The activity_sid
        :rtype: str
        """
        return self._properties['activity_sid']

    @property
    def attributes(self):
        """
        :returns: The attributes
        :rtype: str
        """
        return self._properties['attributes']

    @property
    def available(self):
        """
        :returns: The available
        :rtype: bool
        """
        return self._properties['available']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_status_changed(self):
        """
        :returns: The date_status_changed
        :rtype: datetime
        """
        return self._properties['date_status_changed']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: str
        """
        return self._properties['sid']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: str
        """
        return self._properties['workspace_sid']

    def fetch(self):
        """
        Fetch a WorkerInstance
        
        :returns: Fetched WorkerInstance
        :rtype: WorkerInstance
        """
        return self._context.fetch()

    def update(self, activity_sid=values.unset, attributes=values.unset,
               friendly_name=values.unset):
        """
        Update the WorkerInstance
        
        :param str activity_sid: The activity_sid
        :param str attributes: The attributes
        :param str friendly_name: The friendly_name
        
        :returns: Updated WorkerInstance
        :rtype: WorkerInstance
        """
        return self._context.update(
            activity_sid=activity_sid,
            attributes=attributes,
            friendly_name=friendly_name,
        )

    def delete(self):
        """
        Deletes the WorkerInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._context.delete()

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: statistics
        :rtype: statistics
        """
        return self._context.statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Taskrouter.V1.WorkerInstance {}>'.format(context)
