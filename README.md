## V Fit : 멀티모달 생성형 AI 기반 가상 피팅 앱서비스 [2023년 공개SW 개발자대회]



## Members
<div align="center">

김준용 | 길다영 | 황현빈
:-:|:-:|:-:
<a href="https://github.com/wragon"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>|<a href="https://github.com/arittung"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>|<a href="https://github.com/HWANGHYUNBIN"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"></a>
<img alt="Html" src ="https://img.shields.io/badge/팀장-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/의상 피팅 모델 구현 및 적용-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/애플리케이션 UI제작-DFDFDF?style=for-the-badge"/> |<img alt="Html" src ="https://img.shields.io/badge/팀원-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/헤어 피팅 모델 구현 및 적용-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/애플리케이션 UI제작-DFDFDF?style=for-the-badge"/>|<img alt="Html" src ="https://img.shields.io/badge/팀원-B1BED5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/크롤링 수행-BFD8D5?style=for-the-badge"/> <img alt="Html" src ="https://img.shields.io/badge/서버 구현-DFDFDF?style=for-the-badge"/><img alt="Html" src ="https://img.shields.io/badge/애플리케이션 통신-F4F3F3?style=for-the-badge"/>

</div>

<br>

## Contents

- [프로젝트 소개](#프로젝트-소개)
  - [개발 기간](#개발-기간)
  - [개발 배경 및 목적](#개발-배경-및-목적) 
  - [기대 및 활용 분야](#기대-및-활용-분야)
  - [확장 가능성](#확장-가능성)
  - [서비스 시연 ](#서비스-시연)
- [시스템 구성](#시스템-구성)
  - [Directory 구조](#Directory-구조)
  - [구현 방법](#구현-방법)
    - [1. 의상 가상 피팅 방법](#1-의상-가상-피팅-방법)
    - [2. 헤어 가상 피팅 방법](#2-헤어-가상-피팅-방법)
    - [3. 어플리케이션 구현](#3-어플리케이션-구현)
    - [4. AI 서버 구현](#4-AI-서버-구현)
- [실행 방법](#실행-방법)
- [개발 환경 및 개발 언어](#개발-환경-및-개발-언어)
- [License](#License)


<br><br>

## 프로젝트 소개

### 개발 기간
- 23.06.15 - 23.09.07


### 개발 배경 및 목적
- 본 프로젝트에서는 사용자가 비용을 지불하기 전에 스타일을 확인하여 소요 시간과 비용을 절약하고 만족도를 높일 수 있는 <b>의상 및 헤어 가상 피팅 앱 서비스</b>를 제공한다.

  ##### 가상 의상 피팅의 필요성 및 핵심 기능
  >- 앱이나 웹을 통해 빠르고 편리하게 옷을 구매하는 사람들이 증가하고 있다. 온라인 쇼핑의 단점 중 하나는 실제로 배송 받은 옷을 입어봤을 때 핏이나 스타일이 예상과 다를 수 있다는 점이다. 이로 인해 구매 후 반품이 빈번하게 발생하며, 이는 온라인 쇼핑의 주요 문제 중 하나다. 
  >- 본 프로젝트는 이러한 문제를 해결하고, 반품으로 인한 시간과 비용 손실을 줄이며, 개별 고객에게 잘 맞는 스타일의 옷을 사전에 확인하고 구매할 수 있도록 ACGPN(Advanced Clothing and Garment Personalization Network) 기반의 가상 의상 피팅 및 옷 추천 서비스를 제공한다.

  ##### 가상 헤어 피팅의 필요성 및 핵심 기능
  >- 헤어스타일은 많은 사람들에게 중요하다. 개인의 외모와 자신감에 큰 영향을 미치기 때문에, 헤어스타일 변경을 고려하는 많은 사람들은 어떤 헤어스타일이 어떻게 얼굴 형태와 피부 톤과 조화를 이룰지 확신하기 어렵다. 
  >- 본 프로젝트에서는 고객이 어떤 헤어스타일이 어떻게 어울릴지 시뮬레이션하고 확신을 얻을 수 있도록 도움을 줄 수 있는 StyleCLIP 기반의 가상 헤어 피팅 서비스를 제공한다. 이를 통해 고객은 헤어스타일 변경에 대한 확신을 얻을 수 있으며, 미용사나 스타일리스트와의 상담 시에도 더욱 명확하게 의사소통 하는데도 도움이 될 수 있다. 



<!--#### 핵심 기능-->

### 기대 및 활용 분야

>- 업체가 제공한 사진과 정보만 보고 의사결정을 해야 했던 고객들은 본 프로젝트를 통해 미리 옷과 헤어를 피팅 할 수 있다.
>- 이 서비스는 다양한 스타일링 옵션을 제공하여 고객의 만족도를 높이는 동시에 옷의 핏이나 스타일을 사전에 확인함으로써 반품율 감소에 도움이 된다.
>- 이러한 서비스를 활용하면 스타일리스트나 이미지 컨설턴트는 고객에게 개인화된 스타일 조언을 제공할 수 있으며, 이를 통해 고객들의 스타일 취향을 파악하여 패션 및 미용 분야의 마케팅 전략을 더욱 효과적으로 개선 가능하다.
>- 쇼핑 업체들은 가상 피팅을 통해 고객이 제품을 더욱 현실적으로 체험하게 할 수 있으며, 이를 통해 온라인 쇼핑 경험 및 만족도를 향상시킬 수 있다. 

### 확장 가능성
>- 카메라 사진 촬영 기능 추가
>- 헤어 스타일 세기(ex. 웨이브의 세기나 염색의 세기 등)를 사용자가 직접 지정할 수 있는 시크바 구현
>- 결과 이미지 다운로드 기능 추가
>- 성별, 나이 및 카테고리별 추천 옷 데이터 저장 Database 추가
>- 날씨별 또는 상황별 옷 추천 기능 추가


<br>

### 서비스 시연 

<div align="center">
<a href="https://www.youtube.com/watch?v=u5lOjsgrRXE"><img src="https://img.shields.io/badge/V Fit Demo Video-YouTube-FF0000?style=for-the-badge&logo=YouTube&logoColor=white"></a>

의상 피팅 | 추천 의상 피팅 | 헤어 피팅
--|--|--
<img src="https://github.com/VIP-Projects/V-Fit-App/assets/53934639/ddd90ea7-5d5a-4ca2-a68d-9fbbe044df28" style="width:200px"> | <img src="https://github.com/VIP-Projects/V-Fit-App/assets/53934639/e1e87022-70ae-44ac-b135-1df309f41b91" style="width:200px">|<img src="https://github.com/VIP-Projects/V-Fit-App/assets/53934639/7317a44d-ff18-4080-be13-efbd5a40941c" style="width:200px">

</div>

<br><br>


## 시스템 구성

<p align="center">
<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/5e057b01-26e8-4d07-b813-73bdabde317d" style="width:600px">
</p>


<br>

### Directory 구조

<details>
<summary>Directory Structure</summary>
<div markdown="1">

  ```
virtual fitting dir
  ```

</div>

</details>

<br>

### 구현 방법

#### 1. 의상 가상 피팅 방법

- [Virtual Cloth Fit.md](https://github.com/VIP-Projects/V-Fit/blob/main/Virtual%20Cloth%20Fit.md)

#### 2. 헤어 가상 피팅 방법

- [Virtual Hair Fit.md](https://github.com/VIP-Projects/V-Fit/blob/main/Virtual%20Hair%20Fit.md)

#### 3. 어플리케이션 구현

- [Application.md](https://github.com/VIP-Projects/V-Fit/blob/main/Application.md)

#### 4. 딥러닝 서버 구현

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
# 1. 서버 실행
python ./Firtual_Fitting/flask_server.py

# 2. Android App 구동
```

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

## License

- <b>Virtual Cloth Fitting </b>: [Towards Photo-Realistic Virtual Try-On by Adaptively Generating↔Preserving Image Content](https://github.com/switchablenorms/DeepFashion_Try_On)
- <b>Virtual Hair Fitting</b>:  [StyleCLIP: Text-Driven Manipulation of StyleGAN Imagery](https://github.com/orpatashnik/StyleCLIP)
- <b>Web Crawling </b>: 1차 23.0.0., 2차 23.0.0 로 무신사에 데이터 사용에 대한 문의를 보냈고, 아직 답을 기다리는 중.











