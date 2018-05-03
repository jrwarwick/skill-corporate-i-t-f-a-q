from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class CorporateITFAQSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('CorporateITFAQ'))
    def handle_corporate_i_t_f_a_q(self, message):
        self.speak_dialog('corporate.i.t.f.a.q')


def create_skill():
    return CorporateITFAQSkill()

