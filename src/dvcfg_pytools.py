# -*- author: 아니아나(Aniana0) aniana0gm@gmail.com -*-
# -*- coding : utf-8 -*-
# -*- latest update date(KST) : 2021-08-31 15:50 -*-
 
import json
import time
import re
import os.path

tm=time.localtime(time.time())

class Dvcfg:

    # 시작 | Start --------------------
    def __init__(self,file_name=''):
        # start_blank = 툴박스 마커 에디터에서 시작 지점에 있는 노란 영역의 길이
        # start_blank = Length of yellow area at start point in ToolBox Marker Editor
        self.start_blank=0.05999999865889549

        # 초기값 - 빈 딕셔너리 | Initial dvcfg - empty dictionary
        if os.path.isfile(file_name):
            self.load(file_name)
        else:
            self.dvcfg_dict={}


# -------------------- 안내 메시지용 | Print message --------------------

    # V_X가 아닐 때 | If symbol is not V_X --------------------
    def __messageError_notVX(self,symbol):
        print ('기호 오류: 입력된 기호({0})가 V_X 형식이 아닙니다. "A_B"와 같은 형태로 입력해주십시오.\n'.format(symbol),
               'Symbol Error: The symbol({0}) is not V_X. Please enter the symbol as follows: "A_B"\n'.format(symbol))

    # 타입이 틀렸을 때 | If symbol type is wrong --------------------
    def __messageError_type(self,item_name,symbol_type):
        print ('타입 오류: {0}의 타입이 {1}가 아닙니다.\n'.format(item_name,symbol_type),
               "Type Error: The item({0})'s type is not {1}.\n".format(item_name,symbol_type))
        
    # 항목이 존재하지 않을 때 | If item is not exist --------------------
    def __messageError_item(self,item_name):
        print ('항목 오류: {0}에 해당하는 항목이 존재하지 않습니다.\n'.format(item_name),
               'Item Error: {0} is not exist.\n'.format(item_name))

    # 마커 값이 잘못 됐을 때 | If markers is wrong --------------------
    def __messageError_markers(self,item_name):
        print ('마커 오류: {0}의 마커 설정이 잘못 되었습니다.\n'.format(item_name),
               "Markers Error: {0}'s is wrong.\n".format(item_name))


# -------------------- 파일 & 데이터 | File & data --------------------

    # .dvcfg 불러오기 | Load .dvcfg --------------------
    
    def load(self,file_name):
        
        if os.path.isfile(file_name):

            with open(file_name,'r',encoding='utf-8') as f:
                self.dvcfg_dict=json.load(f)

            ##작동확인용 메시지
            ##print('{0}을 불러왔습니다'.format(file_name))

        else:
            self.dvcfg_dict={}


    # .dvcfg 저장하기 | Save .dvcfg --------------------
    
    def save(self,file_name='voice.dvcfg'):
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
    def dvcfg_to_dict(self):
        return self.dvcfg_dict.copy()


    # CV 타입 항목의 마커 시간을 반환 | Return item(Type: CV)'s markers times --------------------
    def markers_CV(self,symbol,pitch,mode='dict'):
        item_name="{0}->{1}".format(pitch,symbol)

        if item_name in self.dvcfg_dict:
            
            if self.dvcfg_dict[item_name]["srcType"]=="CV":
                
                cp = self.dvcfg_dict[item_name]["startTime"] + self.dvcfg_dict[item_name]["connectPoint"]
                pp = self.dvcfg_dict[item_name]["startTime"] + self.dvcfg_dict[item_name]["preutterance"]
                vsp = self.dvcfg_dict[item_name]["startTime"] + self.dvcfg_dict[item_name]["vowelStart"]
                vep = self.dvcfg_dict[item_name]["startTime"] + self.dvcfg_dict[item_name]["vowelEnd"]

                if mode=='dict':
                    return {'cp':cp,'pp':pp,'vsp':vsp,'vep':vep}
                elif mode=='tuple':
                    return (cp,pp,vsp,vep)
                else:
                    return {'cp':cp,'pp':pp,'vsp':vsp,'vep':vep}

            else:
                self.__messageError_type(item_name,"CV")
                
        else:
            self.__messageError_item(item_name)


    # V_X 타입 항목의 마커 시간을 반환 | Return item(Type: VX)'s markers times --------------------
    def markers_VX(self,symbol,pitch,mode='dict'):
        if re.search('.*_.*',symbol):
            item_name="{0}->{1}".format(pitch,symbol)

            if item_name in self.dvcfg_dict:

                if self.dvcfg_dict[item_name]["srcType"]=="VX":
                    
                    sp = self.dvcfg_dict[item_name]["startTime"] + self.dvcfg_dict[item_name]["connectPoint"]
                    ep = self.dvcfg_dict[item_name]["startTime"] + self.dvcfg_dict[item_name]["tailPoint"]

                    if mode=='dict':
                        return {'sp':sp,'ep':ep}
                    elif mode=='tuple':
                        return (sp,ep)
                    else:
                        return {'sp':sp,'ep':ep}

                else:
                    self.__messageError_type(item_name,"VX")
                
            else:
                self.__messageError_item(item_name)
                
        else:
            self.__messageError_notVX(symbol)


    # INDIE 타입 항목의 마커 시간을 반환 | Return item(Type: INDIE)'s markers times --------------------
    def markers_INDIE(self,symbol,pitch,mode='dict'):
        item_name="{0}->{1}".format(pitch,symbol)
        
        if item_name in self.dvcfg_dict:

            if self.dvcfg_dict[item_name]["srcType"]=="INDIE":

                sp = self.dvcfg_dict[item_name]["startTime"] + self.dvcfg_dict[item_name]["startPoint"]
                ep = self.dvcfg_dict[item_name]["startTime"] + self.dvcfg_dict[item_name]["endPoint"]

                if mode=='dict':
                    return {'sp':sp,'ep':ep}
                elif mode=='tuple':
                    return (sp,ep)
                else:
                    return {'sp':sp,'ep':ep}

            else:
                self.__messageError_type(item_name,"INDIE")

        else:
            self.__messageError_item(item_name)

            
# -------------------- 발음 항목 추가 | Add symbol item --------------------

    # 항목 추가 - CV | Add item - Type: CV --------------------
    def add_CV(self,wav_name,symbol,pitch,cp,pp,vsp,vep):
        item_name="{0}->{1}".format(pitch,symbol)

        if self.start_blank < cp < pp < vsp < vep:
            connectPoint = self.start_blank
            startTime = cp - connectPoint
            self.dvcfg_dict[item_name] = {}
            self.dvcfg_dict[item_name]["wavName"] = wav_name
            self.dvcfg_dict[item_name]["srcType"] = "CV"
            self.dvcfg_dict[item_name]["symbol"] = symbol
            self.dvcfg_dict[item_name]["pitch"] = pitch
            self.dvcfg_dict[item_name]["updateTime"] = time.strftime('%Y-%m-%d %H:%M:%S',tm)
            self.dvcfg_dict[item_name]["connectPoint"] = connectPoint
            self.dvcfg_dict[item_name]["startTime"] = startTime
            self.dvcfg_dict[item_name]["endTime"] = vep + connectPoint
            self.dvcfg_dict[item_name]["preutterance"] = pp - startTime
            self.dvcfg_dict[item_name]["vowelStart"] = vsp - startTime
            self.dvcfg_dict[item_name]["vowelEnd"] = vep - startTime
            self.dvcfg_dict[item_name]["tailPoint"] = vep - startTime + 0.054999998658895

        else:
            self.__messageError_markers(item_name)

        
    # 항목 추가 - V_X | Add item - Type: V_X --------------------
    def add_VX(self,wav_name,symbol,pitch,sp,ep):
        if re.search('.*_.*',symbol):
            item_name="{0}->{1}".format(pitch,symbol)

            if self.start_blank < sp < ep:
                connectPoint = self.start_blank
                startTime = sp - connectPoint
                self.dvcfg_dict[item_name]={}
                self.dvcfg_dict[item_name]["wavName"]=wav_name
                self.dvcfg_dict[item_name]["srcType"]="VX"
                self.dvcfg_dict[item_name]["symbol"]=symbol
                self.dvcfg_dict[item_name]["pitch"]=pitch
                self.dvcfg_dict[item_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
                self.dvcfg_dict[item_name]["connectPoint"] = connectPoint
                self.dvcfg_dict[item_name]["startTime"] = startTime
                self.dvcfg_dict[item_name]["endTime"] = ep + connectPoint
                self.dvcfg_dict[item_name]["tailPoint"] = ep - startTime

            else:
                self.__messageError_markers(item_name)
                
        else:
            self.__messageError_notVX(symbol)


    # 항목 추가 - 독립기호(Independent) | Add item - Type: Independent --------------------
    def add_INDIE(self,wav_name,symbol,pitch,sp,ep):
        item_name="{0}->{1}".format(pitch,symbol)

        if self.start_blank < sp < ep:
            startPoint = self.start_blank
            startTime = sp - startPoint
            self.dvcfg_dict[item_name]={}
            self.dvcfg_dict[item_name]["wavName"]=wav_name
            self.dvcfg_dict[item_name]["srcType"]="INDIE"
            self.dvcfg_dict[item_name]["symbol"]=symbol
            self.dvcfg_dict[item_name]["pitch"]=pitch
            self.dvcfg_dict[item_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
            self.dvcfg_dict[item_name]["startPoint"]=startPoint
            self.dvcfg_dict[item_name]["endPoint"] = ep - startTime
            self.dvcfg_dict[item_name]["startTime"] = startTime
            self.dvcfg_dict[item_name]["endTime"] = ep + startPoint

        else:
            self.__messageError_markers(item_name)



# -------------------- 마커 값 변경 | Edit Markers --------------------

    # 마커 값 변경 - CV | Edit Markers - Type: CV --------------------
    def edit_CV(self,symbol,pitch,cp=0,pp=0,vsp=0,vep=0):
        item_name="{0}->{1}".format(pitch,symbol)
        
        if item_name in self.dvcfg_dict:
            
            if self.dvcfg_dict[item_name]["srcType"]=="CV":

                if cp == 0:
                    cp = markers_CV(symbol,pitch,'tuple')[0]
                if pp == 0:
                    pp = markers_CV(symbol,pitch,'tuple')[1]
                if vsp == 0:
                    vsp = markers_CV(symbol,pitch,'tuple')[2]
                if vep == 0:
                    vep = markers_CV(symbol,pitch,'tuple')[3]

                if self.start_blank<cp < pp < vsp < vep:
                    connectPoint = self.start_blank
                    startTime = cp - connectPoint
                    self.dvcfg_dict[item_name]["updateTime"] = time.strftime('%Y-%m-%d %H:%M:%S',tm)
                    self.dvcfg_dict[item_name]["connectPoint"] = connectPoint
                    self.dvcfg_dict[item_name]["startTime"] = startTime
                    self.dvcfg_dict[item_name]["endTime"] = vep + connectPoint
                    self.dvcfg_dict[item_name]["preutterance"] = pp - startTime
                    self.dvcfg_dict[item_name]["vowelStart"] = vsp - startTime
                    self.dvcfg_dict[item_name]["vowelEnd"] = vep - startTime
                    self.dvcfg_dict[item_name]["tailPoint"] = vep - startTime + 0.054999998658895

                else:
                    self.__messageError_markers(item_name)
                
            else:
                self.__messageError_type(item_name,"CV")
                
        else:
            self.__messageError_item(item_name)


    # 마커 값 변경 - V_X | Edit Markers - Type: V_X --------------------
    def edit_VX(self,symbol,pitch,sp=0,ep=0):
        if re.search('.*_.*',symbol):
            item_name="{0}->{1}".format(pitch,symbol)
            
            if item_name in self.dvcfg_dict:
                
                if self.dvcfg_dict[item_name]["srcType"]=="VX":

                    if sp == 0:
                        sp = markers_VX(symbol,pitch,'tuple')[0]
                    if ep == 0:
                        ep = markers_VX(symbol,pitch,'tuple')[1]

                    if self.start_blank < sp < ep:
                        connectPoint = self.start_blank
                        startTime = sp - connectPoint
                        self.dvcfg_dict[item_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
                        self.dvcfg_dict[item_name]["connectPoint"] = connectPoint
                        self.dvcfg_dict[item_name]["startTime"]= startTime
                        self.dvcfg_dict[item_name]["endTime"] = ep + connectPoint
                        self.dvcfg_dict[item_name]["tailPoint"] = ep - startTime

                    else:
                        self.__messageError_markers(item_name)
                        
                else:
                    self.__messageError_type(item_name,"V_X")
                        
            else:
                self.__messageError_item(item_name)
                
        else:
            self.__messageError_notVX(symbol)


    # 마커 값 변경 - 독립기호(Independent) | Edit Markers - Type: Independent --------------------
    def edit_INDIE(self,symbol,pitch,sp=0,ep=0):
        item_name="{0}->{1}".format(pitch,symbol)
        
        if item_name in self.dvcfg_dict:
            
            if self.dvcfg_dict[item_name]["srcType"]=="INDIE":

                if sp == 0:
                    sp = markers_INDIE(symbol,pitch,'tuple')[0]
                if ep == 0:
                    ep = markers_INDIE(symbol,pitch,'tuple')[1]

                if self.start_blank < sp < ep:
                    startPoint = self.start_blank
                    startTime = sp - self.start_blank
                    self.dvcfg_dict[item_name]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
                    self.dvcfg_dict[item_name]["startPoint"] = startPoint
                    self.dvcfg_dict[item_name]["endPoint"] = ep - startTime
                    self.dvcfg_dict[item_name]["startTime"] = startTime
                    self.dvcfg_dict[item_name]["endTime"] = ep + startPoint

                else:
                    self.__messageError_markers(item_name)

            else:
                self.__messageError_type(item_name,"INDIE")
                
        else:
            self.__messageError_item(item_name)



# -------------------- 항목 수정 | Edit item --------------------

    # 기호, 피치 변경 | Rename symbol and pitch --------------------
    def rename(self,original_symbol,original_pitch,new_symbol,new_pitch):
        original_item="{0}->{1}".format(original_pitch,original_symbol)
        new_item="{0}->{1}".format(new_pitch,new_symbol)
        self.dvcfg_dict[new_item]=self.dvcfg_dict[original_item].copy()
        del(self.dvcfg_dict[original_item])
        self.dvcfg_dict[new_item]["symbol"]=new_symbol
        self.dvcfg_dict[new_item]["pitch"]=new_pitch
        self.dvcfg_dict[new_item]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)


    # 항목 복사 | Copy item --------------------
    def copy(self,original_symbol,original_pitch,new_symbol,new_pitch):
        original_item="{0}->{1}".format(original_pitch,original_symbol)
        new_item="{0}->{1}".format(new_pitch,new_symbol)
        self.dvcfg_dict[new_item]=self.dvcfg_dict[original_item].copy()
        self.dvcfg_dict[new_item]["symbol"]=new_symbol
        self.dvcfg_dict[new_item]["pitch"]=new_pitch
        self.dvcfg_dict[new_item]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)


    # 항목 삭제 | Delete item --------------------
    def delete(self,symbol,pitch):
        del(self.dvcfg_dict["{0}->{1}".format(pitch,symbol)])



# ---------------------------------------- 오리지널 기능 | Features that do not exist in the ToolBox ----------------------------------------

# -------------------- 일괄 수정 | Replace all --------------------

    # 피치 일괄 변경 | Replace all pitch -------------------------
    def replace_pitch(self,original_pitch,new_pitch):
        for item,data in list(self.dvcfg_dict.items()):
            if data["pitch"]==original_pitch:
                new_item="{0}->{1}".format(new_pitch,data["symbol"])
                self.dvcfg_dict[new_item]=data.copy()
                self.dvcfg_dict[new_item]["pitch"]=new_pitch
                self.dvcfg_dict[new_item]["updateTime"]=time.strftime('%Y-%m-%d %H:%M:%S',tm)
                del(self.dvcfg_dict[item])




# -------------------- 작동 확인용 | module test code --------------------
if __name__=='__main__':
    test=Dvcfg('test.dvcfg')
    test.load('voice.dvcfg')
    print(test.dvcfg_to_dict())
    
    test.add_CV("test.wav","ya","C4",1.0,1.2,1.3,1.5)
    test.add_VX("test.wav","a_y","C4",1.0,1.2)
    test.add_INDIE("test.wav","test","C4",1.0,1.5)

    test.copy("ya","C4","ya2","F4")
    test.copy("a_y","C4","a_y2","F4")
    test.copy("test","C4","test2","F4")

    test.rename("ya","C4","ya3","C#4")
    test.rename("a_y","C4","a_y3","C#4")
    test.rename("test","C4","test3","C#4")

    test.delete('test2','F4')

    test.edit_CV("ya3","C#4",2.0,2.2,2.3,2.5)
    test.edit_VX("a_y3","C#4",2.0,2.2)
    test.edit_INDIE("test3","C#4",3.0,3.5)

    test.replace_pitch('F4','E4')

    print(test.markers_CV('ya2',"E4"))
    print(test.markers_VX('a_y2',"E4",'tuple'))
    print(test.markers_INDIE('test3',"C#4",'dict'))

    test.save()
