import random
from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
from mycroft.util.log import LOG, getLogger


__author__: 'Hotcakes Sanderson'
LOGGER = getLogger(__name__)

class Riddles(MycroftSkill):
    riddles = [
        {
            "question": "How many bricks does it take to complete a building made of bricks?",
            "answer": "The last one"
        }, {
            "question": "I have no doors but I have keys. I have no rooms but I have a space. You can enter but you can never leave. What am I?",
            "answer": "a keyboard"
        }
    ]
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('riddles.intent')
    def handle_riddles(self, message):
        riddle = random.choice(self.riddles)
        question = riddle["question"]
        answer = riddle["answer"]
        self.speak_dialog(question)

def create_skill():
    return Riddles()
