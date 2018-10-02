#! /usr/bin/env python3

import serial


def main():
  print("hello")
  ser= serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
  )


if __name__ == "__main__":
  main()
