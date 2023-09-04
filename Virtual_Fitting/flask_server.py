from flask import Flask, request, jsonify, send_file
from PIL import Image
import urllib.request
import os
import base64
import io
import V_Fit
os.environ["REPLICATE_API_TOKEN"]="r8_BKQTfIB1vSJgHaFTSfxUNHIvDGa2K6l2pYV7D"

import replicate

def DeleteFiles(path):
    if os.path.exists(path):
        for file in os.scandir(path):
            os.remove(file.path)
            print("File Remove")
            return 0
        else:
            print("File not Find")
            return 0
        
app = Flask(__name__)

# 서버 접속 시 기본 실행 function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# top fusion model function
@app.route('/hello', methods=['GET','POST'])
def hello_test():
    DeleteFiles('./Data_preprocessing/test_color/')
    DeleteFiles('./Data_preprocessing/test_edge/')
    DeleteFiles('./Data_preprocessing/test_img/')
    DeleteFiles('./Data_preprocessing/test_label/')
    DeleteFiles('./Data_preprocessing/test_pose/')
    print("hello~")
    data = request.get_json()
    # print(data['image'])
    imgdata1 = base64.b64decode(data['image1'])
    img1 = Image.open(io.BytesIO(imgdata1))
    imgdata2 = base64.b64decode(data['image2'])
    img2 = Image.open(io.BytesIO(imgdata2))
    
    img1.save('inputs/img/img1.jpg',"JPEG")
    img2.save('inputs/cloth/img2.jpg',"JPEG")

    # input 폴더에서 이미지 가져오기
    cloth_path = os.path.join(sorted(os.listdir('inputs/cloth'))[0])
    img_path = os.path.join(sorted(os.listdir('inputs/img'))[0])

    V_Fit.vfit(cloth_path, img_path)
    
    filename = "./results/img.jpg"
    with open(filename, 'rb') as f:
        load_file = f.read()
    result = base64.b64encode(load_file).decode('utf8')
    return jsonify({'data':result})

# 헤어 합성 모델 실행 function
@app.route("/use_hair_fit_model", methods=['GET','POST'])
def use_hair_fit_model():
    data = request.get_json()
    imgdata1 = base64.b64decode(data['image1'])
    img1 = Image.open(io.BytesIO(imgdata1))
    img1.save('img1.jpg',"JPEG")
    img1 = open("img1.jpg", "rb")
    
    neutral = str(data['neutral'])
    target = str(data['target'])
    manipulation_strength = str(data['mani'])
    output = replicate.run(
    "자신의 TokenAPI 받기",

    input={"input": img1,                         # input image
            "neutral" : neutral,        # origin    
            "target" : target,     # target 
            "manipulation_strength" : float(manipulation_strength),         # 높을수록 target description에 가까워짐    
            "disentanglement_threshold" : 0.15     # Lower values mean that broader changes are made to the input image
           }
    )
    print("!!!")

    # 이미지 요청 및 다운로드
    urllib.request.urlretrieve(output, "output.jpg")
    
    with open("output.jpg", 'rb') as f:
        load_file = f.read()
    result = base64.b64encode(load_file).decode('utf8')
    
    return jsonify({'data':result})


if __name__ == "__main__":
    app.run()
