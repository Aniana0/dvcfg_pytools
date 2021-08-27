# voice.dvcfg 작성/수정을 위한 파이썬 모듈
### voice.dvcfg란?   
DeepVocal의 음성 라이브러리를 제작할 때 필요한 파일로, 오디오 샘플에서 각 발음의 음소가 위치한 시간이 기록되어 있습니다.   
(UTAU의 oto.ini와 역할이 비슷하다고 볼 수 있습니다)
   
## dvcfg_pytools   
voice.dvcfg를 파이썬에서 편하게 수정하기 위해 만든 모듈입니다.   
DeepVocal ToolBox의 'Voice Config'에서 할 수 있는 작업을 파이썬에서도 할 수 있도록 만들었습니다.   
그 외에 음성 라이브러리를 제작할 때 자주 필요할 것 같은 기능도 추가하고 있습니다.   
   
#### 주의사항(?)     
제작자가 코딩을 학교 교양강의에서 매우 기초만 살짝 배우고 나머지는 독학으로 배운 사람입니다...   
따라서 용어를 잘못 사용하거나 설명이 이상할 수도 있습니다...
- - -
## 설치
(준비중)
## 사용법   
dvcfg_pytools 모듈을 불러온 다음, Dvcfg 클래스를 이용해 객체를 생성합니다.
```Python
import dvcfg_pytools   
   
dvcfg_file = dvcfg_pytools.Dvcfg()
```   
이후 메소드를 이용해 원하는 작업합니다
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
## 용어
이 문서에서 일부 단어는 아래와 같은 의미로 사용됩니다.
#### 파라미터
voice.dvcfg에 저장되어 있는 발음 설정값 항목의 정식 명칭을 모르겠어서(...) 대충 파라미터라고 부르고 있습니다.


## 기본 메소드(툴박스 기능)
### load(파일 이름)   
voice.dvcfg 파일에서 파라미터 데이터를 읽어들입니다.   
   
### save(파일 이름='voice.dvcfg')
voice.dvcfg 파일을 저장합니다.
아무것도 입력하지 않으면 'voice.dvcfg'로 저장합니다.   
   
### dict_to_dvcfg(딕셔너리)
입력한 딕셔너리를 객체의 voice.dvcfg 데이터로 지정합니다.

### dvcfg_to_dict()
객체에 저장된 현재의 voice.dvcfg 데이터를 딕셔너리로 반환합니다.
