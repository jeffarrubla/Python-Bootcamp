#GUI widget basics
import ipywidgets as widgets

w = widgets.IntSlider()

from IPython.display import display

display(w)

display(w)

w.close()

#play with the widget properties
w = widgets.IntSlider()
display(w)

print(w.value)

w.value = 50

w.keys

w.max = 2000

#link 2 widgets
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a,'value'),(b,'value'))

