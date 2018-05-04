from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class CorporateITFAQSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def addressified(self, standard_string):
        return standard_string.replace('.', ' dot ')


    @intent_handler(IntentBuilder("WifiSsid").require("wifi_ssid"))
    def handle_wifi_ssid(self, message):
        if 'wifi_ssid' not in self.settings or not self.settings['wifi_ssid']:
            self.speak_dialog("unknown")
        else:
            data = {'wifi_ssid': self.addressified(self.settings['wifi_ssid'])}
            self.speak_dialog("wifi_ssid", data)

    @intent_handler(IntentBuilder("ITManagerIntent").require("it_manager"))
    def handle_it_manager(self, message):
        if 'it_manager' not in self.settings or not self.settings['it_manager']:
            self.speak_dialog("unknown")
        else:
            data = {'it_manager': self.settings['it_manager']}
            self.speak_dialog("it_manager", data)

    @intent_handler(IntentBuilder("VpnAddressIntent").require("vpn_address"))
    def handle_vpn_address(self, message):
        if 'vpn_address' not in self.settings or not self.settings['vpn_address']:
            self.speak_dialog("unknown")
        else:
            data = {'vpn_address': self.addressified(self.settings['vpn_address'])}
            self.speak_dialog("vpn_address", data)

    @intent_handler(IntentBuilder("WebmailAddressIntent").require("webmail_address"))
    def handle_webmail_address(self, message):
        if 'webmail_address' not in self.settings or not self.settings['webmail_address']:
            self.speak_dialog("unknown")
        else:
            data = {'webmail_address': self.addressified(self.settings['webmail_address'])}
            self.speak_dialog("webmail_address", data)

    ###@intent_handler(IntentBuilder("WifiPasswordIntent").optional("corporate").require("wifi_password"))
    @intent_handler(IntentBuilder("WifiPasswordIntent").require("wifi_password"))
    def handle_wifi_password(self, message):
        if 'wifi_password' not in self.settings or not self.settings['wifi_password']:
            self.speak_dialog("unknown")
        else:
            data = {'wifi_password': self.settings['wifi_password']}
            self.speak_dialog("wifi_password", data)

    @intent_handler(IntentBuilder("IntranetWebsiteAddressIntent").require("intranet_website_address"))
    def handle_intranet_website_address(self, message):
        if 'intranet_website_address' not in self.settings or not self.settings['intranet_website_address']:
            self.speak_dialog("unknown")
        else:
            data = {'intranet_website_address': self.addressified(self.settings['intranet_website_address'])}
            self.speak_dialog("intranet_website_address", data)

    @intent_handler(IntentBuilder("KerberosDomainNameIntent").require("kerberos_domain_name"))
    def handle_kerberos_domain_name(self, message):
        if 'kerberos_domain_name' not in self.settings or not self.settings['kerberos_domain_name']:
            self.speak_dialog("unknown")
        else:
            data = {'kerberos_domain_name': addressified(self.settings['kerberos_domain_name'])}
            self.speak_dialog("kerberos_domain_name", data)

def create_skill():
    return CorporateITFAQSkill()

