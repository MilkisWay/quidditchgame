import pygame
from tiles import Tile
from mapp import tile_size, screen_width, screen_height
from tile_image_emun import Tile_image

class Ground:
    def __init__(self,ground_data,ground_result):
        #ground setup
        self.display_ground= ground_result
        self.setup_ground(ground_data)
        self.world_shift_x=0
        self.world_shift_y=0

    def setup_ground (self,layout):

        self.tiles=pygame.sprite.Group()

        for row_index,row in enumerate(layout):#index and information #enum
             for col_index,lock in enumerate(row):
                 x = col_index * tile_size
                 y = row_index * tile_size
                 for i in Tile_image:
                     if lock == i.name:
                         tile = Tile((x,y),tile_size,i.value)
                         self.tiles.add(tile)
    def run(self):

        #tiles
        self.tiles.update(self.world_shift_x,self.world_shift_y)
        self.tiles.draw(self.display_ground)