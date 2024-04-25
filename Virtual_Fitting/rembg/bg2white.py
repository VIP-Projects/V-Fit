import pixellib
from pixellib.tune_bg import alter_bg
from PIL import Image

change_bg = alter_bg()
change_bg.load_pascalvoc_model("./deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
change_bg.color_bg('/home/jykim/JY_project/Project/Fashine/ACGPN/inputs/person_data/re_000192_0.png', colors=(255, 255, 255), output_image_name='/home/jykim/JY_project/Project/Fashine/ACGPN/inputs/person_data/wh_000192_0.png')

im = Image.open('/home/jykim/JY_project/Project/Fashine/ACGPN/inputs/person_data/wh_000192_0.png').convert('RGB')
im.save('/home/jykim/JY_project/Project/Fashine/ACGPN/inputs/person_data/wh_000192_0.jpg', 'jpeg')