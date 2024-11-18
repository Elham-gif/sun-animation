from cs1graphics import *
from time import sleep

canvas = Canvas(800, 600, 'white', 'Sunrise')

#colors for the sky
sky_colors = [(60, 70, 80), (80, 100, 150), (180, 200, 240)]

#colors for the sun
sun_colors = [(255, 255, 200), (255, 200, 150), (255, 100, 0)]

sky = Rectangle(1800, 1800)
    
sky.setBorderWidth(0)
canvas.add(sky)

sun = Circle(50, Point(10,100))
    
sun.setBorderWidth(0)
    
canvas.add(sun)

#interpolate colors
def interpolate_colors(color1, color2, ratio):
    """Interpolate two RGB colors using a given ratio"""
    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
    return (r, g, b)

#animation

for i in range(150):
    # calculate the current ratio for the sky and sun colors
    sky_ratio = min(i / 50.0, 2.0 - i / 50.0)
    sun_ratio = min(i / 50.0, 1.0)

    # interpolate the colors for the sky and sun
    sky_color = interpolate_colors(sky_colors[0], sky_colors[1], sky_ratio)
    sun_color = interpolate_colors(sun_colors[0], sun_colors[1], sun_ratio)

    # color of the sky and sun
    sun.setFillColor(Color(sun_color))
    sky.setFillColor(Color(sky_color))

    
    sun.move(7,0)

    #before drawing the next frame WAIT
    sleep(0.1)

