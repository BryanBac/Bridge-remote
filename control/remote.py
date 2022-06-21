from dispositivo.device import Device


class Remote:
    def __init__(self, dispositivo: Device):
        self.__device: Device = dispositivo
        # eso de arriba cambiará una vez tenga lo de laura

    def toggle_power(self):
        if self.__device.is_enabled():
            self.__device.disable()
        else:
            self.__device.enable()

    def volumen_down(self):
        bajar: int = self.__device.get_volume() - 1
        self.__device.set_volume(bajar)

    def volumen_up(self):
        subir: int = self.__device.get_volume() + 1
        self.__device.set_volume(subir)

    def channel_down(self):
        bajar_canal = self.__device.get_channel() - 1
        self.__device.set_channel(bajar_canal)

    def channel_up(self):
        subir_canal = self.__device.get_channel() + 1
        self.__device.set_channel(subir_canal)
