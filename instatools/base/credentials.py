import abc
import instatools.base.payload_formatter as payload_formatter_base

class Credentials(metaclass=abc.ABCMeta):
    
    _payload_formatter = None

    @property
    def payload_formatter(self):
        return self._payload_formatter

    @payload_formatter.setter
    def payload_formatter(self, val):
        if val is not None and not issubclass(val, payload_formatter_base.PayloadFormatter):
            raise TypeError('The payload_formatter property must be set to an instance of PayloadFormatter')
        self._payload_formatter = val

    def hasPayloadFormatter(self):
        return self.payload_formatter is not None

    def getPayload(self):
        if not self.hasPayloadFormatter():
            return None
        return self.payload_formatter.generate(self)
