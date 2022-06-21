from dispositivo.device import Device


class TV(Device):
    def __init__(self):
        self.__enabled = False
        self.__volume = 0
        self.__channel = 0

    def is_enabled(self):
        return self.__enabled

    def enable(self):
        self.__enabled = True
        return "Esta habilitado"

    def disable(self):
        self.__enabled = False
        return "Esta deshabilitado"

    def get_volume(self):
        return self.__volume

    def set_volume(self, percent: int):
        self.__volume = percent
        print(f"Volumen: {percent}")

    def get_channel(self):
        return self.__channel

    def set_channel(self, channel: int):
        self.__channel = channel
        print(f"Canal: {self.__channel}")
