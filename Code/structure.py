# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:20:36 2021

@author: HP
"""

class Joueur :
    def __init__(self,nom,rang):
        self.nom=nom
        self.rang=rang
        self.point=0
        if rang==1 :
            self.coup=5
        else :
            self.coup=4
        
    def joue(self) :
        self.coup-=1
        