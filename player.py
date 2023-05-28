from direct.actor.Actor import Actor
import sys

class Player:
    def __init__(self, position):
        self.player = Actor('sours minecraft/ralph',
            {
                'walk': 'sours minecraft/ralph_walk',
                'run': 'sours minecraft/ralph_run'
            }
        )
        self.player.setTexture(loader.loadTexture('sours minecraft/ralph.jpg'))
        self.player.reparentTo(render)
        self.player.setPos(position)
        self.player.setScale(0.3)
        self.player.setH(45)
        self.eventHandler()
        self.firstFace()
        self.lastX = None
        self.lastY = None
        self.is_recenter = True
        self.mouseMagnitute = 10
        self.rotateX =0
        self.rotateY =0

        # taskMgr.add(self.gravity, 'gravity')
        taskMgr.add(self.checkPos, 'checkPos')

        taskMgr.add(self.checkZ, 'checkZ')
    def firstFace(self):
        base.disableMouse()
        base.camera.reparentTo(self.player)
        base.camera.setZ(1.5)
        base.camera.setH(180)
        base.accept("escape", sys.exit, [0])

    def eventHandler(self):
        base.accept('a', self.left)
        base.accept('d', self.right)
        base.accept('w', self.up)
        base.accept('s', self.down)

    def left(self):
        self.player.setX(self.player.getX() - 1)
    def right(self):
        self.player.setX(self.player.getX() + 1)
    def up(self):
        self.player.setY(self.player.getY() - 1)
    def down(self):
        self.player.setY(self.player.getY() + 1)



    def gravity(self, task):
        self.player.setZ(self.player.getZ() - 1)

        return task.cont

    def checkZ(self, task):
        if self.player.getZ() < -100:
           sys.exit()
        return task.cont   

    def checkPos(self, task):
        mouse = base.mouseWatcherNode # --_--
        is_mouse = mouse.hasMouse()
        if is_mouse:
            x= mouse.getMouseX()     
            y= mouse.getMouseY()
            if self.lastX is not None: 
                if self.is_recenter:
                    dX, dY = x,y
                else:
                    dX,dY = x-self.lastX, y-self.lastY                   
            
            else:
                dX,dY = 0,0 #because
            self.lastX,self.lastY = x,y
        else:
            dX,dY,x,y = 0,0,0,0
        if self.is_recenter:
            self.reCenterMouse()
            self.lastX, self.lastY = 0,0   
        self.rotateX = dX*self.mouseMagnitute*10 #because 2 PS:(no thanks)
        self.rotateY = dY*self.mouseMagnitute*10 #because 3 
        self.player.setH(-self.rotateX) #H for x
        self.player.setP(-self.rotateY) #P for y
        # da поможет нам господь
        return task.cont


    def reCenterMouse(self):
        base.win.movePointer(0,int(base.win.getProperties().getXSize()/2),int(base.win.getProperties().getYSize()/2))# I debil

         

