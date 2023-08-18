import V_Fit
import os

# input 폴더에 사진 넣고 경로 설정
cloth_path = 'inputs/cloth/000038_1.jpg'
img_path = 'inputs/img/000174_0.jpg'

print(V_Fit.vfit(cloth_path, img_path))