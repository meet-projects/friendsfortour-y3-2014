import kivy
kivy.require('1.0.8') #our version..

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.lang import Builder


sm = ScreenManager()

#screens = [Screen(name='Title {}'.format(i)) for i in range(2)]

#sm.switch_to(screens[0])
#sm.switch_to(screens[1], direction='right')

#for i in range(2):
#	screen = Screen(name='Title %d' % i)
#	sm.add_widget(screen)

#sm.current = 'Title 2'

class FindVol(Screen):
	pass
class NewsFeed(Screen):
	pass

#sm.add_widget(FindVol(name='FindAVolunteer'))
#sm.add_widget(NewsFeed(name='NewsFeed'))	

class FFTApp(App):
	def build(self):
		self.news = NewsFeed()
		sm.add_widget(news)
		self.find = FindVol()
		return sm
	def change(self):


if __name__ == '__main__':
	FFTApp().run()
