## 의상 가상 피팅 방법

<p align="center">
<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/7c5fbec5-c086-4cfb-9ae9-c4c5b6212d02" style="width:500px"></p>

### 데이터셋
- VITON dataset



### 구현 기능
- 옷 마스크 추출 → 모델 Pose, Segmentation → 추론



### 구현 내용
-	<b> Virtual Fitting model :</b> Pose Estimation(Open Pose - pose_iter_440000.caffemodel)
-	<b> Fashion Mask Extraction Model :</b> U2Net Model
-	<b> Human Segmentation Mask Model :</b> ACGPN Model

<br><br>

##  의상 가상 피팅 실행 방법

### 1. 모델, checkpoint 준비

<b> Human Segmentation Mask 모델  </b>

- './Virtual_Fitting' 에 'lip_final.pth'로 파일명 변경하여 저장
- [DOWNLOAD](https://drive.google.com/uc?id=1k4dllHpu)

<b> ACGPN 모델  </b>
- './Virtual_Fitting/checkpoints/'에 저장 후 unzip
- [DOWNLOAD](https://drive.google.com/uc?id=1UWT6esQIU_d4tUm8cjxDKMhB8joQbrFx)

<b> Pose Prediction Model </b>

- './Virtual_Fitting/pose' 에 저장
- [DOWNLOAD](https://github.com/foss-for-synopsys-dwc-arc-processors/synopsys-caffe-models/blob/master/caffe_models/openpose/caffe_model/pose_iter_440000.caffemodel)
  
<b> Cloth Mask 모델  </b>
- './Virtual_Fitting/U2Net/saved_models/u2netp/'에 'u2netp.pth'으로 파일명 변경하여 저장
- [DOWNLOAD](https://drive.google.com/uc?id=1rbSTGKAE-MTxBYHd-51l2hMOQPT_7EPy)

- './U2Net/saved_models/u2net/'에 'u2net.pth'으로 파일명 변경하여 저장
- [DOWNLOAD](https://drive.google.com/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ)



<br>

### 2. 실행
  
  ```
 ./Virtual_Fitting/V_Fit.py 실행
   ```
