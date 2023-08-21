# Virtual Fitting

### 모델, checkpoint 준비

#### 1) Pose Prediction Model

- './pose' 에 저장
- [DOWNLOAD](https://github.com/foss-for-synopsys-dwc-arc-processors/synopsys-caffe-models/blob/master/caffe_models/openpose/caffe_model/pose_iter_440000.caffemodel)

#### 2) Human Segmentation Mask 모델

- './ACGPN' 에 'lip_final.pth'로 파일명 변경하여 저장
- [DOWNLOAD](https://drive.google.com/uc?id=1k4dllHpu)

#### 3) Cloth Mask 모델
- './U2Net/saved_models/u2netp/'에 'u2netp.pth'으로 파일명 변경하여 저장
- [DOWNLOAD](https://drive.google.com/uc?id=1rbSTGKAE-MTxBYHd-51l2hMOQPT_7EPy)

- './U2Net/saved_models/u2net/'에 'u2net.pth'으로 파일명 변경하여 저장
- [DOWNLOAD](https://drive.google.com/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ)

#### 4) ACGPN 모델
- './checkpoints/'에 저장 후 unzip
- [DOWNLOAD](https://drive.google.com/uc?id=1UWT6esQIU_d4tUm8cjxDKMhB8joQbrFx)


<br>

### 실행 방법

- [main.py](https://github.com/VIP-Projects/V-Fit/blob/dayoung/Virtual_Fitting/main.py) 실행

  
  ```
  # input 
  cloth_path = 'inputs/cloth/000038_1.jpg'    # 옷 이미지 경로
  img_path = 'inputs/img/000174_0.jpg'        # 사용자 이미지 경로

  # output
  V_Fit.vfit(cloth_path, img_path)         # virtual fitting 결과 이미지 경로
   ```





<br>

### conda 환경
pytorch 1.7.1 / python=3.7

