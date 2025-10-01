import panel as pn

pn.extension(sizing_mode="stretch_width")

slider = pn.widgets.FloatSlider(start=0, end=10, name='Amplitude')

def callback(new):
    return f'Amplitude is: {new}'

pn.Row(slider, pn.bind(callback, slider)).servable(target='simple_app')


p1 = pn.widgets.Button( name='Scatter', margin=5)

logo = 'https://panel.holoviz.org/_static/logo_horizontal.png'
w1 = pn.widgets.TextInput(name='Text:')
w2 = pn.widgets.FloatSlider(name='Slider')
p2 = pn.Card(w1, w2, name='Card', title='Card', styles={'background': 'WhiteSmoke'}  , 
    header_background='#2f2f2f',
    header_color='white',
    header=pn.panel(logo, height=40),
)

p3 = pn.pane.SVG('https://assets.holoviz.org/panel/samples/svg_sample2.svg', name='Square', sizing_mode='stretch_width')
pn.Accordion(p1, p2, p3, toggle=True, header_color='green').servable(target='accordion')

