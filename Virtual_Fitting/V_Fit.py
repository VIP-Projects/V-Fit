import gdown
import numpy as np  # numpy <= 1.21
from PIL import Image
import IPython
import gdown
import os
import sys
import time
from predict_pose import generate_pose_keypoints

from U2Net.u2net_load import model
from U2Net.u2net_run import infer
from Self_ACGPN import simple_extractor
import test

def DeleteFiles(path):
    if os.path.exists(path):
        for file in os.scandir(path):
            os.remove(file.path)
            print("File Remove")
            return 0
        else:
            print("File not Find")
            return 0


u2net = model(model_name='u2netp')

def vfit(c_path, i_path):
    u2net = model(model_name='u2netp')


    # Data Preprocessing
    # data_path = 'inputs/cloth' + c_path
    DeleteFiles('./Data_preprocessing/test_color/')
    DeleteFiles('./Data_preprocessing/test_edge/')
    DeleteFiles('./Data_preprocessing/test_img/')
    DeleteFiles('./Data_preprocessing/test_label/')
    DeleteFiles('./Data_preprocessing/test_pose/')

    
    # Extraction of Cloth Mask
    cloth_name = f'cloth_{int(time.time())}.png'

    cloth_path = os.path.join('inputs/cloth', c_path)
    cloth = Image.open(cloth_path)
    cloth = cloth.resize((192, 256), Image.BICUBIC).convert('RGB')
    cloth.save(os.path.join('Data_preprocessing/test_color', cloth_name))

    infer(u2net, 'Data_preprocessing/test_color', 'Data_preprocessing/test_edge')


    # Model Pose, Segmentation
    img_name = f'img_{int(time.time())}.png'

    img_path = os.path.join('inputs/img' , i_path)
    print(img_path)
    img = Image.open(img_path)
    img = img.resize((192,256), Image.BICUBIC)

    img_path = os.path.join('Data_preprocessing/test_img', img_name)
    img.save(img_path)
    print(img_name)

    simple_extractor.main()
    pose_path = os.path.join('Data_preprocessing/test_pose', img_name.replace('.png', '_keypoints.json'))
    generate_pose_keypoints(img_path, pose_path)


    # Inference
    if os.path.isfile('Data_preprocessing/test_pairs.txt'):
        os.remove('Data_preprocessing/test_pairs.txt')
    with open('Data_preprocessing/test_pairs.txt', 'w') as f:
        f.write(f'{img_name} {cloth_name}')

    test.main()


    # Result
    output_grid = np.concatenate([
        np.array(Image.open(f'Data_preprocessing/test_img/{img_name}')),
        np.array(Image.open(f'Data_preprocessing/test_color/{cloth_name}')),
        np.array(Image.open(f'results/test/try-on/{img_name}'))
    ], axis=1)

    image_grid = Image.fromarray(output_grid)
    image_grid.show()
    output_path = "results/img.jpg"
    image_grid.save(output_path, "JPEG")

    return output_path
