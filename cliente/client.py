from control.remote import Remote


class Client:
    def __init__(self):
        self.control: Remote = Remote()
