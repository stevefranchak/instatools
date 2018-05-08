import abc

class PayloadFormatter(metaclass=abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def generate(instance):
        pass
