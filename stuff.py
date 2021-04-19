import pygame

pygame.init()        

class Box:

	def __init__(self, p_x, p_y, p_w = 20, p_h = 20, p_colour = [0, 0, 225], fill = True):
		self.x = p_x
		self.y = p_y
		self.w = p_w
		self.h = p_h
		self.colour = (p_colour[0], p_colour[1], p_colour[2])
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
		self.fill = fill

	def isColliding(self, other):
		if self.rect.colliderect(other.rect):
			return True

	def draw(self, window):
		if self.fill:
			pygame.draw.rect(window, self.colour, self.rect)
		else:
			pygame.draw.rect(window, self.colour, self.rect, 5)


class Button(Box):

	def __init__(self, p_x, p_y, p_w, p_h, p_colour=[100, 100, 100], string=None, p_size=15):
		self.size = p_size
		self.string = string
		self.original_colour = (p_colour[0], p_colour[1], p_colour[2])
		self.hover_colour = ((self.original_colour[0]+50), (self.original_colour[1]+50), (self.original_colour[2]+50))
		super().__init__(p_x, p_y, p_w, p_h, p_colour)
		self.rect.centerx = p_x
		self.rect.centery = p_y

	def draw(self, screen):
		super().draw(screen)
		write(screen, self.string, self.rect.centerx, self.rect.centery, self.size)


	def is_over(self, m_x, m_y):
		if (self.rect.x <= m_x <= self.rect.x+self.w) and (self.rect.y <= m_y <= self.rect.y+self.h):
			self.colour = self.hover_colour
			return True
		self.colour = self.original_colour
		return False



def Grid(window, p_r, p_c, p_w, p_h):
	for i in range(p_c):
		for j in range(p_r+1):
			#if i != 0  and j != 0 and i != p_w and j != p_h:
			pygame.draw.line(window, (50, 50, 50), (p_w/p_c * i, 0), (p_w/p_c * i, p_h), 3)
			pygame.draw.line(window, (50, 50, 50), (0, p_h/p_r * j), (p_w, p_h/p_r * j), 3)

def load_image(p_name):
	image = pygame.image.load(p_name)
	return image, image.get_rect()


def write(surface, msg, x, y, size):
	if pygame.font:
		font = pygame.font.Font(None, size)
		text = font.render(msg, 1, (50, 50, 50))
		textpos = text.get_rect(centerx=x, centery=y)
		surface.blit(text, textpos)

def scale(p_c, p_ch, p_th):
	return (p_c/p_ch) * p_th