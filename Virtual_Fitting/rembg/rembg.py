import rembg
from PIL import Image

input = Image.open('/home/jykim/JY_project/Project/Fashine/ACGPN/inputs/person_data/000347_1.jpg') # load image
output = rembg.remove(input) # remove background
output = output.convert('RGB')
output.save('/home/jykim/JY_project/Project/Fashine/ACGPN/inputs/person_data/re_000347_1.jpg') # save image