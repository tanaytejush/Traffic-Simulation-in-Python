
import random
import time

class TrafficLight:
    def __init__(self):
        self.state = "green"
        self.time_since_change = 0

    def change_state(self):
        if self.state == "green":
            self.state = "yellow"
        elif self.state == "yellow":
            self.state = "red"
        else:
            self.state = "green"

    def update(self, time_elapsed):
        self.time_since_change += time_elapsed
        if self.time_since_change >= 60: # Change state every 60 seconds
            self.change_state()
            self.time_since_change = 0

def simulate_traffic_control_system():
    traffic_light = TrafficLight()
    while True:
        time_elapsed = random.randint(1, 5) # Simulate time elapsed between 1 and 5 seconds
        traffic_light.update(time_elapsed)
        print(f"Current state of traffic light: {traffic_light.state}")
        time.sleep(1) # Wait for 1 second before updating again

simulate_traffic_control_system()