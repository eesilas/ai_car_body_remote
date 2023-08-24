function L () {
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    -50,
    SuperBit.enMotors.M2,
    50
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    50,
    SuperBit.enMotors.M4,
    -50
    )
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        F()
        basic.showArrow(ArrowNames.North)
    } else if (receivedNumber == 2) {
        B()
        basic.showArrow(ArrowNames.South)
    } else if (receivedNumber == 3) {
        L()
        basic.showArrow(ArrowNames.West)
    } else if (receivedNumber == 4) {
        R()
        basic.showArrow(ArrowNames.East)
    } else if (receivedNumber == 5) {
        Stop()
        basic.showIcon(IconNames.SmallSquare)
    } else {
        basic.showIcon(IconNames.Angry)
    }
})
function F () {
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    50,
    SuperBit.enMotors.M2,
    50
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    50,
    SuperBit.enMotors.M4,
    50
    )
}
input.onGesture(Gesture.LogoUp, function () {
    radio.sendNumber(2)
    basic.showArrow(ArrowNames.South)
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendNumber(3)
    basic.showArrow(ArrowNames.West)
})
function B () {
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    -50,
    SuperBit.enMotors.M2,
    -50
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    -50,
    SuperBit.enMotors.M4,
    -50
    )
}
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(5)
    basic.showIcon(IconNames.SmallSquare)
})
function R () {
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    50,
    SuperBit.enMotors.M2,
    -50
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    -50,
    SuperBit.enMotors.M4,
    50
    )
}
input.onGesture(Gesture.TiltRight, function () {
    radio.sendNumber(4)
    basic.showArrow(ArrowNames.East)
})
input.onGesture(Gesture.LogoDown, function () {
    radio.sendNumber(1)
    basic.showArrow(ArrowNames.North)
})
function Stop () {
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M1,
    0,
    SuperBit.enMotors.M2,
    0
    )
    SuperBit.MotorRunDual(
    SuperBit.enMotors.M3,
    0,
    SuperBit.enMotors.M4,
    0
    )
}
basic.showIcon(IconNames.Heart)
radio.setGroup(123)
basic.forever(function () {
	
})
