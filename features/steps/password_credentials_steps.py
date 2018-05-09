# pylint: disable=E0611
from behave import given, when, then, step
from instatools.auth.password_credentials import PasswordCredentials
from instatools.base.credentials import Credentials
import json

# TODO: This disgusts me, but it will do for now
def parse_parameterized_scenario_value(value):
    if value == 'None':
        return None
    if value == 'TypeError':
        return TypeError
    if value == 'ValueError':
        return ValueError
    if value.startswith(('{', '[')):
        parsed_json = None
        try:
            parsed_json = json.loads(value)
        except:
            pass
        else:
            return parsed_json

    return value

@given('we have username ""')
def have_empty_username(context):
    context.username = ''

@given('we have username "{username}"')
def have_username(context, username):
    context.username = parse_parameterized_scenario_value(username)

@given('we have password ""')
def have_empty_password(context):
    context.password = ''

@given('we have password "{password}"')
def have_password(context, password):
    context.password = parse_parameterized_scenario_value(password)

@when('we create an instance of the class')
def create_credentials_instance(context):
    context.credentials = None
    context.exception = None

    try:
        context.credentials = PasswordCredentials(context.username, context.password)
    except Exception as exception:
        context.exception = exception

@then('it should have the provided username and password')
def verify_username_and_password_match(context):
    assert context.credentials.username == context.username
    assert context.credentials.password == context.password

@then('it should be of the proper type and class')
def verify_password_credentials_type(context):
    assert isinstance(context.credentials, PasswordCredentials)
    assert isinstance(context.credentials, Credentials)

@then('it should not have a payload formatter')
def verify_payload_formatter_does_not_exist(context):
    assert context.credentials.hasPayloadFormatter() is False

@then('it should raise a "{exception}" exception')
def verify_specific_exception_is_raised(context, exception):
    exception_class = parse_parameterized_scenario_value(exception)
    assert isinstance(context.exception, exception_class)