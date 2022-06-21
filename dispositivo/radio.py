from dispositivo.device import Device


class Radio(Device):
    __frecuencias: list[float]
    __channel: int
    __volume: int
    __enabled: bool

    def __init__(self):
        self.__enabled = False
        self.__volume = 0
        self.__channel = 0
        self.__frecuencias = [90.1, 90.3, 90.5, 90.7, 90.9, 91.0]

    def is_enabled(self) -> bool:
        return self.__enabled

    def enable(self):
        self.__enabled = True
        print("Esta habilitado")

    def disable(self):
        self.__enabled = False
        print("Esta deshabilitado")

    def get_volume(self) -> int:
        return self.__volume

    def set_volume(self, percent: int):
        self.__volume = percent
        print(f"Volumen: {percent}")

    def get_channel(self) -> float:
        return self.__frecuencias[self.__channel]

    def set_channel(self, channel: int):
        if channel < len(self.__frecuencias):
            self.__channel = channel
            print(f"Frecuencia: {self.__frecuencias[self.__channel]}")
        else:
            print("Frecuencia no válida")
