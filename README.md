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
  - [서비스 시연 ](#서비스-시연)
- [시스템 구성](#시스템-구성)
  - [Directory 구조](#Directory-구조)
  - [의상 가상 피팅 방법](#의상-가상-피팅-방법)
  - [헤어 가상 피팅 방법](#헤어-가상-피팅-방법)
  - [AI 서버 구현](#AI-서버-구현)
- [개발 환경 및 개발 언어](개발-환경-및-개발-언어)
- [실행 방법](실행-방법)


<br><br>

## 프로젝트 소개
- 본 프로젝트에서는 사용자가 비용을 지불하기 전에 스타일을 확인하여 소요 시간과 비용을 절약하고 만족도를 높일 수 있는 의상 및 헤어 가상 피팅 서비스를 제공한다.

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

<p align="center" width=100%>
<img src="https://github.com/VIP-Projects/V-Fit/assets/53934639/5e057b01-26e8-4d07-b813-73bdabde317d" style="width:50%">
<img src="https://github.com/VIP-Projects/V-Fit-App/assets/53934639/e75deef4-4193-44c0-bb22-4688aa068520" style="width:50%">
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


### 의상 가상 피팅 방법

- [Virtual Cloth Fit.md](https://github.com/VIP-Projects/V-Fit/blob/main/Virtual%20Cloth%20Fit.md)

### 헤어 가상 피팅 방법

- [Virtual Hair Fit.md](https://github.com/VIP-Projects/V-Fit/blob/main/Virtual%20Hair%20Fit.md)

### 어플리케이션 구현

- [Application.md](https://github.com/VIP-Projects/V-Fit/blob/main/Application.md)

### AI 서버 구현

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

## 개발 환경 및 개발 언어

```
운영체제 : Linux 22.04
GPU : GeForce RTX 3090
개발언어 : Python 3.7 / Java 11
사용 툴 : Jupyter notebook, Android Studio Giraffe
AI 라이브러리 : Pytorch 1.7.1
```

<br><br>

## 실행 방법

```
.py 실행
```



