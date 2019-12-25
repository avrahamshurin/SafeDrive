from CameraOperator import CameraOperator
from ArduinoOperator import ArduinoOperator


class SafeDriver:

    def __init__(self):
        self.camera_operator = CameraOperator()
        self.arduino_operator = ArduinoOperator(port='COM4')
        # todo: this is the time eyes closed we want to alarm (if the driver not open his eyes during this period).
        self.time_eyes_closed_threshold = 300  # in ms

        # todo: this is the time eyes closed we want to alarm (if the driver not open his eyes during this period).
        # todo update this in the initialization
        self.head_wheel_distance_threshold = 20

    def predict_sleeping(self, time_between_blinks, time_eyes_closed, head_wheel_distance):
        def calculate_fetigue(time_between_blinks):
            """
            :param time_between_blinks: time in ms
            :return: number between 0 and 1.
            """
            # todo

            return 0.5

        fetigue = calculate_fetigue(time_between_blinks)

        if time_eyes_closed * fetigue > self.time_eyes_closed_threshold:
            return True  # alarm

        if fetigue > 0.5 and head_wheel_distance < self.head_wheel_distance_threshold:
            return True  # alarm

        return False

    def alarm(self):
        self.arduino_operator.alarm()
        print('***ALARM***')

    def main(self):
        while True:
            time_between_blinks = self.camera_operator.get_time_between_blinks()
            time_eyes_closed = self.camera_operator.get_time_eyes_closed()
            head_wheel_distance = self.arduino_operator.get_head_wheel_distance()
            print(head_wheel_distance)

            if self.predict_sleeping(time_between_blinks, time_eyes_closed, head_wheel_distance):
                self.alarm()


if __name__ == "__main__":
    SafeDriver().main()