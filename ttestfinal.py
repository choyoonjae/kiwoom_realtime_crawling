import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from testing import *  # kiwoom.py에 해당
import time
import pandas as pd
import numpy as np
from pandas import DataFrame as df
import pickle
from datetime import date


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kiwoomconnect()
        self.kiwoom.res_set_real("1001")  #####실시간 연결 시작
        print("connection complete")

    def kiwoomconnect(self):
        self.kiwoom = Kiwoom()
        self.kiwoom._comm_connect()
        self.kiwoom.OnReceiveRealData.connect(self.real_check)

    # 이벤트 처리하는곳
    def real_check(self, sRealKey, sRealType, sRealData):
        if self.kiwoom._get_comm_real_data(sRealKey, 43) != '':
            b = sRealKey, self.kiwoom._get_comm_real_data(sRealKey, 21), self.kiwoom._get_comm_real_data(sRealKey, 13), \
                self.kiwoom._get_comm_real_data(sRealKey, 50), self.kiwoom._get_comm_real_data(sRealKey, 70), self.kiwoom._get_comm_real_data(sRealKey, 49), \
                self.kiwoom._get_comm_real_data(sRealKey, 69), self.kiwoom._get_comm_real_data(sRealKey, 48), self.kiwoom._get_comm_real_data(sRealKey, 68), \
                self.kiwoom._get_comm_real_data(sRealKey, 47), self.kiwoom._get_comm_real_data(sRealKey, 67), self.kiwoom._get_comm_real_data(sRealKey, 46), \
                self.kiwoom._get_comm_real_data(sRealKey, 66), self.kiwoom._get_comm_real_data(sRealKey, 45), self.kiwoom._get_comm_real_data(sRealKey, 65), \
                self.kiwoom._get_comm_real_data(sRealKey, 44), self.kiwoom._get_comm_real_data(sRealKey, 64), self.kiwoom._get_comm_real_data(sRealKey, 43), \
                self.kiwoom._get_comm_real_data(sRealKey, 63), self.kiwoom._get_comm_real_data(sRealKey, 42), self.kiwoom._get_comm_real_data(sRealKey, 62), \
                self.kiwoom._get_comm_real_data(sRealKey, 41), self.kiwoom._get_comm_real_data(sRealKey, 61), self.kiwoom._get_comm_real_data(sRealKey, 51), \
                self.kiwoom._get_comm_real_data(sRealKey, 71), self.kiwoom._get_comm_real_data(sRealKey, 52), self.kiwoom._get_comm_real_data(sRealKey, 72), \
                self.kiwoom._get_comm_real_data(sRealKey, 53), self.kiwoom._get_comm_real_data(sRealKey, 73), self.kiwoom._get_comm_real_data(sRealKey, 54), \
                self.kiwoom._get_comm_real_data(sRealKey, 74), self.kiwoom._get_comm_real_data(sRealKey, 55), self.kiwoom._get_comm_real_data(sRealKey, 75), \
                self.kiwoom._get_comm_real_data(sRealKey, 56), self.kiwoom._get_comm_real_data(sRealKey, 76), self.kiwoom._get_comm_real_data(sRealKey, 57), \
                self.kiwoom._get_comm_real_data(sRealKey, 77), self.kiwoom._get_comm_real_data(sRealKey, 58), self.kiwoom._get_comm_real_data(sRealKey, 78), \
                self.kiwoom._get_comm_real_data(sRealKey, 59), self.kiwoom._get_comm_real_data(sRealKey, 79), self.kiwoom._get_comm_real_data(sRealKey, 60), \
                self.kiwoom._get_comm_real_data(sRealKey, 80)

            np.set_printoptions(linewidth=np.inf)
            b = np.array(b)

            if b[:1] == ('091990'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('215600'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('035760'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('084990'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('003670'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('086900'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('028300'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('253450'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('263750'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('025980'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('068760'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('034230'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('036490'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('078340'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('145020'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('095700'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('056190'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('046890'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('041960'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('028150'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('003380'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('098460'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('041510'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('042000'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('192080'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('035900'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('178920'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('022100'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('036830'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('038540'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('048260'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('240810'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('102940'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('000250'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('066970'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('122870'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('183490'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('214370'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('140410'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('058470'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('086520'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('036420'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('092040'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('083790'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('069080'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('200230'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('030190'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('073070'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('007390'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('267980'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('112040'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('108320'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('052020'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('200130'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('045390'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('078160'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('218410'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('115450'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('064760'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('039200'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('031390'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('038500'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('023410'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('243070'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('067630'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('039030'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('065660'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('086450'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('091700'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('080160'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('090460'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('141080'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('058820'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('053800'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('096530'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('144510'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('067160'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('049950'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('006730'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('005290'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('035600'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('033290'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('068240'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('084110'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('039840'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('082270'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('108230'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('010170'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('215200'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('060570'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('272290'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('029960'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('053030'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('067080'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('051500'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('035810'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('025770'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('063080'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('213420'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            elif b[:1] == ('237690'):
                basket1 = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                print('%s' % sRealKey, basket1)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + sRealKey + '_' + today.isoformat() + '.txt', 'a')
                f1.write(basket1 + '\n')
                f1.close()

            else:
                print('wrong case occurred')
                ttest = np.array2string(b)
                np.set_printoptions(linewidth=np.inf)  # 데이터 한줄로 만들기
                # print('%s' % sRealKey, ttest)
                today = date.today()
                f1 = open('C:/Users/CHO/Desktop/stockdata/' + 'wrongcase_' + today.isoformat() + '.txt', 'a')
                f1.write(ttest + '\n')
                f1.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()