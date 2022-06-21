from control.remote import Remote
from dispositivo.device import Device


class AdvancedRemote(Remote):
    def __init__(self, dispositivo: Device):
        self.__device = dispositivo
        super().__init__(dispositivo)

    def mute(self):
        self.__device.set_volume(0)
