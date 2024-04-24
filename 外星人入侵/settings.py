class Settings:
    '''存储游戏《外星人入侵》中的所有设置'''

    def __init__(self):
        '''初始化游戏的静态的设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 2

        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width =10
        self.bullet_height =10
        self.bullet_color = (180,100,100)
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed = 1
        self.fleet_drop_speed = 10

        #加快游戏的节奏的速度
        self.speedup_scale = 1.1
        #外星人分数的提高速度
        self.score_scale = 1.5

        self.initializa_dynamic_settings()


    def initializa_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed = 0.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.5
        # fleet_direction 为1 表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        #计分
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度的设置和外星人的分数'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points)
