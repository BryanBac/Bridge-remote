from dispositivo.device import Device


class SmartTV(Device):
    def __init__(self):
        self.__enabled = False
        self.__volume = 0
        self.__channel = 0
        self.__aplicaciones = ["Netflix", "Disney+", "YouTube", "HboMax"]

    def is_enabled(self):
        return self.__enabled

    def enable(self):
        self.__enabled = True
        print("Esta habilitado")

    def disable(self):
        self.__enabled = False
        print("Esta deshabilitado")

    def get_volume(self):
        return self.__volume

    def set_volume(self, percent: int):
        self.__volume = percent
        print(f"Volumen: {self.__volume}")

    def get_channel(self):
        return self.__channel

    def set_channel(self, channel: int):
        self.__channel = channel
        if self.__channel >= len(self.__aplicaciones):
            self.__channel -= 1
        elif self.__channel <= -1:
            self.__channel = 0
        print(f"Aplicación: {self.__aplicaciones[self.__channel]}")
