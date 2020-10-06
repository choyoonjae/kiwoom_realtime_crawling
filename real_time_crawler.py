import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
import time

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnReceiveRealData.connect(self._receive_real_data)
        self.OnEventConnect.connect(self._event_connect)

    def _comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop=QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self,err_code):
        if err_code==0:
            print("connected")
        else:
            print("disconnected")
        self.login_event_loop.exit()

    def _get_connect_state(self):
        ret=self.dynamicCall("GetConnectState()")
        return ret

# processing the event
    def _receive_real_data(self, sRealKey, sRealType, sRealData):
        pass

# define basic function
    def _get_comm_real_data(self,strRealType,nFid):
        ret=self.dynamicCall("GetCommRealData(QString,int)",strRealType,nFid)

        return ret.strip()


    def _set_real_reg(self, strScreenNo, strCodeList, strFidList, strRealType):
        ret=self.dynamicCall("SetRealReg(QString,QString,QString,QString)", strScreenNo, strCodeList, strFidList,strRealType)
        return ret

    def _set_real_remove(self,strScrNo,strDelCode):
        ret=self.dynamicCall("SetRealRemove(QString,QString)",strScrNo,strDelCode)
        return ret

# define the receiving data  e.g. self._set_real_reg(ScrNo, "jongmok1;jongmok2;...jongmokN", "column1;column2;...comlumnK", "0")
    def res_set_real(self,ScrNo):
        ret =self._set_real_reg(ScrNo, "091990;215600;035760;084990;003670;086900;028300;253450;263750;025980;068760;034230;036490;078340;145020;095700;056190;046890;041960;028150;003380;098460;041510;042000;192080;035900;178920;022100;036830;038540;048260;240810;102940;000250;066970;122870;183490;214370;140410;058470;086520;036420;092040;083790;069080;200230;030190;073070;007390;267980;112040;108320;052020;200130;045390;078160;218410;115450;064760;039200;031390;038500;023410;243070;067630;039030;065660;086450;091700;080160;090460;141080;058820;053800;096530;144510;067160;049950;006730;005290;035600;033290;068240;084110;039840;082270;108230;010170;215200;060570;272290;029960;053030;067080;051500;035810;025770;063080;213420;237690"
, "13;50;70;49;69;48;68;47;67;46;66;45;65;44;64;43;63;42;62;41;61;51;71;52;72;53;73;54;74;55;75;56;76;57;77;58;78;59;79;60;80", "0")
        
        return ret
