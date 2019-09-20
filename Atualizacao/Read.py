#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from view import QuestionarioGUI


class SensorRFID:
        def __init__(self):
                reader = SimpleMFRC522()

                try:
                        id, text = reader.read()
                        print(id)
                        print(text)
                        QuestionarioGUI()
                finally:
                        GPIO.cleanup()


