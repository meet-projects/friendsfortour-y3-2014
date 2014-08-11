from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout




class FFTmain(Widget):
############### for future use::::::
	##def displayTopRatedVols(self):
	##	userLayout = GridLayout(cols = 3)
	##	for i in range(10):
	##    		userLayout.add_widget(Label(text = ".....name....."))
	##    		findvol_layout.add_layout(userLayout)
	pass



class FFTApp(App):
	def build(self):
        	main = FFTmain()
		return main


if __name__ == '__main__':
	FFTApp().run()
