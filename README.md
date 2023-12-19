## V Fit : 멀티모달 생성형 AI 기반 가상 피팅 앱서비스 

<a href="https://kossa.kr/materials/2023/ossp/index.html"><img src ="https://img.shields.io/badge/2023 공개SW 개발자대회-우수작 선정-87AAAA?style=for-the-badge"/></a>

## Members
<div align="center">



김준용 | 길다영 | 황현빈
:-:|:-:|:-:
<a href="https://github.com/wragon"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>[![junyong@soongsil.ac.kr](https://img.shields.io/badge/Mail-004788?style=for-the-badge&logo=maildotcom&logoColor=white&link=mailto:junyong@soongsil.ac.kr)](junyong@soongsil.ac.kr)|<a href="https://github.com/arittung"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>[![dayoung.k.ssu@gmail.com](https://img.shields.io/badge/Mail-004788?style=for-the-badge&logo=maildotcom&logoColor=white&link=mailto:dayoung.k.ssu@gmail.com)](mailto:dayoung.k.ssu@gmail.com)|<a href="https://github.com/HWANGHYUNBIN"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>[![hhb9817@naver.com](https://img.shields.io/badge/Mail-004788?style=for-the-badge&logo=maildotcom&logoColor=white&link=mailto:hhb9817@naver.com)](hhb9817@naver.com)
<img alt="Html" src ="https://img.shields.io/badge/팀장-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/의상 피팅 모델 구현 및 적용-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/애플리케이션 UI제작-DFDFDF?style=for-the-badge"/> |<img alt="Html" src ="https://img.shields.io/badge/팀원-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/헤어 피팅 모델 구현 및 적용-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/애플리케이션 UI제작-DFDFDF?style=for-the-badge"/>|<img alt="Html" src ="https://img.shields.io/badge/팀원-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/크롤링 수행-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/서버 구현-DFDFDF?style=for-the-badge"/><img alt="Html" src ="https://img.shields.io/badge/애플리케이션 통신-F4F3F3?style=for-the-badge"/>

</div>

<br>

## Contents

- [프로젝트 소개](#프로젝트-소개)
- [시스템 구성](#시스템-구성)
  - [개발 환경 및 개발 언어](#-개발-환경-및-개발-언어)
  - [시스템 디렉터리 구조](#-시스템-디렉터리-구조)
  - [구현 방법](#-구현-방법)
    - [1. 의상 가상 피팅 방법](#1-의상-가상-피팅-방법)
    - [2. 헤어 가상 피팅 방법](#2-헤어-가상-피팅-방법)
    - [3. 어플리케이션 구현](#3-어플리케이션-구현)
    - [4. 딥러닝 서버 구현](#4-딥러닝-서버-구현)
- [실행 방법](#실행-방법)
- [확장 가능성](#확장-가능성)
- [License](#License)


<br><br>

## 프로젝트 소개

### 📅 개발 기간
- 23.06.15 - 23.09.07 (2023 공개SW 개발자대회)

<br>

### 💡 개발 배경 및 목적

- 코로나 시대 이후 많은 서비스들이 비대면으로 전환되며, 고객들이 직접 가게를 방문하지 않는 온라인 쇼핑몰이 급증하였다.
  
- 그 중에서도 온라인 패션 거래액의 규모는 지속적으로 성장하여, 2022년 기준 약 49조원을 넘었다.
- 또한, 최근에는 미용을 위한 헤어샵을 방문하기 위해 온라인 예약제가 적용되는 추세이며, 이를 위해 네이버와 같은 플랫폼에서도 온라인 예약 서비스를 제공하고 있다.
- 이러한 온라인 패션 쇼핑과 헤어샵 예약의 공통점은 서비스 이용을 위해 비대면 방식이 적용되지만, 실제 서비스를 이용하여 의상을 입어보거나 헤어 서비스를 받기 전까지 고객의 모습을 확인할 수 없다는 것이다.
- 본 프로젝트에서는 사용자가 의상 구매 및 헤어 서비스를 결정하기 전에 자신의 스타일을 확인하여, 결정에 소요되는 시간 및 비용을 절약하고 만족도를 높일 수 있는  <b>의상 및 헤어 가상 피팅 앱 서비스</b>를 제공한다. 

<br>



### 📼 서비스 시연 

<div align="center">
<a href="https://www.youtube.com/watch?v=u5lOjsgrRXE"><img src="https://img.shields.io/badge/V Fit Demo Video-YouTube-FF0000?style=for-the-badge&logo=YouTube&logoColor=white"></a>

의상 피팅(직접 업로드) | 의상 피팅(추천 옷) | 헤어 피팅(스타일) | 헤어 피팅(컬러)
--|--|--|--
<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/1acd07f5-88c7-487a-95e2-40f189472148" style="width:200px"> | <img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/f1525463-b1a6-4114-8c36-1ad086951fff" style="width:200px">|<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/f49beca7-e09a-4684-850e-3bfc4d8ef4f0" style="width:200px">|<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/cd4dcedc-9faf-4d5a-a648-f52da902a3fa" style="width:200px">





</div>



<br>

### 📱 필요성 및 핵심 기능

#### 가상 의상 피팅

  - 앱이나 웹을 통해 빠르고 편리하게 옷을 구매하는 사람들이 증가하는 경향이 있음.
  - 온라인 쇼핑의 단점 중 하나는 실제로 배송 받은 옷을 입어봤을 때 핏이나 스타일이 예상과 다를 수 있다는 점으로, 이로 인해 구매 후 반품이 빈번하게 발생하며, 이는 온라인 쇼핑의 주요 문제 중 하나임. 
  - 본 프로젝트는 이러한 문제를 해결하기 위해, 개별 고객에게 잘 맞는 스타일의 옷을 사전에 확인할 수 있도록 사용자가 가상으로 의상을 입어볼 수 있는 <b>ACGPN(Advanced Clothing and Garment Personalization Network) 기반의 가상 의상 피팅 및 옷 추천 서비스를 제공</b>함.


#### 가상 헤어 피팅


  - 헤어스타일은 개인의 외모와 자신감에 큰 영향을 미치기 때문에, 헤어스타일 변경을 고려하는 많은 사람들은 어떤 헤어스타일이 자신의 얼굴 형태와 피부 톤과 조화를 이룰지 확신하기 어려워 함. 
  - 본 프로젝트에서는 고객이 어떤 헤어스타일이 어떻게 어울릴지 시뮬레이션하고 확신을 얻을 수 있도록 도움을 줄 수 있는 <b>StyleCLIP 기반의 가상 헤어 피팅 서비스</b>를 제공함.
  - 이를 통해 고객은 헤어스타일 변경에 대한 확신을 얻을 수 있으며, 미용사나 스타일리스트와의 상담 시에도 더욱 명확하게 의사소통 하는데도 도움을 줄 수 있음. 


<br>

### 💫 기대 효과

- 소비자 뿐만 아니라 온라인 쇼핑몰이 반품으로 인한 <b>감정적, 경제적 손실을 줄일 수 있음 </b>
- <b>지인에게</b> 잘 어울리는 의류 스타일과 색상 확인하여 <b>옷을 선물해주기에 용이함</b>

- 스타일 변경 실패에 대한 두려움을 줄일 수 있으며, <b>헤어 관련 업체와 고객 간의 갈등을 줄일 수 있음</b>
- 자신에게 어울리는 <b>의상 및 헤어 스타일을 잘 알지 못하는 20-30대 연령층</b>이 새로운 고객이 될 수 있으며, <b>본인의 스타일이 확립된 40-50대 연령층</b>에게 스타일 변경에 대한 흥미를 유발할 수 있음





<br><br>


## 시스템 구성

<p align="center">
<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/5e057b01-26e8-4d07-b813-73bdabde317d" style="width:600px">
</p>



<br>

### 🛠 개발 환경 및 개발 언어

```
운영체제 : Linux 22.04
GPU : GeForce RTX 3090
개발언어 : Python 3.7 / Java 11
사용 툴 : Jupyter notebook, Android Studio Giraffe
AI 라이브러리 : Pytorch 1.7.1
```


<br>

### 🗂 시스템 디렉터리 구조

<details>
<summary>Directory Structure</summary>
<div markdown="1">

  ```
virtual fitting dir

.
|--Virtual_Fitting
|      |--checkpoints
|      |            '--label2city
|      |--Data_preprocessing
|      |            |--test_color
|      |            |--test_colormask
|      |            |--test_edge
|      |            |--test_img
|      |            |--test_label
|      |            |--test_mask
|      |            '--test_pose
|      |--Self_ACGPN
|      |            |--datasets
|      |            |      |--__init__.py
|      |            |      |--datasets.py
|      |            |      |--simple_extractor_dataset.py
|      |            |      '--target_generation.py
|      |            |--modules
|      |            |      |--__init__.py
|      |            |      |--bn.py
|      |            |      |--deeplab.py
|      |            |      |--dense.py
|      |            |      |--functions.py
|      |            |      |--misc.py
|      |            |      '--residual.py
|      |            |--networks
|      |            |      |--backbone
|      |            |      |      |--mobilenetv2.py
|      |            |      |      |--resnet.py
|      |            |      |      '--resnext.py
|      |            |      |--context_encoding
|      |            |      |      |--aspp.py
|      |            |      |      |--ocnet.py
|      |            |      |      '--psp.py
|      |            |      |--__init__.py
|      |            |      '--AugmentCE2P.py
|      |            |--utils
|      |            |      |--__init__.py
|      |            |      '--transforms.py
|      |            '--simple_extractor.py
|      |--U2Net
|      |            |--model
|      |            |      |--__init__.py
|      |            |      |--u2net.py
|      |            |      '--u2net_refactor.py
|      |            |--save_models
|      |            |      |--face_detection_cv2
|      |            |      |--u2net
|      |            |      '--u2netp
|      |            |--data_loader.py
|      |            |--u2net_load.py
|      |            |--u2net_run.py
|      |            '--u2net_test.py
|      |--data
|      |            |--aligned_dataset.py
|      |            |--base_data_loader.py
|      |            |--base_dataset.py
|      |            |--custom_dataset_data_loader.py
|      |            |--data_loader.py
|      |            '--image_folder.py
|      |--options
|      |            |--base_options.py
|      |            '--test_options.py
|      |--pose
|      |            |--pose_deploy_linevec.prototxt
|      |            '--pose_iter_440000.caffemodel
|      |--util
|      |            |--image_pool.py
|      |            '--util.py
|      |--Hair_Fit.py
|      |--V_Fit.py
|      |--flask_server.py
|      |--grid_sample.py
|      |--predict_pose.py
|      |--test.py
|      '--tps_grid_gen.py
.
|--Android App
|      |--src/main
|      |      |--java/com/example/vfitapplication
|      |      |            |--MainActivity.java
|      |      |            |--ProgressDialog.java
|      |      |            |--SubActivity2.java
|      |      |            |--SubActivity3.java
|      |      |            |--SubActivity3_1.java
|      |      |            |--SubActivity3_1_1.java
|      |      |            |--SubActivity3_1_2.java
|      |      |            |--SubActivity4.java
|      |      |            |--SubActivity4_1.java
|      |      |            '--SubActivity4_2.java
|      |      |--res
|      |      |            |--drawble
|      |      |            |      |--white.png
|      |      |            |      |--iu.jpg
|      |      |            |      |--iu_hair.jpg
|      |      |            |      |--iu_result.png
|      |      |            |      |--btn_white_blackstroke.xml
|      |      |            |      |--ic_launcher_background.xml
|      |      |            |      |--ic_launcher_foreground.xml
|      |      |            |      |--progress_bg.xml
|      |      |            |      |--progress_image.xml
|      |      |            |--layout
|      |      |            |      |--activity_main.xml
|      |      |            |      |--activity_sub2.xml
|      |      |            |      |--activity_sub3.xml
|      |      |            |      |--activity_sub31.xml
|      |      |            |      |--activity_sub311.xml
|      |      |            |      |--activity_sub312.xml
|      |      |            |      |--activity_sub4.xml
|      |      |            |      |--activity_sub41.xml
|      |      |            |      |--activity_sub42.xml
|      |      |            |      '--dialog_progress.xml
|      |      '--AndroidManifest.xml
|      '--build.gradle.kts
'
  ```

</div>

</details>

<br>

### 💻 구현 방법

#### 1. 의상 가상 피팅 방법

- 옷 마스크 추출 → 모델 Pose, Segmentation → 추론
- [Virtual Cloth Fit.md](https://github.com/VIP-Projects/V-Fit/blob/main/Virtual%20Cloth%20Fit.md)

#### 2. 헤어 가상 피팅 방법

- 이미지와 헤어 정보 텍스트를 입력 → 멀티모달 수행 → 헤어 합성 이미지 생성
- [Virtual Hair Fit.md](https://github.com/VIP-Projects/V-Fit/blob/main/Virtual%20Hair%20Fit.md)

#### 3. 어플리케이션 구현

- 사용자가 애플리케이션을 통해 가상 피팅 기능을 사용, 원하는 의상 및 헤어를 피팅하여 결과를 확인
- [Application.md](https://github.com/VIP-Projects/V-Fit/blob/main/Application.md)

#### 4. 딥러닝 서버 구현

- 애플리케이션과 통신하여 데이터 송•수신, 의상 피팅 및 헤어 피팅 수행
- [Server.md](https://github.com/VIP-Projects/V-Fit/blob/main/Server.md)





<!--
## 웹 크롤링 방법
####  수집 데이터
- 무신사 내의 상품 id, 의상 이미지, 성별, 카테고리, 제품명
####  구현 기능
- 이미지 데이터 및 상품 정보 데이터 크롤링, 성별 및 카테고리별 분류, 가상 피팅 방법과의 연동 및 추천 옷 이미지 제공
####  구현 내용
-	(성별 – 카테고리) 별로 의상 이미지를 무신사 추천순으로 수집
-	의상 피팅에 적합한 이미지를 선별
-	사용자 추천 옷 이미지로 사용
-->




<br><br>

## 실행 방법

```
# 1. 환경 설정
Package 및 Android Studio 설치

# 2. 가상 의상 피팅 모델 Download
Virtual Cloth Fit.md 참고해 가상 의상 피팅 pretrained model Download

# 3. 서버 실행
python ./Firtual_Fitting/flask_server.py

# 4. Android App 구동
```



<br><br>

## 확장 가능성

- 가상 피팅의 정확도를 더 향상시킬 수 있는 CVPR 2023의 TryOnDiffusion 모델 구현
- 헤어 웨이브 및 염색의 세기를 조절할 수 있는 SeekBar 구현

- 성별 및 카테고리별 옷 데이터 추가 및 추천 기능 구현




<br><br>

## License

- <b>Virtual Cloth Fitting </b> - [Towards Photo-Realistic Virtual Try-On by Adaptively Generating↔Preserving Image Content](https://github.com/switchablenorms/DeepFashion_Try_On)
- <b>Virtual Hair Fitting</b> - [StyleCLIP: Text-Driven Manipulation of StyleGAN Imagery](https://github.com/orpatashnik/StyleCLIP)
- <b>Web Crawling </b> - 1차 23.08.11, 2차 23.10.17로 무신사 스토어에 웹 크롤링을 통한 데이터 사용에 대한 문의를 전달했으며, 현재 답변 대기중. 











