import panel as pn

pn.extension(sizing_mode="stretch_width")

slider = pn.widgets.FloatSlider(start=0, end=10, name='Amplitude')

def callback(new):
    return f'Amplitude is: {new}'

pn.Row(slider, pn.bind(callback, slider)).servable(target='simple_app')


p1 = pn.widgets.Button( name='Scatter', margin=5)

p2 = pn.widgets.Button( name='Line', margin=5)

p3 = pn.pane.SVG('https://assets.holoviz.org/panel/samples/svg_sample2.svg', name='Square', sizing_mode='stretch_width')
pn.Accordion(p1, p2, p3, toggle=True, header_color='green').servable(target='accordion')

