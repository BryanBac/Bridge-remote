from control.remote import Remote


class AdvancedRemote(Remote):
    def __init__(self):
        super.__init__()

    def mute(self):
        self.__device.set_volume(0)
