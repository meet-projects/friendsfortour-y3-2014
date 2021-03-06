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
from kivy.uix.anchorlayout import AnchorLayout
from kivy.clock import Clock

i = 0
sm = ScreenManager()

class FindVol(Screen):
	pass

class NewsFeed(Screen):
	pass

class Chat(Screen):
	def write(self, dt):
		global i
		if i==0:
			i +=1 
			self.ids.l11.text = self.ids.l12.text
			self.ids.l12.text = "every thing is fine"
		elif i==1:
			self.ids.messageBox.add_widget(Label(text = "you suck"))

	def g(self):
		self.ids.l12.text = self.ids.messageText.text
		self.ids.messageText.text = ''
		Clock.schedule_once(self.write, 4)

class NewsFeedScroll(ScrollView):
	pass
class FFTApp(App):

	def build(self):
		self.news = NewsFeed(name= 'news')
		sm.add_widget(self.news)
		self.find = FindVol(name= 'find')
		sm.add_widget(self.find)
		self.chat = Chat(name = 'chat')
		sm.add_widget(self.chat)

		container = BoxLayout(orientation = 'vertical')

		topBar = AnchorLayout(size_hint = (1, None), anchor_x = 'center', anchor_y = 'top')

		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		for i in range(5):
			examp = BoxLayout(size_hint_x=1, size_hint_y=None, height=100)
			examp.add_widget(Label(text="moshe"+str(i)))
			layout.add_widget(examp)
		self.news.ids.moshe.add_widget(layout)
		#scroll = ScrollView(size_hint=(None,None), size=(400,400))
		#scroll.add_widget(layout)
		#self.news.add_widget(scroll)
		return sm
	
	def change(self):
		sm.current = 'find'
	
	def change2(self):
		sm.current = 'news'
	def change3(self):
		sm.current = 'chat'

if __name__ == '__main__':
	FFTApp().run()


