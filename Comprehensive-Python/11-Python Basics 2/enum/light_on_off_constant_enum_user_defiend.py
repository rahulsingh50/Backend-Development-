# Enums are used to define the user defined constants values

from enum import Enum


class State(Enum):
    ON = 1
    OFF = 0


state = State.ON

if state == State.ON:
    print("Lamp is On")
    print(State.ON.value)
elif state == State.OFF:
    print("Lamp is OFF")


