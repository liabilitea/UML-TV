# Create a module to call later 

# Create class and list down attributes as stated in UML
class TV: 
    channel: int
    volume: int
    on: bool
    
# Create methds for default constructor 
    def __init__(self, channel, volume):
        self.channel = channel
        self.volume = volume

# Methods for switch
    def turn_on(self) -> None:
        self.on = True
    
    def turn_off(self) -> None:
        self.off = False
 
# Methods for channel
    def get_channel(self) -> int:
        return self.channel
    
    def set_channel(self, channel) -> None:
    # Use conditional statement for limits in channel number
        if channel >= 1 and channel <= 120:
            self.channel = channel
        else:
            print(f"Channel {channel} does not exist! Please try again.")

# Methods for volume
    def get_volume(self) -> int:
        return self.volume
    
    def set_volume(self, volume) -> None:
    # Use conditional statement for limits in channel number
        if volume >= 1 and volume <= 7:
            self.volume = volume
        else:
            print(f"Volume {volume} does not exit! Please try again.")

# Methods for channel control

# Set channel value to none first
    def channel_up(self) -> None:
    # Algorithm for adding channel value
        if self.channel + 1 <= 120:
            self.channel = self.channel + 1
        else:
            print(f"Channel {self.channel + 1} does not exist! Please try again.")

# Set channel value to none first
    def channel_down(self) -> None:
    # Algorithm for subtracting channel value
        if self.channel - 1 >= 1:
            self.channel = self.channel - 1
        else:
            print(f"Channel {self.channel - 1} does not exist! Please try again.")

# Methods for volume control

# Set volume value to none first
    def volume_up(self) -> None:
    # Algorithm for adding volume value
        if self.volume + 1 <= 7:
            self.volume = self.volume + 1
        else:
            print(f"Volume {self.volume + 1} does not exist! Please try again.")

# Set volume value to none first
    def volume_down(self) -> None:
    # Algorithm for subtracting volume value
        if self.volume + 1 >= 1:
            self.volume = self.volume - 1
        else:
            print(f"Volume {self.volume - 1} does not exist! Please try again.")
