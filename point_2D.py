from math import pi, sin, cos, sqrt

class point(object):
	""" point """
	def __init__(self, x: float=0.0, y: float=0.0):
		self.x = x
		self.y = y

	def __neg__(self):
		return point(-self.x, -self.y)

	def __add__(self, other):
		if isinstance(other, (int, float)):
			return point(self.x + other, self.y + other)
		elif isinstance(other, point):
			return point(self.x + other.x, self.y + other.y)
		elif isinstance(other, (list, tuple)):
			if len(other) == 2:
				a, b = other
				return point(self.x + a, self.y + b)
			else:
				raise ValueError("Invalid size for adding")
		else:
			raise ValueError("Invalid type for adding")

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		return self + (-other)

	def __rsub__(self, other):
		return -self + other

	def __iadd__(self, other):
		return self + other

	def __mul__(self, other):
		if isinstance(other, (int, float)):
			return point(self.x * other, self.y * other)
		elif isinstance(other, list):
			if len(other) == len(other[0]) == 2:
				[b11, b12], [b21, b22] = other
				return point(self.x * b11 + self.y * b21, self.x * b12 + self.y * b22)
			else:
				raise ValueError("Invalid size for multiplying")
		else:
			raise ValueError("Invalid type for multiplying")

	def __rmul__(self, other):
		if isinstance(other, (int, float)):
			return point(self.x * other, self.y * other)
		elif isinstance(other, list):
			if len(other) == len(other[0]) == 2:
				[a11, a12], [a21, a22] = other
				return point(a11 * self.x + a12 * self.y, a21 * self.x + a22 * self.y)
			else:
				raise ValueError("Invalid size for multiplying")
		else:
			raise ValueError("Invalid type for multiplying")

	def __truediv__(self, other):
		if isinstance(other, (int, float)):
			return point(self.x / other, self.y / other)
		else:
			raise ValueError("Invalid type for dividing")

	def __floordiv__(self, other):
		if isinstance(other, (int, float)):
			return point(self.x // other, self.y // other)
		else:
			raise ValueError("Invalid type for dividing")

	def __int__(self):
		return point(int(self.x), int(self.y))

	def __iter__(self):
		return iter((self.x, self.y))

	def __str__(self):
		return f"({self.x}, {self.y})"

	def rotate(self, angle: float, ox: float=0.0, oy: float=0.0):
		angle, center = pi * (angle / 180), point(ox, oy)
		rot_matr = [[cos(angle), -sin(angle)],
					[sin(angle),  cos(angle)]]
		return rot_matr * (self - center) + center
