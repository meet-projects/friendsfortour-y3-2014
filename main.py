import kivy
kivy.require('1.0.8') #our version..

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder


sm = ScreenManager()

class NewsFeed(Screen):
	pass


class FFTApp(App):
	def build(self):
		self.news = NewsFeed()
		sm.add_widget(self.news)
		return sm

if __name__ == '__main__':
	FFTApp().run()
