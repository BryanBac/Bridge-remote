class Remote:
    def __init__(self, dispositivo: str):
        self.__device: str = dispositivo
        # eso de arriba cambiará una vez tenga lo de laura

    def toggle_power(self):
        raise NotImplementedError

    def volumen_down(self):
        raise NotImplementedError

    def volumen_up(self):
        raise NotImplementedError

    def channel_down(self):
        raise NotImplementedError

    def channel_up(self):
        raise NotImplementedError
