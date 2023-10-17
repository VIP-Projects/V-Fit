## V Fit : 멀티모달 생성형 AI 기반 가상 피팅 앱서비스 


#### 2023년 공개SW 개발자대회 - [V FiT] 김준용, 길다영, 황현빈

<br>

### Members
김준용 | 길다영 | 황현빈
:-:|:-:|:-:
<a href="https://github.com/wragon"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>|<a href="https://github.com/arittung"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>|<a href="https://github.com/HWANGHYUNBIN"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>
<img alt="Html" src ="https://img.shields.io/badge/팀장-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/의상 피팅 모델 구현 및 적용-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/애플리케이션 UI제작-DFDFDF?style=for-the-badge"/> |<img alt="Html" src ="https://img.shields.io/badge/팀원-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/헤어 피팅 모델 구현 및 적용-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/애플리케이션 UI제작-DFDFDF?style=for-the-badge"/>|<img alt="Html" src ="https://img.shields.io/badge/팀원-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/크롤링 수행-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/서버 구현-DFDFDF?style=for-the-badge"/><img alt="Html" src ="https://img.shields.io/badge/애플리케이션 통신-F4F3F3?style=for-the-badge"/>




### 프로젝트 소개
- 본 프로젝트에서는 사용자가 비용을 지불하기 전에 스타일을 확인하여 소요 시간과 비용을 절약하고 만족도를 높일 수 있는 의상 및 헤어 가상 피팅 서비스를 제공한다.

<br><br>


## 시스템 구성

<p align="center">
<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/5e057b01-26e8-4d07-b813-73bdabde317d" style="width:600px"></p>


<br><br>


## 의상 가상 피팅 방법

#### 데이터셋
- VITON dataset

#### 구현 기능
- 옷 마스크 추출 → 모델 Pose, Segmentation → 추론
#### 구현 내용
-	<b> Virtual Fitting model :</b> Pose Estimation(Open Pose - pose_iter_440000.caffemodel)
-	<b> Fashion Mask Extraction Model :</b> U2Net Model
-	<b> Human Segmentation Mask Model :</b> ACGPN Model

<p align="center">
<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/7c5fbec5-c086-4cfb-9ae9-c4c5b6212d02" style="width:500px"></p>





<br>

## 헤어 가상 피팅 방법
#### 구현 기능
- 이미지와 헤어 정보 텍스트를 입력 → 멀티모달 수행 → 헤어 합성 이미지 생성
#### 구현 내용
- cloud API를 통해 StyleCLIP 모델을 사용
- 헤어스타일 관련 텍스트 정보를 입력으로 받아 사용자 이미지를 변경하는 멀티 모달 수행 
- manipulation_strength 옵션을 사용하여 스타일 세기 조정
#### 종류

  Types of hair fitting | hairs
  -- | --
  헤어스타일 | fringle hair(앞머리), short hair(짧은 머리), lonb hair(긴 머리), straignt hair(생머리),   <br> culry hairstyle(곱슬머리), afri hairstyle(크고 둥글게 만든 곱슬머리), hi-top fade hair(정수리의 머리카락을 길게 기르고 옆머리를 매우 짧게 이발),   <br> mohawk hairstyle(정수리를 중심으로 정가운데만 곧게 뻗치게 하고 양옆은 삭발), bald(대머리)
  헤어 컬러 | blond, red, blue, white, black, grey

<br>

## 웹 크롤링 방법
####  수집 데이터
- 무신사 내의 상품 id, 의상 이미지, 성별, 카테고리, 제품명
####  구현 기능
- 이미지 데이터 및 상품 정보 데이터 크롤링, 성별 및 카테고리별 분류, 가상 피팅 방법과의 연동 및 추천 옷 이미지 제공
####  구현 내용
-	(성별 – 카테고리) 별로 의상 이미지를 무신사 추천순으로 수집
-	의상 피팅에 적합한 이미지를 선별
-	사용자 추천 옷 이미지로 사용

<br>

##  AI 서버 구현

####  구현 기능
- 애플리케이션과 통신하여 데이터 송•수신, 의상 피팅 및 헤어 피팅 수행
####  구현 내용
-	애플리케이션과 통신하여 이미지 및 텍스트 데이터를 송•수신
-	애플리케이션에서 가상 피팅 요청 시 데이터를 전달받아 AI 모델을 통해 피팅 수행
-	가상 피팅 결과 이미지를 애플리케이션에 전송
-	원활한 통신을 위해 base64를 활용하여 이미지를 텍스트로 변환


<br><br>

## 개발 환경 및 개발 언어

```
운영체제 : Linux 22.04
GPU : GeForce RTX 3090
개발언어 : Python 3.7 / Java 11
사용 툴 : Jupyter notebook, Android Studio Giraffe
AI 라이브러리 : Pytorch 1.7.1
```

<br><br>

## Virtual Fitting 실행 방법

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

main.py 실행

  
  ```
  # input 
  cloth_path = 'inputs/cloth/000038_1.jpg'    # 옷 이미지 경로
  img_path = 'inputs/img/000174_0.jpg'        # 사용자 이미지 경로

  # output
  V_Fit.vfit(cloth_path, img_path)         # virtual fitting 결과 이미지 경로
   ```



<br><br>




## 팀원 역할

팀원|역할
--|--
김준용|팀장, 의상 피팅 모델 구현 및 적용, 애플리케이션 UI제작
길다영|팀원, 헤어 피팅 모델 구현 및 적용, 애플리케이션 UI제작
황현빈|팀원, 크롤링 수행, 서버 구현, 애플리케이션 통신


