from aiogram.fsm.state import State, StatesGroup

class PostState(StatesGroup):
    waiting_for_content = State()  # Ожидание текста/фото
    selecting_channel = State()    # Выбор канала для публикации