# https://github.com/orpatashnik/StyleCLIP
# https://replicate.com/orpatashnik/styleclip/api

import replicate
import urllib.request
import os

os.environ["REPLICATE_API_TOKEN"]="r8_*************************************"

image = open("./iu.jpg", "rb")

output = replicate.run(
    "orpatashnik/styleclip:7af9a66f36f97fee2fece7dcc927551a951f0022cbdd23747b9212f23fc17021",

    input={"input": image,                         # input image
            "neutral" : "a face with hair",        # origin    
            "target" : "a face with red hair",     # target 
            "manipulation_strength" : 7.5,         # 높을수록 target description에 가까워짐    
            "disentanglement_threshold" : 0.15     # Lower values mean that broader changes are made to the input image
           }
)

# image url
print(output) 

# 이미지 요청 및 다운로드
urllib.request.urlretrieve(output, "output.jpg")
