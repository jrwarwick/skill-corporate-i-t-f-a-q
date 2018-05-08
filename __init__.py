from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class CorporateITFAQSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def addressified(self, standard_string):
        return standard_string.replace('.', ' dot ')


    @intent_handler(IntentBuilder("EmailAttachmentSizeLimit").optionally("corporate").require("email_attach_size_limit"))
    def handle_email_attach_size_limit(self, message):
        if 'email_attach_size_limit' not in self.settings or not self.settings['email_attach_size_limit']:
            self.speak_dialog("unknown")
        else:
            data = {'email_attach_size_limit': self.addressified(self.settings['email_attach_size_limit'])}
            self.speak_dialog("email_attach_size_limit", data)

    @intent_handler(IntentBuilder("WifiSsid").optionally("corporate").require("wifi_ssid"))
    def handle_wifi_ssid(self, message):
        if 'wifi_ssid' not in self.settings or not self.settings['wifi_ssid']:
            self.speak_dialog("unknown")
        else:
            data = {'wifi_ssid': self.addressified(self.settings['wifi_ssid'])}
            self.speak_dialog("wifi_ssid", data)

    @intent_handler(IntentBuilder("ITManagerIntent").optionally("corporate").require("it_manager"))
    def handle_it_manager(self, message):
        if 'it_manager' not in self.settings or not self.settings['it_manager']:
            self.speak_dialog("unknown")
        else:
            data = {'it_manager': self.settings['it_manager']}
            self.speak_dialog("it_manager", data)

    @intent_handler(IntentBuilder("VpnAddressIntent").optionally("corporate").require("vpn_address"))
    def handle_vpn_address(self, message):
        if 'vpn_address' not in self.settings or not self.settings['vpn_address']:
            self.speak_dialog("unknown")
        else:
            data = {'vpn_address': self.addressified(self.settings['vpn_address'])}
            self.speak_dialog("vpn_address", data)

    @intent_handler(IntentBuilder("WebmailAddressIntent").optionally("corporate").require("webmail_address"))
    def handle_webmail_address(self, message):
        if 'webmail_address' not in self.settings or not self.settings['webmail_address']:
            self.speak_dialog("unknown")
        else:
            data = {'webmail_address': self.addressified(self.settings['webmail_address'])}
            self.speak_dialog("webmail_address", data)

    @intent_handler(IntentBuilder("WifiPasswordIntent").optionally("corporate").require("wifi_password"))
    ###@intent_handler(IntentBuilder("WifiPasswordIntent").require("wifi_password"))
    def handle_wifi_password(self, message):
        if 'wifi_password' not in self.settings or not self.settings['wifi_password']:
            self.speak_dialog("unknown")
        else:
            data = {'wifi_password': self.settings['wifi_password']}
            self.speak_dialog("wifi_password", data)

    @intent_handler(IntentBuilder("IntranetWebsiteAddressIntent").optionally("corporate").require("intranet_website_address"))
    def handle_intranet_website_address(self, message):
        if 'intranet_website_address' not in self.settings or not self.settings['intranet_website_address']:
            self.speak_dialog("unknown")
        else:
            data = {'intranet_website_address': self.addressified(self.settings['intranet_website_address'])}
            self.speak_dialog("intranet_website_address", data)

    @intent_handler(IntentBuilder("KerberosDomainNameIntent").optionally("corporate").require("kerberos_domain_name"))
    def handle_kerberos_domain_name(self, message):
        if 'kerberos_domain_name' not in self.settings or not self.settings['kerberos_domain_name']:
            self.speak_dialog("unknown")
        else:
            data = {'kerberos_domain_name': self.addressified(self.settings['kerberos_domain_name'])}
            self.speak_dialog("kerberos_domain_name", data)

def create_skill():
    return CorporateITFAQSkill()

