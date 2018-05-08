# pylint: disable=E0611
from behave import given, when, then, step
from instatools.auth.password_credentials import PasswordCredentials
from instatools.base.credentials import Credentials

@given('we have username "{username}"')
def have_username(context, username):
    context.username = username

@given('we have password "{password}"')
def have_password(context, password):
    context.password = password

@when('we create an instance of the encapsulation')
def create_credentials_instance(context):
    context.credentials = PasswordCredentials(context.username, context.password)

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
