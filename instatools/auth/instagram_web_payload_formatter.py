import instatools.base.payload_formatter as payload_formatter_base
import instatools.auth.password_credentials as password_credentials

class InstagramWebPayloadFormatter(payload_formatter_base.PayloadFormatter):
    
    @staticmethod
    def generate(instance):
        payload = {}

        if isinstance(instance, password_credentials.PasswordCredentials):
            payload.update({
                'username': instance.username,
                'password': instance.password
            })
        else:
            raise TypeError('{} is not supported by InstagramWebPayloadFormatter'.format(instance.__class__.__name__))

        return payload
