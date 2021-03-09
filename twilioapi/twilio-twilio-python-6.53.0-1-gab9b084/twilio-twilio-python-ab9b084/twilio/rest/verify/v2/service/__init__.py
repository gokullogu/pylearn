# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.verify.v2.service.access_token import AccessTokenList
from twilio.rest.verify.v2.service.entity import EntityList
from twilio.rest.verify.v2.service.messaging_configuration import MessagingConfigurationList
from twilio.rest.verify.v2.service.rate_limit import RateLimitList
from twilio.rest.verify.v2.service.verification import VerificationList
from twilio.rest.verify.v2.service.verification_check import VerificationCheckList
from twilio.rest.verify.v2.service.webhook import WebhookList


class ServiceList(ListResource):

    def __init__(self, version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.verify.v2.service.ServiceList
        :rtype: twilio.rest.verify.v2.service.ServiceList
        """
        super(ServiceList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Services'.format(**self._solution)

    def create(self, friendly_name, code_length=values.unset,
               lookup_enabled=values.unset, skip_sms_to_landlines=values.unset,
               dtmf_input_required=values.unset, tts_name=values.unset,
               psd2_enabled=values.unset, do_not_share_warning_enabled=values.unset,
               custom_code_enabled=values.unset, push_include_date=values.unset,
               push_apn_credential_sid=values.unset,
               push_fcm_credential_sid=values.unset):
        """
        Create the ServiceInstance

        :param unicode friendly_name: A string to describe the verification service
        :param unicode code_length: The length of the verification code to generate
        :param bool lookup_enabled: Whether to perform a lookup with each verification
        :param bool skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines
        :param bool dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone call
        :param unicode tts_name: The name of an alternative text-to-speech service to use in phone calls
        :param bool psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification
        :param bool do_not_share_warning_enabled: Whether to add a security warning at the end of an SMS.
        :param bool custom_code_enabled: Whether to allow sending verifications with a custom code.
        :param bool push_include_date: Optional. Include the date in the Challenge's reponse. Default: true
        :param unicode push_apn_credential_sid: Optional. Set APN Credential for this service.
        :param unicode push_fcm_credential_sid: Optional. Set FCM Credential for this service.

        :returns: The created ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'CodeLength': code_length,
            'LookupEnabled': lookup_enabled,
            'SkipSmsToLandlines': skip_sms_to_landlines,
            'DtmfInputRequired': dtmf_input_required,
            'TtsName': tts_name,
            'Psd2Enabled': psd2_enabled,
            'DoNotShareWarningEnabled': do_not_share_warning_enabled,
            'CustomCodeEnabled': custom_code_enabled,
            'Push.IncludeDate': push_include_date,
            'Push.ApnCredentialSid': push_apn_credential_sid,
            'Push.FcmCredentialSid': push_fcm_credential_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return ServiceInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.ServiceInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServicePage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ServicePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ServiceContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.verify.v2.service.ServiceContext
        :rtype: twilio.rest.verify.v2.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ServiceContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.verify.v2.service.ServiceContext
        :rtype: twilio.rest.verify.v2.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.ServiceList>'


class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.service.ServicePage
        :rtype: twilio.rest.verify.v2.service.ServicePage
        """
        super(ServicePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.ServicePage>'


class ServiceContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.verify.v2.service.ServiceContext
        :rtype: twilio.rest.verify.v2.service.ServiceContext
        """
        super(ServiceContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Services/{sid}'.format(**self._solution)

        # Dependents
        self._verifications = None
        self._verification_checks = None
        self._rate_limits = None
        self._messaging_configurations = None
        self._entities = None
        self._webhooks = None
        self._access_tokens = None

    def fetch(self):
        """
        Fetch the ServiceInstance

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the ServiceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def update(self, friendly_name=values.unset, code_length=values.unset,
               lookup_enabled=values.unset, skip_sms_to_landlines=values.unset,
               dtmf_input_required=values.unset, tts_name=values.unset,
               psd2_enabled=values.unset, do_not_share_warning_enabled=values.unset,
               custom_code_enabled=values.unset, push_include_date=values.unset,
               push_apn_credential_sid=values.unset,
               push_fcm_credential_sid=values.unset):
        """
        Update the ServiceInstance

        :param unicode friendly_name: A string to describe the verification service
        :param unicode code_length: The length of the verification code to generate
        :param bool lookup_enabled: Whether to perform a lookup with each verification
        :param bool skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines
        :param bool dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone call
        :param unicode tts_name: The name of an alternative text-to-speech service to use in phone calls
        :param bool psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification
        :param bool do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS.
        :param bool custom_code_enabled: Whether to allow sending verifications with a custom code.
        :param bool push_include_date: Optional. Include the date in the Challenge's reponse. Default: true
        :param unicode push_apn_credential_sid: Optional. Set APN Credential for this service.
        :param unicode push_fcm_credential_sid: Optional. Set FCM Credential for this service.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'CodeLength': code_length,
            'LookupEnabled': lookup_enabled,
            'SkipSmsToLandlines': skip_sms_to_landlines,
            'DtmfInputRequired': dtmf_input_required,
            'TtsName': tts_name,
            'Psd2Enabled': psd2_enabled,
            'DoNotShareWarningEnabled': do_not_share_warning_enabled,
            'CustomCodeEnabled': custom_code_enabled,
            'Push.IncludeDate': push_include_date,
            'Push.ApnCredentialSid': push_apn_credential_sid,
            'Push.FcmCredentialSid': push_fcm_credential_sid,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def verifications(self):
        """
        Access the verifications

        :returns: twilio.rest.verify.v2.service.verification.VerificationList
        :rtype: twilio.rest.verify.v2.service.verification.VerificationList
        """
        if self._verifications is None:
            self._verifications = VerificationList(self._version, service_sid=self._solution['sid'], )
        return self._verifications

    @property
    def verification_checks(self):
        """
        Access the verification_checks

        :returns: twilio.rest.verify.v2.service.verification_check.VerificationCheckList
        :rtype: twilio.rest.verify.v2.service.verification_check.VerificationCheckList
        """
        if self._verification_checks is None:
            self._verification_checks = VerificationCheckList(self._version, service_sid=self._solution['sid'], )
        return self._verification_checks

    @property
    def rate_limits(self):
        """
        Access the rate_limits

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitList
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitList
        """
        if self._rate_limits is None:
            self._rate_limits = RateLimitList(self._version, service_sid=self._solution['sid'], )
        return self._rate_limits

    @property
    def messaging_configurations(self):
        """
        Access the messaging_configurations

        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationList
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationList
        """
        if self._messaging_configurations is None:
            self._messaging_configurations = MessagingConfigurationList(
                self._version,
                service_sid=self._solution['sid'],
            )
        return self._messaging_configurations

    @property
    def entities(self):
        """
        Access the entities

        :returns: twilio.rest.verify.v2.service.entity.EntityList
        :rtype: twilio.rest.verify.v2.service.entity.EntityList
        """
        if self._entities is None:
            self._entities = EntityList(self._version, service_sid=self._solution['sid'], )
        return self._entities

    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.verify.v2.service.webhook.WebhookList
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookList
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(self._version, service_sid=self._solution['sid'], )
        return self._webhooks

    @property
    def access_tokens(self):
        """
        Access the access_tokens

        :returns: twilio.rest.verify.v2.service.access_token.AccessTokenList
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenList
        """
        if self._access_tokens is None:
            self._access_tokens = AccessTokenList(self._version, service_sid=self._solution['sid'], )
        return self._access_tokens

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.ServiceContext {}>'.format(context)


class ServiceInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the ServiceInstance

        :returns: twilio.rest.verify.v2.service.ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        super(ServiceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'code_length': deserialize.integer(payload.get('code_length')),
            'lookup_enabled': payload.get('lookup_enabled'),
            'psd2_enabled': payload.get('psd2_enabled'),
            'skip_sms_to_landlines': payload.get('skip_sms_to_landlines'),
            'dtmf_input_required': payload.get('dtmf_input_required'),
            'tts_name': payload.get('tts_name'),
            'do_not_share_warning_enabled': payload.get('do_not_share_warning_enabled'),
            'custom_code_enabled': payload.get('custom_code_enabled'),
            'push': payload.get('push'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the verification service
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def code_length(self):
        """
        :returns: The length of the verification code
        :rtype: unicode
        """
        return self._properties['code_length']

    @property
    def lookup_enabled(self):
        """
        :returns: Whether to perform a lookup with each verification
        :rtype: bool
        """
        return self._properties['lookup_enabled']

    @property
    def psd2_enabled(self):
        """
        :returns: Whether to pass PSD2 transaction parameters when starting a verification
        :rtype: bool
        """
        return self._properties['psd2_enabled']

    @property
    def skip_sms_to_landlines(self):
        """
        :returns: Whether to skip sending SMS verifications to landlines
        :rtype: bool
        """
        return self._properties['skip_sms_to_landlines']

    @property
    def dtmf_input_required(self):
        """
        :returns: Whether to ask the user to press a number before delivering the verify code in a phone call
        :rtype: bool
        """
        return self._properties['dtmf_input_required']

    @property
    def tts_name(self):
        """
        :returns: The name of an alternative text-to-speech service to use in phone calls
        :rtype: unicode
        """
        return self._properties['tts_name']

    @property
    def do_not_share_warning_enabled(self):
        """
        :returns: Whether to add a security warning at the end of an SMS.
        :rtype: bool
        """
        return self._properties['do_not_share_warning_enabled']

    @property
    def custom_code_enabled(self):
        """
        :returns: Whether to allow sending verifications with a custom code.
        :rtype: bool
        """
        return self._properties['custom_code_enabled']

    @property
    def push(self):
        """
        :returns: The service level configuration of factor push type.
        :rtype: dict
        """
        return self._properties['push']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The URLs of related resources
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the ServiceInstance

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the ServiceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name=values.unset, code_length=values.unset,
               lookup_enabled=values.unset, skip_sms_to_landlines=values.unset,
               dtmf_input_required=values.unset, tts_name=values.unset,
               psd2_enabled=values.unset, do_not_share_warning_enabled=values.unset,
               custom_code_enabled=values.unset, push_include_date=values.unset,
               push_apn_credential_sid=values.unset,
               push_fcm_credential_sid=values.unset):
        """
        Update the ServiceInstance

        :param unicode friendly_name: A string to describe the verification service
        :param unicode code_length: The length of the verification code to generate
        :param bool lookup_enabled: Whether to perform a lookup with each verification
        :param bool skip_sms_to_landlines: Whether to skip sending SMS verifications to landlines
        :param bool dtmf_input_required: Whether to ask the user to press a number before delivering the verify code in a phone call
        :param unicode tts_name: The name of an alternative text-to-speech service to use in phone calls
        :param bool psd2_enabled: Whether to pass PSD2 transaction parameters when starting a verification
        :param bool do_not_share_warning_enabled: Whether to add a privacy warning at the end of an SMS.
        :param bool custom_code_enabled: Whether to allow sending verifications with a custom code.
        :param bool push_include_date: Optional. Include the date in the Challenge's reponse. Default: true
        :param unicode push_apn_credential_sid: Optional. Set APN Credential for this service.
        :param unicode push_fcm_credential_sid: Optional. Set FCM Credential for this service.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.verify.v2.service.ServiceInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            code_length=code_length,
            lookup_enabled=lookup_enabled,
            skip_sms_to_landlines=skip_sms_to_landlines,
            dtmf_input_required=dtmf_input_required,
            tts_name=tts_name,
            psd2_enabled=psd2_enabled,
            do_not_share_warning_enabled=do_not_share_warning_enabled,
            custom_code_enabled=custom_code_enabled,
            push_include_date=push_include_date,
            push_apn_credential_sid=push_apn_credential_sid,
            push_fcm_credential_sid=push_fcm_credential_sid,
        )

    @property
    def verifications(self):
        """
        Access the verifications

        :returns: twilio.rest.verify.v2.service.verification.VerificationList
        :rtype: twilio.rest.verify.v2.service.verification.VerificationList
        """
        return self._proxy.verifications

    @property
    def verification_checks(self):
        """
        Access the verification_checks

        :returns: twilio.rest.verify.v2.service.verification_check.VerificationCheckList
        :rtype: twilio.rest.verify.v2.service.verification_check.VerificationCheckList
        """
        return self._proxy.verification_checks

    @property
    def rate_limits(self):
        """
        Access the rate_limits

        :returns: twilio.rest.verify.v2.service.rate_limit.RateLimitList
        :rtype: twilio.rest.verify.v2.service.rate_limit.RateLimitList
        """
        return self._proxy.rate_limits

    @property
    def messaging_configurations(self):
        """
        Access the messaging_configurations

        :returns: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationList
        :rtype: twilio.rest.verify.v2.service.messaging_configuration.MessagingConfigurationList
        """
        return self._proxy.messaging_configurations

    @property
    def entities(self):
        """
        Access the entities

        :returns: twilio.rest.verify.v2.service.entity.EntityList
        :rtype: twilio.rest.verify.v2.service.entity.EntityList
        """
        return self._proxy.entities

    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.verify.v2.service.webhook.WebhookList
        :rtype: twilio.rest.verify.v2.service.webhook.WebhookList
        """
        return self._proxy.webhooks

    @property
    def access_tokens(self):
        """
        Access the access_tokens

        :returns: twilio.rest.verify.v2.service.access_token.AccessTokenList
        :rtype: twilio.rest.verify.v2.service.access_token.AccessTokenList
        """
        return self._proxy.access_tokens

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.ServiceInstance {}>'.format(context)
