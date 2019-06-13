# Widget styling and layouts

import ipywidgets as widgets
from IPyton.display import display

w = widgets.IntSlider()
display(w)

w.layout.margin = 'auto'
w.layout.height = '75px'

x = widgets.IntSlider(value=15,description='New Slider')
display(x)

x.layout = w.layout

widgets.Button(description='Ordinary Button',button_style='info')

b1 = widgets.Button(description='Custom Color')
b1.style.button_color = 'lightgreen'
b1

b1.style.keys

b2 = widgets.Button(description='NEW')
b2.style = b1.style
b

s1 = widgets.IntSlider(description='My Handle')
s1.slyle.handle_color = 'blue'
s1

s1.style.keys
