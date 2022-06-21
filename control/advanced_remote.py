from control.remote import Remote


class AdvancedRemote(Remote):
    def __init__(self):
        super.__init__()

    def mute(self):
        raise NotImplementedError
