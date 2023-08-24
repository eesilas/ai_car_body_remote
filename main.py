def L():
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, -50, SuperBit.enMotors.M2, 50)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, 50, SuperBit.enMotors.M4, -50)

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        F()
        basic.show_arrow(ArrowNames.NORTH)
    elif receivedNumber == 2:
        B()
        basic.show_arrow(ArrowNames.SOUTH)
    elif receivedNumber == 3:
        L()
        basic.show_arrow(ArrowNames.WEST)
    elif receivedNumber == 4:
        R()
        basic.show_arrow(ArrowNames.EAST)
    elif receivedNumber == 5:
        Stop()
        basic.show_icon(IconNames.SMALL_SQUARE)
    else:
        basic.show_icon(IconNames.ANGRY)
radio.on_received_number(on_received_number)

def F():
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, 50, SuperBit.enMotors.M2, 50)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, 50, SuperBit.enMotors.M4, 50)

def on_gesture_logo_up():
    radio.send_number(2)
    basic.show_arrow(ArrowNames.SOUTH)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    radio.send_number(3)
    basic.show_arrow(ArrowNames.WEST)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def B():
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, -50, SuperBit.enMotors.M2, -50)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, -50, SuperBit.enMotors.M4, -50)

def on_button_pressed_ab():
    radio.send_number(5)
    basic.show_icon(IconNames.SMALL_SQUARE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def R():
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, 50, SuperBit.enMotors.M2, -50)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, -50, SuperBit.enMotors.M4, 50)

def on_gesture_tilt_right():
    radio.send_number(4)
    basic.show_arrow(ArrowNames.EAST)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    radio.send_number(1)
    basic.show_arrow(ArrowNames.NORTH)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def Stop():
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, 0, SuperBit.enMotors.M2, 0)
    SuperBit.motor_run_dual(SuperBit.enMotors.M3, 0, SuperBit.enMotors.M4, 0)
basic.show_icon(IconNames.HEART)
radio.set_group(123)

def on_forever():
    pass
basic.forever(on_forever)
