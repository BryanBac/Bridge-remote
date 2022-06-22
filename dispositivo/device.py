from abc import ABCMeta
from abc import abstractmethod


class Device(metaclass=ABCMeta):
    @abstractmethod
    def is_enabled(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def get_volume(self):
        raise NotImplementedError

    def set_volume(self, percent: int):
        raise NotImplementedError

    def get_channel(self):
        raise NotImplementedError

    def set_channel(self, channel: int):
        raise NotImplementedError
