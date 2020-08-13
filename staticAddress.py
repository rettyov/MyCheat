from option import Option
from memory_tools import MemoryTools as MemT


class StaticAddressOption(Option):

    def __init__(self, description, type_option, hot_key):
        super().__init__(description, type_option, hot_key)
        mem = MemT()
        mem.read_integer()
