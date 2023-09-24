// Define a function to move the servo to zero degrees when button A is pressed
input.onButtonPressed(Button.A, function () {
    basic.showArrow(ArrowNames.East)
    Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo2, 0)
    basic.showIcon(IconNames.Asleep)
})
// Define a function to move the servo to 180 degrees when button A is pressed
input.onButtonPressed(Button.B, function () {
    basic.showArrow(ArrowNames.West)
    Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo2, 180)
    basic.showIcon(IconNames.Asleep)
})
// Start our program and move the motor to its starting position (0 degrees)
Kitronik_Robotics_Board.servoWrite(Kitronik_Robotics_Board.Servos.Servo2, 0)
basic.showIcon(IconNames.Asleep)
