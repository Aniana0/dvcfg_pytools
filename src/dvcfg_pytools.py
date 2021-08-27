# -*- author: 아니아나(Aniana0) aniana0gm@gmail.com -*-
# -*- coding : utf-8 -*-
# -*- latest update date : 2021-08-26 -*-
 
import json
import time
import re

tm=time.localtime(time.time())

class Dvcfg:

    # 초기값 - 빈 딕셔너리 | Initial dvcfg - empty dictionary --------------------
    
    def __init__(self):
        self.dvcfg_dict={}
        
        # start_blank = 툴박스 마커 에디터에서 시작 지점에 있는 노란 영역의 길이
        # start_blank = Length of yellow area at start point in ToolBox Marker Editor
        self.start_blank=0.05999999865889549



    # .dvcfg 불러오기 | Load .dvcfg --------------------
    
    def load(self,file_name):
        with open(file_name,'r',encoding='utf-8') as f:
            self.dvcfg_dict=json.load(f)

        ##작동확인용 메시지
        ##print('{0}을 불러왔습니다'.format(file_name))


    # .dvcfg 저장하기 | Save .dvcfg --------------------
    
    def save(self,file_name):
        if file_name=='':
            file_name='voice.dvcfg'
        else:
            pass
        with open(file_name,'w',encoding='utf-8') as f:
            json.dump(self.dvcfg_dict,f,indent=3)

        ##작동확인용 메시지 
        ##print('{0}에 저장했습니다'.format(file_name))


    # 입력한 딕셔너리를 dvcfg 딕셔너리로 설정 | Set inputted dictionary to dvcfg dictionary --------------------
    def dict_to_dvcfg(self,input_dict):
        self.dvcfg_dict=input_dict


    # 현재 dvcfg 딕셔너리를 반환 | Return dvcfg dictionary --------------------
    def dvcfg_dict(self):
        return self.dvcfg_dict



# -------------------- 파라미터 추가 | Add parameter --------------------

    # 파라미터 추가 - CV | Add parameter - Type: CV --------------------
    def add_CV(self,wav_name,symbol,pitch,cp,pp,vsp,vep):
        parameter_name="{0}->{1}".format(pitch,symbol)
        startTime=cp-self.start_blank
        self.dvcfg_dict[parameter_name]={}
        self.dvcfg_dict[parameter_name]["wavName"]=wav_name
        self.dvcfg_dict[parameter_name]["srcType"]="CV"
        self.dvcfg_dict[parameter_name]["symbol"]=symbol
        self.dvcfg_dict[parameter_name]["pitch"]=pitch
        self.dvcfg_dict[parameter_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
        self.dvcfg_dict[parameter_name]["connectPoint"]=self.start_blank
        self.dvcfg_dict[parameter_name]["startTime"]=startTime
        self.dvcfg_dict[parameter_name]["endTime"]=vep+self.start_blank
        self.dvcfg_dict[parameter_name]["preutterance"]=pp-startTime
        self.dvcfg_dict[parameter_name]["vowelStart"]=vsp-startTime
        self.dvcfg_dict[parameter_name]["vowelEnd"]=vep-startTime
        self.dvcfg_dict[parameter_name]["tailPoint"]=vep-startTime+0.054999998658895

        
    # 파라미터 추가 - V_X | Add parameter - Type: V_X --------------------
    def add_VX(self,wav_name,symbol,pitch,sp,ep):
        if re.search('.*_.*',symbol):
            parameter_name="{0}->{1}".format(pitch,symbol)
            startTime=sp-self.start_blank
            self.dvcfg_dict[parameter_name]={}
            self.dvcfg_dict[parameter_name]["wavName"]=wav_name
            self.dvcfg_dict[parameter_name]["srcType"]="VX"
            self.dvcfg_dict[parameter_name]["symbol"]=symbol
            self.dvcfg_dict[parameter_name]["pitch"]=pitch
            self.dvcfg_dict[parameter_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
            self.dvcfg_dict[parameter_name]["connectPoint"]=self.start_blank
            self.dvcfg_dict[parameter_name]["startTime"]=startTime
            self.dvcfg_dict[parameter_name]["endTime"]=ep+self.start_blank
            self.dvcfg_dict[parameter_name]["tailPoint"]=ep-startTime
        else:
            print('기호 오류: 입력된 기호가 V_X 형식이 아닙니다. "A_B"와 같은 형태로 입력해주십시오.\nSymbol Error: The symbol you entered is not V_X. Please enter the symbol as follows: "A_B"')


    # 파라미터 추가 - 독립기호(Independent) | Add parameter - Type: Independent --------------------
    def add_INDIE(self,wav_name,symbol,pitch,sp,ep):
        parameter_name="{0}->{1}".format(pitch,symbol)
        startTime=sp-self.start_blank
        self.dvcfg_dict[parameter_name]={}
        self.dvcfg_dict[parameter_name]["wavName"]=wav_name
        self.dvcfg_dict[parameter_name]["srcType"]="INDIE"
        self.dvcfg_dict[parameter_name]["symbol"]=symbol
        self.dvcfg_dict[parameter_name]["pitch"]=pitch
        self.dvcfg_dict[parameter_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
        self.dvcfg_dict[parameter_name]["startPoint"]=self.start_blank
        self.dvcfg_dict[parameter_name]["endPoint"]=ep-startTime
        self.dvcfg_dict[parameter_name]["startTime"]=startTime
        self.dvcfg_dict[parameter_name]["endTime"]=ep+self.start_blank



# -------------------- 마커 값 변경 | Edit Markers --------------------

    # 마커 값 변경 - CV | Edit Markers - Type: CV --------------------
    def edit_CV(self,symbol,pitch,cp,pp,vsp,vep):
        parameter_name="{0}->{1}".format(pitch,symbol)
        if parameter_name in self.dvcfg_dict:
            if self.dvcfg_dict[parameter_name]["srcType"]=="CV":
                startTime=cp-self.start_blank
                self.dvcfg_dict[parameter_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
                self.dvcfg_dict[parameter_name]["connectPoint"]=self.start_blank
                self.dvcfg_dict[parameter_name]["startTime"]=startTime
                self.dvcfg_dict[parameter_name]["endTime"]=vep+self.start_blank
                self.dvcfg_dict[parameter_name]["preutterance"]=pp-startTime
                self.dvcfg_dict[parameter_name]["vowelStart"]=vsp-startTime
                self.dvcfg_dict[parameter_name]["vowelEnd"]=vep-startTime
                self.dvcfg_dict[parameter_name]["tailPoint"]=vep-startTime+0.054999998658895
            else:
                print("타입 오류: 이 파라미터는 CV가 아닙니다.\nType Error: The parameter's type is not CV.")
        else:
            print('파라미터 오류: 파라미터가 존재하지 않습니다.\nParameter Error: Parameter is not exist.')


    # 마커 값 변경 - V_X | Edit Markers - Type: V_X --------------------
    def edit_VX(self,symbol,pitch,sp,ep):
        if re.search('.*_.*',symbol):
            parameter_name="{0}->{1}".format(pitch,symbol)
            if parameter_name in self.dvcfg_dict:
                if self.dvcfg_dict[parameter_name]["srcType"]=="VX":
                    startTime=sp-self.start_blank
                    self.dvcfg_dict[parameter_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
                    self.dvcfg_dict[parameter_name]["connectPoint"]=self.start_blank
                    self.dvcfg_dict[parameter_name]["startTime"]=startTime
                    self.dvcfg_dict[parameter_name]["endTime"]=ep+self.start_blank
                    self.dvcfg_dict[parameter_name]["tailPoint"]=ep-startTime
                else:
                    print("타입 오류: 이 파라미터는 V_X가 아닙니다.\nType Error: The parameter's type is not V_X.")
            else:
                print('파라미터 오류: 파라미터가 존재하지 않습니다.\nParameter Error: Parameter is not exist.')
        else:
            print('기호 오류: 입력된 기호가 V_X 형식이 아닙니다. "A_B"와 같은 형태로 입력해주십시오.\nSymbol Error: The symbol you entered is not V_X. Please enter the symbol as follows: "A_B"')


    # 마커 값 변경 - 독립기호(Independent) | Edit Markers - Type: Independent --------------------
    def edit_INDIE(self,symbol,pitch,sp,ep):
        parameter_name="{0}->{1}".format(pitch,symbol)
        if parameter_name in self.dvcfg_dict:
            if self.dvcfg_dict[parameter_name]["srcType"]=="INDIE":
                startTime=sp-self.start_blank
                self.dvcfg_dict[parameter_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
                self.dvcfg_dict[parameter_name]["startPoint"]=self.start_blank
                self.dvcfg_dict[parameter_name]["endPoint"]=ep-startTime
                self.dvcfg_dict[parameter_name]["startTime"]=startTime
                self.dvcfg_dict[parameter_name]["endTime"]=ep+self.start_blank
            else:
                print("타입 오류: 이 파라미터는 INDIE가 아닙니다.\nType Error: The parameter's type is not INDIE.")
        else:
            print('파라미터 오류: 파라미터가 존재하지 않습니다.\nParameter Error: Parameter is not exist.')



# -------------------- 파라미터 수정 | Edit Parameters --------------------

    # 기호, 피치 변경 | Rename symbol and pitch --------------------
    def rename(self,original_symbol,original_pitch,new_symbol,new_pitch):
        original_parameter="{0}->{1}".format(original_pitch,original_symbol)
        new_parameter="{0}->{1}".format(new_pitch,new_symbol)
        self.dvcfg_dict[new_parameter]=self.dvcfg_dict[original_parameter].copy()
        del(self.dvcfg_dict[original_parameter])
        self.dvcfg_dict[new_parameter]["symbol"]=new_symbol
        self.dvcfg_dict[new_parameter]["pitch"]=new_pitch
        self.dvcfg_dict[new_parameter]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)


    # 파라미터 복사 | Copy parameter --------------------
    def copy(self,original_symbol,original_pitch,new_symbol,new_pitch):
        original_parameter="{0}->{1}".format(original_pitch,original_symbol)
        new_parameter="{0}->{1}".format(new_pitch,new_symbol)
        self.dvcfg_dict[new_parameter]=self.dvcfg_dict[original_parameter].copy()
        self.dvcfg_dict[new_parameter]["symbol"]=new_symbol
        self.dvcfg_dict[new_parameter]["pitch"]=new_pitch
        self.dvcfg_dict[new_parameter]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)


    # 파라미터 삭제 | Delete parameter --------------------
    def delete(self,symbol,pitch):
        del(self.dvcfg_dict["{0}->{1}".format(pitch,symbol)])



# ---------------------------------------- 오리지널 기능 | Features that do not exist in the ToolBox ----------------------------------------

# -------------------- 일괄 수정 | Replace all --------------------

    # 피치 일괄 변경 | Replace all pitch -------------------------
    def replace_pitch(self,original_pitch,new_pitch):
        for line in list(self.dvcfg_dict.keys()):
            if self.dvcfg_dict[line]["pitch"]==original_pitch:
                new_parameter="{0}->{1}".format(new_pitch,self.dvcfg_dict[line]["symbol"])
                self.dvcfg_dict[new_parameter]=self.dvcfg_dict[line].copy()
                self.dvcfg_dict[new_parameter]["pitch"]=new_pitch
                self.dvcfg_dict[new_parameter]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
                del(self.dvcfg_dict[line])




# -------------------- 작동 확인용 | module test code --------------------
if __name__=='__main__':
    test=Dvcfg()
    test.load('voice.dvcfg')
    print(test.dvcfg_to_dict())
    
    test.add_CV("iy.wav","ya","C4",1.0,1.2,1.3,1.5)
    test.add_VX("iy.wav","i_y","C4",1.0,1.2)
    test.add_INDIE("iy.wav","aaaa","C4",1.0,1.5)

    test.copy("ya","C4","ye","C4")
    test.copy("i_y","C4","i_yy","C4")
    test.copy("aaaa","C4","bbbb","C4")

    test.rename("ye","C4","yeo","C#4")
    test.rename("i_yy","C4","i_yyy","C#4")
    test.rename("bbbb","C4","cccc","C#4")

    test.delete('a','F4')

    test.edit_CV("yeo","C#4",2.0,2.2,2.3,2.5)
    test.edit_VX("i_yyy","C#4",2.0,2.2)
    test.edit_INDIE("cccc","C#4",3.0,3.5)

    test.replace_pitch('F4','E4')

    test.save('voice2.dvcfg')
