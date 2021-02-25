from PIL import Image, ImageDraw
from math import pi, sin, cos, sqrt
from random import randint, choice, normalvariate
from point_2D import point

def rand_point():
	# return (normalvariate(im_size // 2, 400), normalvariate(im_size // 2, 400)) 
	return (randint(0, im_size), randint(0, im_size))

def distance(pt1, pt2):
	(x1, y1), (x2, y2) = pt1, pt2
	return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def interpolate(from_color, to_color, interval):
	delta =[(t - f) / interval for f , t in zip(from_color, to_color)]
	return [tuple(round(f + det * i) for f, det in zip(from_color, delta)) for i in range(interval)]

def get_polygon(ox: float, oy: float, radius: float, n_vertices) -> list:
	vertex = list()
	x, y = ox, oy - radius
	theta = 2 * pi / n_vertices

	for i in range(n_vertices):
		new_x = (x - ox) * cos(i * theta) - (y - oy) * sin(i * theta) + ox
		new_y = (x - ox) * sin(i * theta) + (y - oy) * cos(i * theta) + oy
		vertex.append((new_x, new_y))
	return vertex


im_size = 1920
image = Image.new('RGB', (im_size, im_size), 'black')
draw = ImageDraw.Draw(image)

'''
for i, color in enumerate(interpolate((125, 0, 0), (0, 125, 0), 2 * im_size - 1)):
	draw.line([(i, 0), (0, i)], tuple(color), width=1)
'''
'''
color = interpolate((255, 255, 0), (255, 100, 0), im_size // 2)
for i in range(len(color) - 1, 0, -1):
	draw.ellipse([im_size // 2 - i, im_size // 2 - i, im_size // 2 + i, im_size // 2 + i], fill=color[i])
'''

'''
curr_point = rand_point()
for _ in range(1000):
	next_point = rand_point()
	draw.line([curr_point, next_point], fill='white', width=1)
	curr_point = next_point
'''

'''
points = [rand_point() for _ in range(40)]
for curr in points:
	for near in sorted(points, key=lambda pt: distance(curr, pt))[22:-4]:
		draw.line([curr, near], fill='white', width=1)
'''


# dist_color = interpolate((255, 0, 0), (0, 0, 125), 161 + 20)

out_points = get_polygon(ox=im_size // 2, oy=im_size // 2, n_vertices=33, radius=im_size // 2 - 100)
in_points  = get_polygon(ox=im_size // 2, oy=im_size // 2, n_vertices=22, radius=im_size // 2 - 300)
center = (im_size // 2, im_size // 2)
# points = get_polygon(ox=im_size // 2, oy=im_size // 2, n_vertices=33, radius=im_size // 2 - 100)

for pt in out_points:
	for near in sorted(in_points, key=lambda x: distance(pt, x))[:5]:
		draw.line([pt, near], fill=(255, 255, 255), width=1)
		#draw.line([pt, near], fill=(0, 102, 255), width=1)
		#draw.line([pt, near], fill=dist_color[int(distance(pt, near) // 10)], width=2)
for pt in in_points:
	draw.line([pt, center], fill=(255, 255, 255), width=1)

image.save("Dura.png")
image.show()
from PIL import Image, ImageDraw
from math import pi, sin, cos, sqrt
from random import randint, choice, normalvariate
from point_2D import point

def rand_point():
	# return (normalvariate(im_size // 2, 400), normalvariate(im_size // 2, 400)) 
	return (randint(0, im_size), randint(0, im_size))

def distance(pt1, pt2):
	(x1, y1), (x2, y2) = pt1, pt2
	return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def interpolate(from_color, to_color, interval):
	delta =[(t - f) / interval for f , t in zip(from_color, to_color)]
	return [tuple(round(f + det * i) for f, det in zip(from_color, delta)) for i in range(interval)]

def get_polygon(ox: float, oy: float, radius: float, n_vertices) -> list:
	vertex = list()
	x, y = ox, oy - radius
	theta = 2 * pi / n_vertices

	for i in range(n_vertices):
		new_x = (x - ox) * cos(i * theta) - (y - oy) * sin(i * theta) + ox
		new_y = (x - ox) * sin(i * theta) + (y - oy) * cos(i * theta) + oy
		vertex.append((new_x, new_y))
	return vertex


im_size = 1920
image = Image.new('RGB', (im_size, im_size), 'black')
draw = ImageDraw.Draw(image)

'''
for i, color in enumerate(interpolate((125, 0, 0), (0, 125, 0), 2 * im_size - 1)):
	draw.line([(i, 0), (0, i)], tuple(color), width=1)
'''
'''
color = interpolate((255, 255, 0), (255, 100, 0), im_size // 2)
for i in range(len(color) - 1, 0, -1):
	draw.ellipse([im_size // 2 - i, im_size // 2 - i, im_size // 2 + i, im_size // 2 + i], fill=color[i])
'''

'''
curr_point = rand_point()
for _ in range(1000):
	next_point = rand_point()
	draw.line([curr_point, next_point], fill='white', width=1)
	curr_point = next_point
'''

'''
points = [rand_point() for _ in range(40)]
for curr in points:
	for near in sorted(points, key=lambda pt: distance(curr, pt))[22:-4]:
		draw.line([curr, near], fill='white', width=1)
'''


# dist_color = interpolate((255, 0, 0), (0, 0, 125), 161 + 20)

out_points = get_polygon(ox=im_size // 2, oy=im_size // 2, n_vertices=33, radius=im_size // 2 - 100)
in_points  = get_polygon(ox=im_size // 2, oy=im_size // 2, n_vertices=22, radius=im_size // 2 - 300)
center = (im_size // 2, im_size // 2)
# points = get_polygon(ox=im_size // 2, oy=im_size // 2, n_vertices=33, radius=im_size // 2 - 100)

for pt in out_points:
	for near in sorted(in_points, key=lambda x: distance(pt, x))[:5]:
		draw.line([pt, near], fill=(255, 255, 255), width=1)
		#draw.line([pt, near], fill=(0, 102, 255), width=1)
		#draw.line([pt, near], fill=dist_color[int(distance(pt, near) // 10)], width=2)
for pt in in_points:
	draw.line([pt, center], fill=(255, 255, 255), width=1)

image.save("Dura.png")
image.show()
