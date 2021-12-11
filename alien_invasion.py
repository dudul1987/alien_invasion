import sys         # 导入模块sys（玩家退出时，使用模块sys中的工具来退出游戏）。
import pygame      # 导入模块pygame（包含开发游戏所需的功能）。

from settings import Settings

class AlienInvasion: 
	"""管理游戏资源和行为的类"""

	def __init__(self):
		"""初始化游戏并创建游戏资源"""
		pygame.init()       # 初始化背景设置。
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("外星人入侵")

	def run_game(self):
		"""开始游戏的主循环"""
		while True:
			# 监视键盘和鼠标的事件。
			for event in pygame.event.get():
				if event.type == pygame.QUIT:     # 当玩家单击关闭按钮时。
					sys.exit()
			self.screen.fill(self.settings.bg_color)       # 每次循环时都重绘屏幕。
			# 让最近绘制的屏幕可见。
			pygame.display.flip()

if __name__ == '__main__':       # 仅当直接运行该文件时，它们才会执行。
	# 创建游戏实例并运行游戏。
	ai = AlienInvasion()
	ai.run_game()
