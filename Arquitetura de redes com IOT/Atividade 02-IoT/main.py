import machine 
import time 
import ssd1306

# Botões de controle
bt_vermelho = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
bt_verde = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP) 

# Botões de navegação
bt_cima = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
bt_baixo = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP) 

# LED
led_desligado = machine.Pin(17, machine.Pin.OUT)
led_ligado = machine.Pin(18, machine.Pin.OUT)

# Tela
largura = 128
altura = 64
i2c = machine.I2C(0, scl = machine.Pin(22), sda = machine.Pin(21))
tela = ssd1306.SSD1306_I2C(largura, altura, i2c)

qual_tela = 1
status_iluminacao = "OFF"
status_ar_condicionado = "OFF"
status_portao_principal = "OFF"
status_cameras = "OFF"
while True:

  if bt_cima.value() == 0 and qual_tela <= 4:
    qual_tela -= 1
    print("Botão Cima OK")

  if bt_baixo.value() == 0:
    qual_tela += 1
    print("Botão Baixo OK")

  print(qual_tela)

  if qual_tela == 1: 

    if bt_vermelho.value() == 0:
      status_iluminacao = "OFF"
      print("Botão Vermelho OK")
    
    if bt_verde.value() == 0:
      status_iluminacao = "ON"
      print("Botão Verde OK")
    
    tela.fill(0)
    tela.text("ILUMINACAO", 0, 0)
    if status_iluminacao == "OFF":
      tela.text("STATUS: OFF", 0, 25)
      led_desligado.value (1)
      led_ligado(0)
    elif status_iluminacao == "ON":
      tela.text("STATUS: ON", 0, 25)
      led_desligado.value (0)
      led_ligado(1)
    tela.text("[1/4]", 0, 50)
    tela.show()

  elif qual_tela == 2:

    if bt_vermelho.value() == 0:
      status_ar_condicionado = "OFF"
      print("Botão Vermelho OK")
    
    if bt_verde.value() == 0:
      status_ar_condicionado = "ON"
      print("Botão Verde OK")
    
    tela.fill(0)
    tela.text("AR-CONDICIONADO", 0, 0)
    if status_ar_condicionado == "OFF":
      tela.text("STATUS: OFF", 0, 25)
      led_desligado.value (1)
      led_ligado(0)
    elif status_ar_condicionado == "ON":
      tela.text("STATUS: ON", 0, 25)
      led_desligado.value (0)
      led_ligado(1)
    tela.text("[2/4]",0, 50)
    tela.show()

  elif qual_tela == 3:

    if bt_vermelho.value() == 0:
      status_portao_principal = "OFF"
      print("Botão Vermelho OK")
    
    if bt_verde.value() == 0:
      status_portao_principal = "ON"
      print("Botão Verde OK")

    tela.fill(0)
    tela.text("PORTAO PRINCIPAL", 0, 0)
    if status_portao_principal == "OFF":
      tela.text("STATUS: OFF", 0, 25)
      led_desligado.value (1)
      led_ligado(0)
    elif status_portao_principal == "ON":
      tela.text("STATUS: ON", 0, 25)
      led_desligado.value (0)
      led_ligado(1)
    tela.text("[3/4]", 0, 50)
    tela.show()

  elif qual_tela == 4:

    if bt_vermelho.value() == 0:
      status_cameras = "OFF"
      print("Botão Vermelho OK")
    
    if bt_verde.value() == 0:
      status_cameras = "ON"
      print("Botão Verde OK")
    
    tela.fill(0)
    tela.text("CAMERAS", 0, 0)
    if status_cameras == "OFF":
      tela.text("STATUS: OFF", 0, 25)
      led_desligado.value (1)
      led_ligado(0)
    elif status_cameras == "ON":
      tela.text("STATUS: ON", 0, 25)
      led_desligado.value (0)
      led_ligado(1)
    tela.text("[4/4]",0, 50)
    tela.show()

  time.sleep(0.1)
  