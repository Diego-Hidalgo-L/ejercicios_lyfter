
class BatteryDevice:
    def __init__(self, battery):
        if battery < 0 or battery > 100:
            print("The battery level must be between 0% and 100%.")
        else:
            self.battery = battery
    
    def status(self):
        return f"Battery at {self.battery}%."


class MusicMixin:
    current_song = None

    def play_song(self, song):
        self.current_song = song
        return f"Playing {self.curent_song}."
    
    def status(self):
        if self.current_song:
            return f"Music: {self.current_song}"
        else:
            return "Music: stopped."

class GPSMixin:
    destination = None
    
    def navigate_to(self, location):
        self.destination = location
        return f"Navigating to {self.destination}."
    
    def status(self):
        if self.destination:
            return f"GPS: heading to {self.destination}."
        else:
            return "GPS: idle."

class SmartDevice(BatteryDevice, MusicMixin, GPSMixin):
    def __init__(self, battery):
        super().__init__(battery) # super().__init__() calls BatteryDevice because it is next in MRO.

    def status(self):
        return f"{BatteryDevice.status(self)} - {MusicMixin.status(self)} - {GPSMixin.status(self)}."



my_iphone = SmartDevice(76)

# print(my_iphone.play_song("Broadview"))

print(my_iphone.navigate_to("Newport"))

print(my_iphone.status())