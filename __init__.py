from mycroft import MycroftSkill, intent_file_handler


class ExistentialCrisis(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('crisis.existential.intent')
    def handle_crisis_existential(self, message):
        self.speak_dialog('crisis.existential')


def create_skill():
    return ExistentialCrisis()

