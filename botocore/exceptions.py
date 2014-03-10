# Copyright (c) 2012-2013 Mitch Garnaat http://garnaat.org/
# Copyright 2012-2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


class BotoCoreError(Exception):
    """
    The base exception class for BotoCore exceptions.

    :ivar msg: The descriptive message associated with the error.
    """
    fmt = 'An unspecified error occured'

    def __init__(self, **kwargs):
        msg = self.fmt.format(**kwargs)
        Exception.__init__(self, msg)
        self.kwargs = kwargs


class DataNotFoundError(BotoCoreError):
    """
    The data associated with a particular path could not be loaded.

    :ivar path: The data path that the user attempted to load.
    """
    fmt = 'Unable to load data for: {data_path}'


class NoCredentialsError(BotoCoreError):
    """
    No credentials could be found
    """
    fmt = 'Unable to locate credentials'


class NoRegionError(BotoCoreError):
    """
    No region was specified

    :ivar env_var: The name of the environment variable to use to
        specify the default region.
    """
    fmt = 'You must specify a region or set the {env_var} environment variable.'


class UnknownSignatureVersionError(BotoCoreError):
    """
    Requested Signature Version is not known.

    :ivar signature_version: The name of the requested signature version.
    """
    fmt = 'Unknown Signature Version: {signature_version}.'


class ServiceNotInRegionError(BotoCoreError):
    """
    The service is not available in requested region.

    :ivar service_name: The name of the service.
    :ivar region_name: The name of the region.
    """
    fmt = 'Service {service_name} not available in region {region_name}'


class ProfileNotFound(BotoCoreError):
    """
    The specified configuration profile was not found in the
    configuration file.

    :ivar profile: The name of the profile the user attempted to load.
    """
    fmt = 'The config profile ({profile}) could not be found'


class ConfigParseError(BotoCoreError):
    """
    The configuration file could not be parsed.

    :ivar path: The path to the configuration file.
    """
    fmt = 'Unable to parse config file: {path}'


class ConfigNotFound(BotoCoreError):
    """
    The specified configuration file could not be found.

    :ivar path: The path to the configuration file.
    """
    fmt = 'The specified config file ({path}) could not be found.'


class MissingParametersError(BotoCoreError):
    """
    One or more required parameters were not supplied.

    :ivar object: The object that has missing parameters.
        This can be an operation or a parameter (in the
        case of inner params).  The str() of this object
        will be used so it doesn't need to implement anything
        other than str().
    :ivar missing: The names of the missing parameters.
    """
    fmt = ('The following required parameters are missing for '
           '{object_name}: {missing}')


class ValidationError(BotoCoreError):
    """
    An exception occurred validating parameters.

    Subclasses must accept a ``value`` and ``param``
    argument in their ``__init__``.

    :ivar value: The value that was being validated.
    :ivar param: The parameter that failed validation.
    :ivar type_name: The name of the underlying type.
    """
    fmt = ("Invalid value ('{value}') for param {param} "
           "of type {type_name} ")


# These exceptions subclass from ValidationError so that code
# can just 'except ValidationError' to catch any possibly validation
# error.

class UnknownKeyError(ValidationError):
    """
    Unknown key in a struct paramster.

    :ivar value: The value that was being checked.
    :ivar param: The name of the parameter.
    :ivar choices: The valid choices the value can be.
    """
    fmt = ("Unknown key '{value}' for param '{param}'.  Must be one "
           "of: {choices}")


class RangeError(ValidationError):
    """
    A parameter value was out of the valid range.

    :ivar value: The value that was being checked.
    :ivar param: The parameter that failed validation.
    :ivar min_value: The specified minimum value.
    :ivar max_value: The specified maximum value.
    """
    fmt = ('Value out of range for param {param}: '
           '{min_value} <= {value} <= {max_value}')


class UnknownParameterError(ValidationError):
    """
    Unknown top level parameter.

    :ivar name: The name of the unknown parameter.
    :ivar operation: The name of the operation.
    :ivar choices: The valid choices the parameter name can be.
    """
    fmt = ("Unknown parameter '{name}' for operation {operation}.  Must be one "
           "of: {choices}")


class UnknownServiceStyle(BotoCoreError):
    """
    Unknown style of service invocation.

    :ivar service_style: The style requested.
    """
    fmt = 'The service style ({service_style}) is not understood.'


class PaginationError(BotoCoreError):
    fmt = 'Error during pagination: {message}'


class EventNotFound(BotoCoreError):
    """
    The specified event name is unknown to the system.

    :ivar event_name: The name of the event the user attempted to use.
    """
    fmt = 'The event ({event_name}) is not known'


class ChecksumError(BotoCoreError):
    """The expected checksum did not match the calculated checksum.

    """
    fmt = ('Checksum {checksum_type} failed, expected checksum '
           '{expected_checksum} did not match calculated checksum '
           '{actual_checksum}.')


class UnseekableStreamError(BotoCoreError):
    """Need to seek a stream, but stream does not support seeking.

    """
    fmt = ('Need to rewind the stream {stream_object}, but stream '
           'is not seekable.')


class WaiterError(BotoCoreError):
    """Waiter failed to reach desired state."""
    fmt = 'Waiter {name} failed: {reason}'


class IncompleteReadError(BotoCoreError):
    """HTTP response did not return expected number of bytes."""
    fmt = ('{actual_bytes} read, but total bytes '
           'expected is {expected_bytes}.')


class InvalidExpressionError(BotoCoreError):
    """Expression is either invalid or too complex."""
    fmt = 'Invalid expression {expression}: Only dotted lookups are supported.'


class UnknownCredentialError(BotoCoreError):
    """Tried to insert before/after an unregistered credential type."""
    fmt = 'Credential named {name} not found.'
