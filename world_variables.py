class World_Variables:
    def __init__(self):
        #screen
        self.screenX = 1200
        self.screenY = 600
        self.fps = 30

        #world
        self.background_color = (0,0,0)
        self.gradient = 2


        #colony
        self.ant_amount = 100
        self.colony_amount_food = 1000

        #ant 
        self.ant_color = (255,255,255)
        self.ant_trace_forward = (255,0,0)
        self.ant_trace_back = (0,255,0)

        #food

        #obstacle
        self.obstacle_color = (127,127,127)
        self.obstacle_amount = 100

        #overlay
        self.overlay_thickness = 250