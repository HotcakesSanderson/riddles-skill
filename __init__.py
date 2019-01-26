from mycroft import MycroftSkill, intent_file_handler


class Riddles(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('riddles.intent')
    def handle_riddles(self, message):
        self.speak_dialog('riddles')


def create_skill():
    return Riddles()

