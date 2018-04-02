import sys
import pygame as pg

#Create a variable to change current button being selected
aboutBtn = 1
back = False

#Init and load sound effects
pg.mixer.init(44100, -16, 2, 4096)
control_menu = pg.mixer.Sound("sounds/control_menu.wav")
control_menu.set_volume(0.22)
select_menu = pg.mixer.Sound("sounds/select_menu.wav")
select_menu.set_volume(0.22)


def checkEvents(setting, screen, stats, sb, playBtn, quitBtn, menuBtn, sel, ship, aliens, bullets, eBullets):
	"""Respond to keypresses and mouse events."""
	# add button_sound (case quit)
	button_click_sound = pg.mixer.Sound('./sound_effect/button_clicked.wav')
	global aboutBtn
	for event in pg.event.get():
		#Check for quit event
		if event.type == pg.QUIT:
			sys.exit()
		#Check for key down has been pressed
		elif event.type == pg.KEYDOWN:
			#Check if down, up, enter, esc is pressed
			if event.key == pg.K_DOWN:
				if aboutBtn < 2:
					control_menu.play()
					aboutBtn += 1
					sel.rect.y += 50
			if event.key == pg.K_UP:
				if aboutBtn > 1:
					control_menu.play()
					aboutBtn -= 1
					sel.rect.y -= 50
			if event.key == pg.K_RETURN:
				if aboutBtn == 1:
					select_menu.play()
					stats.mainMenu = True
					stats.mainGame = False
					stats.twoPlayer = False
					stats.mainAbout = False
					aboutBtn = 1
					sel.rect.centery = playBtn.rect.centery
				elif aboutBtn == 2:
					pg.mixer.Sound.play(button_click_sound)
					pg.time.delay(300)
					sys.exit()
			if event.key == pg.K_ESCAPE:
				pg.mixer.Sound.play(button_click_sound)
				pg.time.delay(300)
				sys.exit()
	prepAbout(setting, screen)

def prepAbout(setting, screen):
	#Font settings for scoring information
	global image, rect
	image = pg.image.load('gfx/About_modify.png')
	image = pg.transform.scale(image,(setting.screenWidth,setting.screenHeight))
	rect = image.get_rect()


def drawMenu(setting, screen, sb, menuBtn, quitBtn, sel):
	"""Draw the menu and all of its elements"""
	global image, rect
	quitBtn.rect.y = 500
	quitBtn.msgImageRect.y = 500
	menuBtn.rect.y = 450
	menuBtn.msgImageRect.y = 450
	screen.fill(setting.bgColor)
	screen.blit(image, rect)
	menuBtn.drawBtn()
	quitBtn.drawBtn()
	#screen.blit(image, rect)
	sel.blitme()
	pg.display.flip()
