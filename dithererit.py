from PIL import Image, ImageOps
import hitherdither
import random

PALETTE = hitherdither.palette.Palette([(25,25,25), (75,75,75),(125,125,125),(175,175,175),(225,225,225),(250,250,250)])
THRESHOLD = [9, 9, 9]
COLOURS = [
  '#E6C229',
  '#F17105',
  '#D11149',
  '#6610F2',
  '#1A8FE3'
]

COLZ = '#07004D'

img = Image.open('./image.jpg').convert('RGB')
img.thumbnail((1024,1024), Image.LANCZOS)

img_dithered = hitherdither.ordered.bayer.bayer_dithering(img, PALETTE, THRESHOLD, order=8)
img_colourized = ImageOps.colorize(img_dithered.convert('L'), black=COLZ, white="white")

out_file = './image_dithered.png'

img_colourized.save(out_file, optimize=True)
