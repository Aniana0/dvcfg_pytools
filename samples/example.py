# -*- coding : utf-8 -*-

import dvcfg_pytools   
   
dvcfg_file = dvcfg_pytools.Dvcfg()


# 실험용 파일을 로드 | Load voice.dvcfg for test
dvcfg_file.load('original_voice.dvcfg')


# 잘못 된 마커 편집 | Edit markers
dvcfg_file.edit_CV('ga','C#4',1.045,1.062,1.12,1.34)
dvcfg_file.edit_VX('a_a','F4',7.0,7.1)

# 숨소리 파라미터 추가
dvcfg_file.add_INDIE('voice/breath.wav','breath','C#4',0.55,1.07)


# 파일 저장 | Save voice.dvcfg
dvcfg_file.save('')
