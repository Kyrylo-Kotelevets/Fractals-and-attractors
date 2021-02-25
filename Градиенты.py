from PIL import Image, ImageDraw
from math import pi, sin, cos, sqrt
from random import randint, choice, normalvariate
from point_2D import point

def rand_point():
	# return (normalvariate(im_size // 2, 400), normalvariate(im_size // 2, 400)) 
	return (randint(0, im_s
def distance(pt1, pt2):
	(x1, y1), (x2, y2) = pt1, pt2ize), randint(0, im_size))

	return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def interpolate(from_color, to_color, interval):
	delta =[(t - f) / interval for f , t in zip(from_color, to_color)]
	return [tuple(round(f + det * i) for f, det in zip(from_color, delta)) for i in range(interval)]
