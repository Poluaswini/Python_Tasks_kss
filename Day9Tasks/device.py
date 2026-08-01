''' Q:Smart Home Devices (Multiple Inheritance)
A smart home device may have both WiFi connectivity and Voice control features.
Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that
inherits from both using multiple inheritance.
'''
class WiFiDevice:
    def wifi(self):
        print("WiFi Connectivity: Available")
class VoiceAssistant:
    def voice(self):
        print("Voice Control: Enabled")
class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Smart Speaker Details")
        print("Brand :", self.brand)
        print("Price :", self.price)
speaker = SmartSpeaker("Amazon", 4999)
speaker.display()
speaker.wifi()
speaker.voice()
