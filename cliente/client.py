from control.advanced_remote import AdvancedRemote
from control.remote import Remote


class Client:
    def __init__(self, tipo: bool, control):
        self.control
        if tipo:
            self.cotrol: Remote = control
        else:
            self.cotrol: AdvancedRemote = control
