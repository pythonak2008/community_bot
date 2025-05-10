from aiogram.fsm.state import State, StatesGroup

class ExampleState(StatesGroup):
    full_name = State()
    last_name = State()
    age = State()
    phone_number = State()
    state = State()
    back = State()
    next = State()
    asas = State()
