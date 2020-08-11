import staticAddress as statAdr


class GameOption:
    description = ''
    type_option = ''
    hot_key = ''
    logic = 0

    def __init__(self, description, type_option, hot_key):
        self.description = description
        self.type_option = type_option
        self.hot_key = hot_key
        self.logic = GameOption.cheat_logic(type_option)

    @staticmethod
    def cheat_logic(type_option):
        if type_option == 'static address':
            return statAdr.StaticAddressOption()

