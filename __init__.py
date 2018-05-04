from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class CorporateITFAQSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder("CorporateITFAQIntent").require("CorporateITFAQ"))
    def handle_corporate_i_t_f_a_q(self, message):
        self.speak_dialog("corporate.i.t.f.a.q")

    @intent_handler(IntentBuilder("ITManagerIntent").require("it_manager"))
    def handle_it_manager(self, message):
        if 'it_manager' not in self.settings or not self.settings['it_manager']:
            self.speak_dialog("unknown")
        else:
            data = {'it_manager': self.settings['it_manager']}
            self.speak_dialog("it_manager",data)

    @intent_handler(IntentBuilder("VpnAddressIntent").require("vpn_address"))
    def handle_vpn_address(self, message):
        if 'vpn_address'not in self.settings or not self.settings['vpn_address']:
            self.speak_dialog("unknown")
        else:
            data = {'vpn_address': self.settings['vpn_address']}
            self.speak_dialog("vpn_address",data=self.settings['vpn_address'])

    @intent_handler(IntentBuilder("WebmailAddressIntent").require("webmail_address"))
    def handle_webmail_address(self, message):
        if 'webmail_address' not in self.settings or not self.settings['webmail_address']:
            self.speak_dialog("unknown")
        else:
            data = {'webmail_address': self.settings['webmail_address']}
            self.speak_dialog("webmail_address",data=self.settings['webmail_address'])

    @intent_handler(IntentBuilder("WifiPasswordIntent").optional("corporate").require("wifi_password"))
    def handle_wifi_password(self, message):
        if 'wifi_password' not in self.settings or not self.settings['wifi_password']:
            self.speak_dialog("unknown")
        else:
            data = {'wifi_password': self.settings['wifi_password']}
            self.speak_dialog("wifi_password",data=self.settings['wifi_password'])

    @intent_handler_kerberos_domain_name(IntentBuilder("KerberosDomainNameIntent").require("kerberos_domain_name"))
    def handle_(self, message):
        if 'kerberos_domain_name' not in self.settings or not self.settings['kerberos_domain_name']:
            self.speak_dialog("unknown")
        else:
            data = {'kerberos_domain_name': self.settings['kerberos_domain_name']}
            self.speak_dialog("kerberos_domain_name",data=self.settings['kerberos_domain_name'])

def create_skill():
    return CorporateITFAQSkill()

