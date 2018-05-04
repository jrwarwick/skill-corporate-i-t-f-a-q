from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class CorporateITFAQSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('CorporateITFAQ'))
    def handle_corporate_i_t_f_a_q(self, message):
        self.speak_dialog('corporate.i.t.f.a.q')

    @intent_handler(IntentBuilder().require('it_manager'))
    def handle_it_manager(self, message):
        data = {'it_manager': self.settings['it_manager']}
        self.speak_dialog('it_manager',data)

    @intent_handler(IntentBuilder().require('vpn_address'))
    def handle_vpn_address(self, message):
        data = {'vpn_address': self.settings['vpn_address']}
        self.speak_dialog('vpn_address',data=self.settings['vpn_address'])

    @intent_handler(IntentBuilder().require('webmail_address'))
    def handle_webmail_address(self, message):
        data = {'webmail_address': self.settings['webmail_address']}
        self.speak_dialog('webmail_address',data=self.settings['webmail_address'])

    @intent_handler(IntentBuilder().require('wifi_password'))
    def handle_wifi_password(self, message):
        data = {'wifi_password': self.settings['wifi_password']}
        self.speak_dialog('wifi_password',data=self.settings['wifi_password'])


def create_skill():
    return CorporateITFAQSkill()

