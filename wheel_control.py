from krpc import *
from tools import *

#wrapper class for controlling wheels

class Rotatron_Wrapper:
    def __init__(self, wheel_object) -> None:
        self.wheel = wheel_object
        self.motor_module = module_with_name(wheel_object, "ModuleIRServo_v3")
        if self.motor_module is None:
            raise "No motor module found in part. Not a motorized wheel?"

    def activate_motor(self, on:bool = True):
        motor_on = self.motor_module.fields["Motor"]
        if motor_on != on:
            self.toggle_motor()

    def toggle_motor(self):
        self.motor_module.set_action('Toggle Motor',True) #True apparently does nothing
    
    def set_speed(self, speed:float):
        self.motor_module.set_field_float('Motor', 1.0)
