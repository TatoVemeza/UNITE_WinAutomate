#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  UNITE DEMO.py
#  
#  Copyright 2017 avelazcx <aldo.alfonsox.velasco.meza@intel.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import time
import sys,os
import pywinauto
import pyautogui
import unittest
from  datetime import datetime
from pywinauto import Desktop, Application
from pywinauto.controls.win32_controls import ButtonWrapper
from pywinauto.application import Application

class AdminPortalAutoTest(unittest.TestCase):
    print("   <========================== UNITE TEST ===========================>")
    print("   -------------------------------------------------------------------")
    print("""                                AVELAZCX
            """)

    def test_1_TCxxxx_Button_Close(self):
        self.app = Application(backend="uia").start("C:\Program Files (x86)\Intel\Intel Unite\Client\Intel Unite.exe")
        time.sleep(4)
        self.inteu = self.app.window(title_re= 'Intel Unite®')
##        self.pinentr = pyautogui.typewrite("782807")
##        time.sleep(5)
        self.button = self.inteu.window(auto_id='btnClose').click_input()

    def test_2_TCxxxx_Button_Close(self):
        self.app = Application(backend="uia").start("C:\Program Files (x86)\Intel\Intel Unite\Client\Intel Unite.exe")
        time.sleep(4)
##        self.inteu = self.app.window(title_re= 'Intel Unite®')
##        self.pinentr = pyautogui.typewrite("782807")
##        time.sleep(5)
##        self.button = self.inteu.window(auto_id='btnClose').click_input()




                
    def tearDown(self):
        # Muestra estado de la prueba....
        print("\n====== * Time Result * =======", datetime.now())

 
if __name__ == '__main__':
    print("\t\t     ==== Test in progress ====\n")    
    unittest.main(verbosity=2)
    
