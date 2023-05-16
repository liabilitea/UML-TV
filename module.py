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
    def turnOn(self) -> None:
        self.on = True
    
    def turnOff(self) -> None:
        self.off = False
 
# Methods for channel
    def getChannel(self) -> int:
        return self.channel
    
    def setChannel(self, channel) -> None:
    # Use conditional statement for limits in channel number
        if channel >= 1 and channel <= 120:
            self.channel = channel
        else:
            print(f"Channel {channel} does not exist! Please try again.")

# Methods for volume
    def getVolume(self) -> int:
        return self.volume
    
    def setVolume(self, volume) -> None:
    # Use conditional statement for limits in channel number
        if volume >= 1 and volume <= 7:
            self.volume = volume
        else:
            print(f"Volume {volume} does not exit! Please try again.")
            
# Methods for channel control 
    # Set channel value to none first
    # Algorithm for adding and subtracting channel value

# Methods for volume control
    # Set volume value to none first
    # Algorithm for adding and subtracting volume value