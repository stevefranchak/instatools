from instatools.auth.password_credentials import PasswordCredentials
from instatools.auth.instagram_web_payload_formatter import InstagramWebPayloadFormatter

class InstagramWebCredentialsFactory(object):

    PASSWORD = 0
    FACEBOOK = 1

    @staticmethod
    def create(credential_type, *args, **kwargs):
        kwargs.update({
            'payload_formatter': InstagramWebPayloadFormatter
        })

        if credential_type == InstagramWebCredentialsFactory.PASSWORD:
            return PasswordCredentials(*args, **kwargs)
        else:
            raise ValueError('Unsupported credential type value {}'.format(credential_type));