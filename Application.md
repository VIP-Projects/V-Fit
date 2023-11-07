## 어플리케이션 구현 방법

### 구현 기능
- 사용자가 애플리케이션을 통해 가상 피팅 기능을 사용, 원하는 의상 및 헤어를 피팅하여 결과를 확인

### 구현 내용 
-	의상 피팅 및 헤어 피팅 선택
-	사진 업로드 (옷, 모델)
-	피팅 할 옷 추천 페이지 
-	헤어 피팅 정보 선택(ex. 빨간 머리, 곱슬 머리 등)
-	사용자 가상 피팅 결과 출력


<br>



## 어플리케이션 구성

<!--
File Type | files
--|--
<b>javafile.java</b> | MainActivity → SubActivity2 → … → SubActivity3_1 → SubActivity3_1_1  → … 
<b>layout.xml</b> | activity_main → activity_sub2 → … → activity_sub31 → activity_sub311  → … 
-->

<p align="center">
<img src="https://github.com/VIP-Projects/V-Fit-App/assets/53934639/e75deef4-4193-44c0-bb22-4688aa068520" style="width:600px"></p>



-	<b> 모델 사진 업로드 페이지(옷 모델) :</b> 의상 피팅을 원하는 사용자의 사진을 업로드
-	<b> 옷 사진 업로드 페이지(갤러리 사용) :</b> 의상 피팅을 원하는 의상 사진을 업로드
-	<b> 옷 추천 페이지 :</b> 만약 원하는 의상이 모호하다면 자체적으로 추천해주는 사진을 선정
-	<b> 모델 사진 업로드 페이지(헤어 모델) :</b> 헤어 피팅을 원하는 사용자의 사진을 업로드
-	<b> 헤어 정보 선택 페이지 :</b> 원하는 헤어 스타일 (ex. 빨간 머리, 곱슬 머리 등)을 선택
-	<b> 결과 페이지 :</b> 의상 피팅 및 헤어 피팅 결과 정보를 사용자에게 전달


### Directory 구조

<details>
<summary>Directory Structure</summary>
<div markdown="1">

  ```
.
|--src/main
|      |--java/com/example/vfitapplication
|      |            |--MainActivity.java
|      |            |--ProgressDialog.java
|      |            |--SubActivity2.java
|      |            |--SubActivity3.java
|      |            |--SubActivity3_1.java
|      |            |--SubActivity3_1_1.java
|      |            |--SubActivity3_1_2.java
|      |            |--SubActivity4.java
|      |            |--SubActivity4_1.java
|      |            '--SubActivity4_2.java
|      |--res
|      |            |--drawble
|      |            |      |--white.png
|      |            |      |--iu.jpg
|      |            |      |--iu_hair.jpg
|      |            |      |--iu_result.png
|      |            |      |--btn_white_blackstroke.xml
|      |            |      |--ic_launcher_background.xml
|      |            |      |--ic_launcher_foreground.xml
|      |            |      |--progress_bg.xml
|      |            |      |--progress_image.xml
|      |            |--layout
|      |            |      |--activity_main.xml
|      |            |      |--activity_sub2.xml
|      |            |      |--activity_sub3.xml
|      |            |      |--activity_sub31.xml
|      |            |      |--activity_sub311.xml
|      |            |      |--activity_sub312.xml
|      |            |      |--activity_sub4.xml
|      |            |      |--activity_sub41.xml
|      |            |      |--activity_sub42.xml
|      |            |      '--dialog_progress.xml
|      '--AndroidManifest.xml
'--build.gradle.kts

  ```

</div>



