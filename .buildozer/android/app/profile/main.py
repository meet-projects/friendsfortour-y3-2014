from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout




class FFTmain(Widget):
	
	pass



class FFTApp(App):
	def build(self):
        	main = FFTmain()
		return main


if __name__ == '__main__':
	FFTApp().run()
