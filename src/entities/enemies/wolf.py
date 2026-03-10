from .enemy import Enemy


class Wolf(Enemy):
    def __init__(self, x, y, platform_group, tile_list):
        super().__init__(
            x, y,
            platform_group,
            tile_list,
            "wolf",
            speed=4,
            vertical_speed=0,
            gravity=0.5,
            # changed health from 50 to 90
            health=90,
            max_health=90,
            # changed strength from 20 to 30
            strength=30
        )
        self.health_bar_offset_x = (self.rect.width - self.health_bar_length) / 2
        self.health_bar_offset_y = self.rect.height / 2 - 35
