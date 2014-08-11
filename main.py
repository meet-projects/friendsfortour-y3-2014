import kivy
kivy.require('1.0.8') #our version..

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

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
