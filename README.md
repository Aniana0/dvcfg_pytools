# voice.dvcfg 작성/수정을 위한 파이썬 모듈

### voice.dvcfg란?   
DeepVocal의 음성 라이브러리를 제작할 때 필요한 파일로, 오디오 샘플에서 각 발음의 음소가 위치한 시간이 기록되어 있습니다.   
(UTAU의 oto.ini와 역할이 비슷하다고 볼 수 있습니다)
   
## dvcfg_pytools 소개   
voice.dvcfg를 파이썬에서 편하게 수정하기 위해 만든 모듈입니다.   
DeepVocal ToolBox의 'Voice Config'에서 할 수 있는 작업을 파이썬에서도 할 수 있도록 만들었습니다.   
그 외에 음성 라이브러리를 제작할 때 자주 필요할 것 같은 기능도 추가하고 있습니다.   
   
* **주의사항(?)**     
제작자가 코딩을 학교 교양강의에서 매우 기초만 살짝 배우고 나머지는 독학으로 배운 사람입니다...   
따라서 용어를 잘못 사용하거나 설명이 이상할 수도 있습니다...   
학업때문에 바빠서 업데이트가 느릴 수 있습니다.


## 설치
* [여기(클릭)](https://github.com/Aniana0/dvcfg_pytools/raw/main/install/dvcfg_pytools-1.0.0.tar.gz)에서 배포 파일을 다운로드합니다.
* 이후 다운로드한 파일이 있는 위치에서 아래와 같이 명령어를 실행합니다.
```
pip install dvcfg_pytools-1.0.0.tar.gz
```
또는
```
python -m pip install dvcfg_pytools-1.0.0.tar.gz
```


## 사용법   
* dvcfg_pytools 모듈을 불러온 다음, Dvcfg 클래스를 이용해 객체를 생성합니다.

```Python
import dvcfg_pytools   
   
dvcfg_file = dvcfg_pytools.Dvcfg()
```   

* 이후 메소드를 이용해 원하는 작업합니다

#### 예시)

```Python
import dvcfg_pytools   
   
dvcfg_file = dvcfg_pytools.Dvcfg()
   
dvcfg_file.load('voice.dvcfg')

dvcfg_file.edit_CV('ga','C#4',1.045,1.062,1.12,1.34)
dvcfg_file.edit_VX('a_a','F4',7.0,7.1)
dvcfg_file.add_INDIE('voice/breath.wav','breath','C#4',0.55,1.07)

dvcfg_file.save('')
```   
자세한 예시는 [이 파일](https://drive.google.com/file/d/1ZvzIF6MUlEn1IRVJseAzOdWzQ1XJaEmL/view?usp=sharing)을 참고해주세요.

## 기본 메소드
Voice Config에 있는 기능들을 구현한 메소드입니다.

### 파일과 데이터 계열

* #### load( 파일이름 )
   * voice.dvcfg 파일에서 데이터를 읽어들입니다.
   
* #### save( 파일이름='voice.dvcfg' )
   * 객체에 저장된 voice.dvcfg 데이터를 파일로 저장합니다.
   * 아무것도 입력하지 않으면 'voice.dvcfg'로 저장합니다.
   
* #### dict_to_dvcfg( 딕셔너리 )
   * 입력한 딕셔너리를 객체의 voice.dvcfg 데이터로 지정합니다.

* #### dvcfg_to_dict()
   * 객체에 저장된 voice.dvcfg 데이터를 딕셔너리로 반환합니다.


### 발음 항목 추가 계열

* **CV 타입의 마커**
1. CP : Connect Point
2. PP : Preutterance Point
3. VSP: Vowel Start Point
4. VEP: Vowel End Point

* **V_X, INDIE 타입의 마커**
1. SP : Start Point
2. EP : End Poiint

마커가 위치할 시간을 각 마커와 같은 이름의 매개변수에 입력하면 됩니다.   
시간 단위는 모두 초(s)입니다.   


* #### add_CV( 오디오 파일이름 , 발음기호 , 피치 , CP , PP , VSP , VEP )
   * CV 타입의 발음 항목을 추가합니다.

* #### add_VX( 오디오 파일이름 , 발음기호 , 피치 , SP , EP )
   * V_X 타입의 발음 항목을 추가합니다.
   * 발음기호를 반드시 'A_B'와 같은 형태로 입력해주세요.

* #### add_INDIE( 오디오 파일이름 , 발음기호 , 피치 , SP , EP )
   * INDIE 타입의 발음 항목을 추가합니다.


### 발음 항목 수정 계열

* #### edit_CV( 발음기호 , 피치 , CP , PP , VSP , VEP )
   * CV 타입인 입력한 발음에 해당하는 항목의 마커 시간을 변경합니다.

* #### edit_VX( 발음기호 , 피치 , SP , EP )
   * V_X 타입인 입력한 발음에 해당하는 항목의 마커 시간을 변경합니다.
   * 발음기호를 반드시 'A_B'와 같은 형태로 입력해주세요.

* #### edit_INDIE( 발음기호 , 피치 , SP , EP )
   * INDIE 타입인 입력한 발음에 해당하는 항목의 마커 시간을 변경합니다.

* #### rename( 대상 발음기호, 대상 피치, 새 발음기호, 새 피치 )
   * 입력한 발음 항목의 오디오 파일 이름, 발음 타입, 마커 시간을 유지한 채 발음기호와 피치를 변경합니다.
   * 바꿀 기존 항목의 발음기호와 피치를 각각 '대상 발음기호/대상 피치'에, 바꿀 새 발음기호와 피치를 각각 '새 발음기호/새 피치'에 입력합니다.

* #### copy( 대상 발음기호, 대상 피치 , 새 발음기호, 새 피치 )
   * 입력한 발음 항목의 오디오 파일 이름, 발음 타입, 마커 시간을 복사해 다른 발음 항목에 붙여넣기합니다.   
   붙여넣을 발음 항목이 존재하지 않으면 입력한 발음 항목의 오디오 파일 이름, 발음 타입, 마커 시간을 가진 새 항목을 생성합니다.
   * 데이터를 복사할 항목의 발음기호와 피치를 각각 '대상 발음기호/대상 피치'에, 데이터를 붙여넣을 발음기호와 피치를 각각 '새 발음기호/새 피치'에 입력합니다.

* #### delete( 대상 발음기호 , 대상 피치 )
   * 입력한 발음 항목을 삭제합니다.


## 모듈 오리지널 메소드(?)
Voice Config에 없는 모듈 오리지널 기능의 메소드입니다.

### 일괄 수정 계열

* #### replace_pitch( 대상 피치 , 새 피치 )
   * 특정 피치인 발음 항목 전부 피치를 변경합니다.
   * 바꿀 기존 피치를 '대상 피치'에, 바꿀 새 피치를 '새 피치'에 입력합니다.

- - -
# 여러정보

## 개발 환경
* 운영체제 : Windows 10 Home
* 파이썬 버전 : 3.9

## 업데이트 내역
* #### 2021-08-28
   * 배포 시작
