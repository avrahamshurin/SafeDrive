import serial

class ArduinoOperator:
     def __init__(self, port):
          self.arduino = serial.Serial(port, 9600)

          # todo
          # while True:
          #      try:
          #           print(int(arduino.readline().decode("utf-8")))  # Read the newest output from the Arduino
          #      except ValueError:
          #           pass

     def get_head_wheel_distance(self):
          """
          read the distance in cm from the arduino
          :return: the distance in cm
          """
          return int(self.arduino.readline().decode("utf-8"))

     def motor_up(self):
          # todo send motor_up signal to the arduino
          pass

     def motor_down(self):
          # todo send motor_down signal to the arduino
          pass

     def alarm(self):
          # todo send alarm signal to the arduino
          pass