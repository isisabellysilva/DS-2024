from machine import Pin, I2C
import machine
import ssd1306

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

bt = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
bt0 = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

led = machine.Pin(26, machine.Pin.OUT)
led0 = machine.Pin(27 ,machine.Pin.OUT)

largura = 128
altura = 64
tela = ssd1306.SSD1306_I2C(largura, altura, i2c)

while True:
    estado = bt.value()
    if estado == 0:
        led0.value(1)
        led.value(0)
        tela.text('Humidade da', 0, 0)
        tela.text ('cozinha esta em 20%', 0, 10)
        tela.text('em 20%', 0, 20)
        tela.show()
        tela.fill(0)

    estado2 = bt0.value()
    if estado2 == 0:
        led.value(1)
        led0.value(0)
        tela.text('Temperatura do', 0, 0)
        tela.text ('quarto esta em', 0, 10)
        tela.text('23 graus', 0, 20)
        tela.show()
        tela.fill(0)
    
    
       


