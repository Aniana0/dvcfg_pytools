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

```   
## 메소드
