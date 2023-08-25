class ElectricSocket:
    def supply_electricity(self, voltage):
        print(f"Подача электроэнергии напряжением {voltage}")


class USPlugAdapter:
    def __init__(self, socket):
        self.socket = socket

    def supply_electricity(self, voltage):
        if voltage == 220:
            self.socket.supply_electricity(110)
        else:
            raise ValueError("Неподдерживаемое напряжение")


# Пример использования
socket = ElectricSocket()
adapter = USPlugAdapter(socket)

socket.supply_electricity(220)
adapter.supply_electricity(220)