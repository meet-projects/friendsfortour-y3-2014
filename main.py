import kivy
kivy.require('1.8.0') #our version..

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

sm = ScreenManager()

class FindVol(Screen):
	pass

class NewsFeed(Screen):
	pass


class FFTApp(App):
	def build(self):
		self.news = NewsFeed(name= 'news')
		sm.add_widget(self.news)
		self.find = FindVol(name= 'find')
		sm.add_widget(self.find)
		return sm
	
	def change(self):
		sm.current = 'find'
	
	def change2(self):
		sm.current = 'news'

if __name__ == '__main__':
	FFTApp().run()
