# Import the TV module
import TV_module

# Instantiate TV object from the TV_module.py

# Create tv1
tv1 = TV_module.TV()
tv1.set_channel(30)
tv1.set_volume(3)

# Create tv2
tv2 = TV_module.TV()
tv2.set_channel(3)
tv2.set_volume(2)

# Print

print(f"tv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume()}")
print(f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume()}")
