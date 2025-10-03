class ModelBasedReflexAgent:
    def __init__(self, demanding_temp, file_name="previous_action.txt"):
        self.demanding_temp = demanding_temp
        self.room_temp = None
        self.file_name = file_name
        self.previous_action = self.load_previous_action()

    def load_previous_action(self):
        try:
            with open(self.file_name, "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return None

    def save_previous_action(self, action):
        with open(self.file_name, "w") as f:
            f.write(action)

    def Sensor(self, temp):
        self.room_temp = temp

    def Performance(self):
        if self.room_temp < self.demanding_temp:
            action = "Heater ON"
        else:
            action = "Heater OFF"

        # Compare with stored previous action
        if action == self.previous_action:
            action = "There will be no change and maintain the previous action"
        else:
            self.previous_action = action
            self.save_previous_action(action)
        return action

    def Actuator(self):
        action = self.Performance()
        print("Temperature:", self.room_temp, "Action:", action)


# Example rooms
rooms = {
    "Class Room": 20,
    "Auditorium": 22,
    "Office": 25,
    "Common Room": 19,
    "Main Department": 22,
    "Admission Office": 22
}

agent = ModelBasedReflexAgent(22)

for room, temp in rooms.items():
    agent.Sensor(temp)
    print(room, ":", end=" ")
    agent.Actuator()
