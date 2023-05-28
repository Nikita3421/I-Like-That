class Map:
    def __init__(self):
        self.default_image1 = 'sours minecraft/stone.png'
        self.default_image = 'sours minecraft/dirt.jpg'
        self.default_image2 = 'sours minecraft/derevo.png'
        self.default_image3 = 'sours minecraft/brevno.png'
        self.default_image4 = 'sours minecraft/grass.png'
        self.default_model = 'sours minecraft/block.egg'
        self.create_branch()
        for x in range (16):
            for y in range (6, 22):
                for z in range(-5,-3):
                    self.create_block((x, y, z))
    def create_block(self, position):
        self.model = loader.loadModel(self.default_model)
        self.texture = loader.loadTexture(self.default_image)
        self.model.setTexture(self.texture)
        self.model.setPos(position)
        self.model.reparentTo(self.branch)
    def create_branch(self):
        self.branch = render.attachNewNode('map_branch')
