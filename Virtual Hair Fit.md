## 헤어 가상 피팅 방법

### 구현 기능
- 이미지와 헤어 정보 텍스트를 입력 → 멀티모달 수행 → 헤어 합성 이미지 생성

<br>

### 구현 내용
- cloud API를 통해 StyleCLIP 모델을 사용
- 헤어스타일 관련 텍스트 정보를 입력으로 받아 사용자 이미지를 변경하는 멀티 모달 수행 
- manipulation_strength 옵션을 사용하여 스타일 세기 조정

<br>

### 종류
<!--
  Types of hair fitting | hairs
  -- | --
  헤어스타일 | fringle hair(앞머리), short hair(짧은 머리), lonb hair(긴 머리), straignt hair(생머리),   <br> culry hairstyle(곱슬머리), afri hairstyle(크고 둥글게 만든 곱슬머리), hi-top fade hair(정수리의 머리카락을 길게 기르고 옆머리를 매우 짧게 이발),   <br> mohawk hairstyle(정수리를 중심으로 정가운데만 곧게 뻗치게 하고 양옆은 삭발), bald(대머리)
  헤어 컬러 | blond, red, blue, white, black, grey
-->

#### 1. 헤어 스타일
- fringle hair(앞머리)
- short hair(짧은 머리)
- lonb hair(긴 머리)
- straignt hair(생머리)
- culry hairstyle(곱슬머리)
- afri hairstyle(크고 둥글게 만든 곱슬머리)
- hi-top fade hair(정수리의 머리카락을 길게 기르고 옆머리를 매우 짧게 이발)
- mohawk hairstyle(정수리를 중심으로 정가운데만 곧게 뻗치게 하고 양옆은 삭발)
- bald(대머리)

#### 2. 헤어 컬러
- blond
- red
- blue
- white
- black
- grey

<br>

### 실행
  
  ```
./Virtual_Fitting/Hair_Fit.py 실행
   ```

