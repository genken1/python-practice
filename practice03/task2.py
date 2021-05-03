class C32:
    def __init__(self):
        self.state = AState(self)

    def peek(self):
        return self.state.peek()

    def smash(self):
        return self.state.smash()

    def scan(self):
        return self.state.scan()


# Главный класс конечного автомата Мили
class MileMachineState:
    def __init__(self, root):
        self.root = root

    def peek(self):
        raise RuntimeError

    def smash(self):
        raise RuntimeError

    def scan(self):
        raise RuntimeError


# Состояние A
class AState(MileMachineState):
    def peek(self):
        self.root.state = EState(self.root)
        return 1

    def smash(self):
        self.root.state = BState(self.root)
        return 0


# Состояние B
class BState(MileMachineState):
    def scan(self):
        self.root.state = BState(self.root)
        return 3

    def peek(self):
        self.root.state = CState(self.root)
        return 2


# Состояние C
class CState(MileMachineState):
    def peek(self):
        self.root.state = FState(self.root)
        return 5

    def smash(self):
        self.root.state = DState(self.root)
        return 4


# Состояние D
class DState(MileMachineState):
    def peek(self):
        self.root.state = EState(self.root)
        return 6


# Состояние E
class EState(MileMachineState):
    def peek(self):
        self.root.state = GState(self.root)
        return 9

    def smash(self):
        self.root.state = FState(self.root)
        return 7

    def scan(self):
        self.root.state = BState(self.root)
        return 8


# Состояние F
class FState(MileMachineState):
    def smash(self):
        self.root.state = GState(self.root)
        return 10


# Состояние F
class GState(MileMachineState):
    def smash(self):
        self.root.state = HState(self.root)
        return 11


# Состояние F
class HState(MileMachineState):
    pass
