from .enemy import Enemy


class Skeleton(Enemy):
    def __init__(self, x, y, platform_group, tile_list):
        super().__init__(
            x, y,
            platform_group,
            tile_list,
            "skeleton",
            speed=2,
            vertical_speed=0,
            gravity=0.5,
            # changed health from 100 to 130
            health=130,
            max_health=130,
            # changed strength from 25 to 33
            strength=33
        )
        self.health_bar_offset_x = (self.rect.width - self.health_bar_length) / 2
        self.health_bar_offset_y = self.rect.height / 2 - 35
