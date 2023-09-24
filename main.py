# Define a function to move the servo to zero degrees when button A is pressed

def on_button_pressed_a():
    basic.show_arrow(ArrowNames.EAST)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 0)
    basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Define a function to move the servo to 180 degrees when button A is pressed

def on_button_pressed_b():
    basic.show_arrow(ArrowNames.WEST)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 180)
    basic.show_icon(IconNames.ASLEEP)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Start our program and move the motor to its starting position (0 degrees)
Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 0)
basic.show_icon(IconNames.ASLEEP)