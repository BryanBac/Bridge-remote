from cliente.client import Client
from control.remote import Remote
from control.advanced_remote import AdvancedRemote
from dispositivo.radio import Radio
from dispositivo.tv import TV
from dispositivo.smartTv import SmartTV


opcion: int = 8
tiene_todo: int = 0
ctrl_opcion: int = 0
dispositivo_opcion: int = 0
usuario: Client
while opcion != 4:
    print("### Menu ###")
    print("1. Seleccione su control")
    print("2. Seleccione su dispositivo")
    print("3. Usar Control")
    print("4. Salir")
    opcion = int(input("Ingrese su opción: "))
    if opcion == 1:
        print("\n   Tipos de control")
        print("1. Control Normal")
        print("2. Control Genial")
        ctrl_opcion = int(input("Ingrese su opción: "))
        if 0 < ctrl_opcion < 3:
            tiene_todo += 1
        else:
            print("No ingresó una opción correcta, pruebe de nuevo")
    if opcion == 2:
        print("\n   Tipos de dispositivos")
        print("1. Radio")
        print("2. Tv")
        print("3. Smart-Tv")
        dispositivo_opcion = int(input("Ingrese su opción: "))
        if 0 < dispositivo_opcion < 4:
            tiene_todo += 1
            if tiene_todo == 2:
                if ctrl_opcion == 1 and dispositivo_opcion == 1:
                    usuario = Client(True, Remote(Radio))
                if ctrl_opcion == 1 and dispositivo_opcion == 2:
                    usuario = Client(True, Remote(TV))
                if ctrl_opcion == 1 and dispositivo_opcion == 3:
                    usuario = Client(True, Remote(SmartTV))
                if ctrl_opcion == 2 and dispositivo_opcion == 1:
                    usuario = Client(False, AdvancedRemote(Radio))
                if ctrl_opcion == 2 and dispositivo_opcion == 2:
                    usuario = Client(False, AdvancedRemote(TV))
                if ctrl_opcion == 2 and dispositivo_opcion == 3:
                    usuario = Client(False, AdvancedRemote(SmartTV))
        else:
            print("No ingresó una opción correcta, pruebe de nuevo")
    if opcion == 3:
        acciones: int = 0
        print("\n   Acciones")
        print("1. Encender / Apagar")
        print("2. Subir Volumen")
        print("3. Bajar Volumen")
        print("4. Subir Canal")
        print("5. Bajar Canal")
        if ctrl_opcion == 2:
            print("6. Mutear")
        acciones = int(input("Ingrese su opción: "))
        if acciones == 1:
            usuario.control.toggle_power()
        elif acciones == 2:
            usuario.control.volumen_up()
        elif acciones == 3:
            usuario.control.volumen_down()
        elif acciones == 4:
            usuario.control.channel_up()
        elif acciones == 5:
            usuario.control.channel_down()
        elif acciones == 6 and ctrl_opcion == 2:
            usuario.cotrol.mute()
    if opcion == 4:
        print("Adios")
        print("Programa realizado por Bryan Bac y Laura Mejia")
