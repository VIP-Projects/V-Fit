from flask import Flask, request, jsonify, send_file
from PIL import Image
import urllib.request
import os
import base64
import io
import V_Fit

# replicate 토큰 로드
os.environ["REPLICATE_API_TOKEN"]="r8_-----------------------------------------"

import replicate

# 이미지 로드 및 세이브 파일 제거
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

# 서버 접속 시 기본 실행 function - 서버 Test
@app.route('/')
def hello_world():
    return 'Hello, World!'

# 의상 피팅 모델 function
@app.route('/cloth_fit', methods=['GET','POST'])
def cloth_fit():
    # 이미 저장된 사진 제거
    DeleteFiles('./Data_preprocessing/test_color/')
    DeleteFiles('./Data_preprocessing/test_edge/')
    DeleteFiles('./Data_preprocessing/test_img/')
    DeleteFiles('./Data_preprocessing/test_label/')
    DeleteFiles('./Data_preprocessing/test_pose/')

    # 데이터 수신
    data = request.get_json()

    # 사용자 이미지
    imgdata1 = base64.b64decode(data['image1'])
    img1 = Image.open(io.BytesIO(imgdata1))
    # 의상 이미지
    imgdata2 = base64.b64decode(data['image2'])
    img2 = Image.open(io.BytesIO(imgdata2))
    # 이미지 저장
    img1.save('inputs/img/img1.jpg',"JPEG")
    img2.save('inputs/cloth/img2.jpg',"JPEG")

    # input 폴더에서 이미지 가져오기
    cloth_path = os.path.join(sorted(os.listdir('inputs/cloth'))[0])
    img_path = os.path.join(sorted(os.listdir('inputs/img'))[0])

    # 의상 피팅 실행 후 저장
    V_Fit.vfit(cloth_path, img_path)

    # 결과 이미지 전달
    filename = "./results/img.jpg"
    with open(filename, 'rb') as f:
        load_file = f.read()
    result = base64.b64encode(load_file).decode('utf8')
    
    return jsonify({'data':result})

# 헤어 피팅 모델 function
@app.route("/hair_fit", methods=['GET','POST'])
def hair_fit():
    # 데이터 수신
    data = request.get_json()
    # 사용자 이미지
    imgdata1 = base64.b64decode(data['image1'])
    img1 = Image.open(io.BytesIO(imgdata1))
    img1.save('img1.jpg',"JPEG")
    img1 = open("img1.jpg", "rb")

    # 헤어 정보 텍스트 데이터
    neutral = str(data['neutral'])
    target = str(data['target'])
    manipulation_strength = str(data['mani'])

    # 헤어 피팅 실행
    output = replicate.run(
    "자신의 API Token 받기",

    input={"input": img1,                         # input image
            "neutral" : neutral,        # origin    
            "target" : target,     # target 
            "manipulation_strength" : float(manipulation_strength),         # 높을수록 target description에 가까워짐    
            "disentanglement_threshold" : 0.15     # Lower values mean that broader changes are made to the input image
           }
    )

    # 결과 이미지 요청 및 다운로드
    urllib.request.urlretrieve(output, "output.jpg")
    
    # 결과 이미지 전달 
    with open("output.jpg", 'rb') as f:
        load_file = f.read()
    result = base64.b64encode(load_file).decode('utf8')
    
    return jsonify({'data':result})


if __name__ == "__main__":
    app.run()
