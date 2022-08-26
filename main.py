
from glob import glob
from logging import root
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import random


class FirstWindow(Screen):
    pass

class SecondWindow(Screen):

    ranno = [i for i in range(9,99)]
    random.shuffle(ranno)
    OG = ranno[0:6]


class ThirdWindow(Screen):
    obj = SecondWindow
    ranno = obj.ranno
    OG = obj.OG
    score = 0

    opt = OG[0:3]
    opt.append(ranno[6 + score])
    random.shuffle(opt)

    def check(self,n):
        if n not in self.OG:
            self.OG.append(n)
            self.score += 1
            self.change_opt()
            self.ids.score.text = "score: %i"%self.score
        elif n in self.OG:
            
            self.ids.question.text = "Wrong ans \n your score %i"%self.score


    def change_opt(self):
        random.shuffle(self.OG)
        self.opt = self.OG[0:3]
        self.opt.append(self.ranno[6 + self.score])
        random.shuffle(self.opt)
        self.ids.opt1.text = str(self.opt[0])
        self.ids.opt2.text = str(self.opt[1])
        self.ids.opt3.text = str(self.opt[2])
        self.ids.opt4.text = str(self.opt[3])

    




class WindowManager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    screen_four = ObjectProperty(None)


    



class memory_game(App):
    def build(self):
        m = WindowManager()
        return m

if __name__ == '__main__':
    
    memory_game().run()


