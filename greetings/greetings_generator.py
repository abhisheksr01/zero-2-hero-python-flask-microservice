import time


class GreetingGenerator:
    def get_greeting(self, user_name):
        current_hour = self.get_current_hour()
        day_state = "Night"
        if (current_hour >= 4) and (current_hour < 12):
            day_state = "Morning"
        elif (current_hour >= 12) and (current_hour < 17):
            day_state = "Afternoon"
        elif (current_hour >= 17) and (current_hour < 20):
            day_state = "Evening"
        return f"Hi {user_name}, Good {day_state}."

    def get_current_hour(self):
        return int(time.strftime("%H"))
