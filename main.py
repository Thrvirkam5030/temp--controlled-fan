Temp = 0
OLED.init(64, 128)

def on_forever():
    global Temp
    Temp = smarthome.read_temperature(TMP36Type.TMP36_TEMPERATURE_C, AnalogPin.P2)
    OLED.clear()
    OLED.write_string("Temperature: ")
    OLED.write_num(Temp)
    if Temp >= 24:
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
