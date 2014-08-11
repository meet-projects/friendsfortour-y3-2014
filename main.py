import kivy
kivy.require('1.0.8') #our version..

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen

sm = ScreenManager()
screens = [Screen(name='Title {}'.format(i)) for i in range(2)]

sm.switch_to(screens[0])
# later
sm.switch_to(screens[1], direction='right')

for i in range(2):
    screen = Screen(name='Title %d' % i)
    sm.add_widget(screen)

sm.current = 'Title 2'

class FFT(ScreenManager):
	class FindVol(Widget):
		pass
	class NewsFeed(Widget):
		pass

	

class FFTApp(App):
	def build(self):
		return FFT()

if __name__ == '__main__':
	FFTApp().run()
