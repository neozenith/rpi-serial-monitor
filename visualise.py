#!/usr/bin/env python

import sys

from datetime import datetime
import argparse

from PIL import ImageFont

import inkyphat

print("""Visualise:

Display information about MQTT feeds

""")

def center(message, font, x=None, y=None):
  """Center text on Inky pHat eInk display

  Parameters:
    message: str - The text to display
    font: ImageFont - See PIL.ImageFont for more information
    x: int - Optional hardcoded x coordinate
    y: int - Optional hardcoded y coordinate

  Returns:
    x: int - x cordinate of final text
    y: int - y coordinate of final text
    w: int - width of text with font
    h: int - height of text with font

  """
  w, h = font.getsize(message)

  if x == None:
    x = (inkyphat.WIDTH / 2) - (w / 2)

  if y == None:
    y = (inkyphat.HEIGHT / 2) - (h / 2)

  inkyphat.text((x, y), message, inkyphat.BLACK, font)

  return x, y, w, h

def main():
  inkyphat.set_rotation(180)

  if len(sys.argv) < 2:
      print("""Usage: {} <your name> <colour>
        Valid colours for v2 are: red, yellow or black
        Inky pHAT v1 is only available in red.
  """.format(sys.argv[0]))
      sys.exit(1)

  inkyphat.set_colour("red")

  ssh = "ssh> pi@{}".format(sys.argv[1])
  web = "http://{}".format(sys.argv[1])

  inkyphat.set_border(inkyphat.RED)

  font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 22)

  x, y, w, h = center(ssh, font)
  center(web, font, y=y+h)
  current_time = datetime.now().strftime('%Y-%m-%d %H:%M')
  center(current_time, font, y=0)

  inkyphat.show()



if __name__ == "__main__":
  main()