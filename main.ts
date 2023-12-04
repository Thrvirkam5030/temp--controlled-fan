let Temp = 0
OLED.init(64, 128)
basic.forever(function () {
    Temp = smarthome.ReadTemperature(TMP36Type.TMP36_temperature_C, AnalogPin.P2)
    OLED.clear()
    OLED.writeString("Temperature: ")
    OLED.writeNum(Temp)
    if (Temp >= 24) {
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
})
