# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:51:05 2021

@author: HP
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from entree import Ui_MainWindow  #importation de fenetre entree
from jeu import Ui_MainWindow as windowGame #importation de fenetre jeu
from Main import Ui_MainWindow as windowRule #importation de fenetre des regles
from Portfolio import Ui_Dialog as windowDev #importation de fenetre du portfolio
from error import Ui_Dialog as windowErreur #importation de fenetre en cas d'erreur
from error import Ui_Dialog as windowWin #importation de fenetre win
from FinPartie import Ui_Dialog as windowEnd #importation de fenetre end
from structure import Joueur

import sys

def afficherErreur():
    Erreur.show()

def afficherRule():
    global joueur1
    global joueur2
    global nombre
    global compteur
    
    nom1= ui.lineEdit_2.text()
    nom2= ui.lineEdit.text()
    nombre=int(ui.spinBox.text())
    if nom1=="" or nom2=="" :
        Erreur.show()
    else :    
        MainWindow.hide()
        Rule.show()
        joueur1=Joueur(nom1,1)
        joueur2=Joueur(nom2,2)
        uiGame.label.setText("Au tour de "+joueur1.nom+" (cercle)")
        uiGame.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MV Boli\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:10px; margin-bottom:10px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">"+joueur1.nom+" "+str(joueur1.point)+"-"+str(joueur2.point)+" "+joueur2.nom+" </span></p></body></html>")
        uiGame.label_2.setText("Manche "+str(compteur))

tour=1 
case = [0]*10
compteur=1

#slots pour gerer les bouttons 
def changetour() :
    global tour
    if tour==1 :
        if joueur1.coup==0 :
            if compteur==nombre :
                uiEnd.label.setText("Match \n nul ")
                afficherEnd()
            else :
                uiWin.label.setText("Match nul")
                Win.show()
        else :
            tour=2
            uiGame.label.setText("Au tour de "+joueur2.nom+ "(croix)")
    else :
        tour=1
        uiGame.label.setText("Au tour de "+joueur1.nom+"(cercle)")

def showWin(rang):
    if case[1]==rang and case[2]==rang and case[3]==rang :
        return True
    if case[4]==rang and case[5]==rang and case[6]==rang :
        return True
    if case[7]==rang and case[8]==rang and case[9]==rang :
        return True
    if case[1]==rang and case[4]==rang and case[7]==rang :
        return True
    if case[2]==rang and case[5]==rang and case[8]==rang :
        return True
    if case[3]==rang and case[6]==rang and case[9]==rang :
        return True
    if case[1]==rang and case[5]==rang and case[9]==rang :
        return True
    if case[3]==rang and case[5]==rang and case[7]==rang :
        return True
    else :
        return False 
        
def afficherGame():
    Rule.hide()
    Game.show()
    
def afficherDev():
    Dev.show()

def afficherEnd():
    End.show()

        
def newManche():
    global tour
    global compteur
    tour=1
    joueur1.coup=5
    joueur2.coup=4
    compteur+=1
   
    global case 
    activ(True)
    RemoveImage()
    case=[0]*10
    uiGame.label.setText("Au tour de "+joueur1.nom+"(cercle)")
    uiGame.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MV Boli\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:10px; margin-bottom:10px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">"+joueur1.nom+" "+str(joueur1.point)+"-"+str(joueur2.point)+" "+joueur2.nom+" </span></p></body></html>")
    uiGame.label_2.setText("Manche "+str(compteur))
    

        
def activ(val):
    for i in range(1,10) :
        buttons[i].setEnabled(val)
        

def RemoveImage():
    for i in range(1,10) :
        buttons[i].setStyleSheet("QPushButton {\n"
"background : none ;\n"
"border:none;\n"
"}")



def afficherWin():
    Win.show()
    #launch()
    
def afficherImage(n):
    global case
    global compteur
    if tour==1:
        buttons[n].setStyleSheet("QPushButton {\n"
"background : none ;\n"
"border:none;\n"
"image : url(cercle.png)\n"
"}")
        buttons[n].setEnabled(False)
        case[n]=1
        joueur1.joue()

        if showWin(1)==True :
            joueur1.point+=1
            uiGame.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MV Boli\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:10px; margin-bottom:10px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">"+joueur1.nom+" "+str(joueur1.point)+"-"+str(joueur2.point)+" "+joueur2.nom+" </span></p></body></html>")
            if nombre==compteur:
                if joueur1.point>joueur2.point :
                    uiEnd.label.setText( joueur1.nom+"\n remporte  la partie")
                elif joueur1.point<joueur2.point :
                    uiEnd.label.setText( joueur2.nom+"\n remporte  la partie")
                else :
                    uiEnd.label.setText("Match \n nul ")
                afficherEnd()
            else:
                uiWin.label.setText(joueur1.nom +"\n a gagné cette \n manche ")
                Win.show()
        else :
            changetour()
            
    else :
        buttons[n].setStyleSheet("QPushButton {\n"
"background : none ;\n"
"border:none;\n"
"image : url(croix.png)\n"
"}")
        buttons[n].setEnabled(False)
        case[n]=2
        joueur2.joue()
        if showWin(2)==True :
            joueur2.point+=1
            uiGame.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'MV Boli\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
    "<p align=\"center\" style=\" margin-top:10px; margin-bottom:10px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt;\">"+joueur1.nom+" "+str(joueur1.point)+"-"+str(joueur2.point)+" "+joueur2.nom+" </span></p></body></html>")
            if nombre==compteur:
                if joueur1.point>joueur2.point :
                    uiEnd.label.setText( joueur1.nom+"\n remporte  la partie")
                elif joueur1.point<joueur2.point :
                    uiEnd.label.setText( joueur2.nom+"\n remporte  la partie")
                else :
                    uiEnd.label.setText("Match \n nul ")
                afficherEnd()
            else:
                uiWin.label.setText(joueur2.nom +"\n a gagné cette \n manche ")
                Win.show()
        else :
            changetour()
        
        
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

#jeu
Game= QtWidgets.QMainWindow()
uiGame = windowGame()
uiGame.setupUi(Game)

#erreur
Erreur= QtWidgets.QDialog()
uiErreur = windowErreur()
uiErreur.setupUi(Erreur)

#win
Win= QtWidgets.QDialog()
uiWin = windowWin()
uiWin.setupUi(Win)

#End
End= QtWidgets.QDialog()
uiEnd = windowEnd()
uiEnd.setupUi(End)

#regles 
Rule= QtWidgets.QMainWindow()
uiRule = windowRule()
uiRule.setupUi(Rule)

#portfolio 
Dev = QtWidgets.QDialog()
uiDev = windowDev()
uiDev.setupUi(Dev) 

buttons = [0,
           uiGame.pushButton1,
           uiGame.pushButton2,
           uiGame.pushButton3,
           uiGame.pushButton4,
           uiGame.pushButton5,
           uiGame.pushButton6,
           uiGame.pushButton7,
           uiGame.pushButton8,
           uiGame.pushButton9,
           ]

def f():
    global compteur
    MainWindow.show()
    newManche()
    compteur=1
    joueur1.point=0
    joueur2.point=0
    Game.hide()
    
def g():
    Game.hide()
    End.hide()

MainWindow.show()
#les signaux , gestion d'evenements sur les boutons 
def launch():
    ui.pushButton.clicked.connect(afficherRule)
    uiRule.actionA_propos.triggered.connect(afficherDev)
    uiRule.actionJeu.triggered.connect(afficherGame)
    uiGame.pushButton1.clicked.connect(lambda : afficherImage(1))
    uiGame.pushButton2.clicked.connect(lambda : afficherImage(2))
    uiGame.pushButton3.clicked.connect(lambda : afficherImage(3))
    uiGame.pushButton4.clicked.connect(lambda : afficherImage(4))
    uiGame.pushButton5.clicked.connect(lambda : afficherImage(5))
    uiGame.pushButton6.clicked.connect(lambda : afficherImage(6))
    uiGame.pushButton7.clicked.connect(lambda : afficherImage(7))
    uiGame.pushButton8.clicked.connect(lambda : afficherImage(8))
    uiGame.pushButton9.clicked.connect(lambda : afficherImage(9))
    uiWin.buttonBox.accepted.connect(newManche)
    uiEnd.buttonBox.accepted.connect(f)
    uiEnd.buttonBox.rejected.connect(g)
launch()

sys.exit(app.exec_())


