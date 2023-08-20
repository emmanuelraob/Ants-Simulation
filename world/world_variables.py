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
        self.food_color = (0,200,0)
        self.food_collection_amount = 4
        self.food_collection_radius = 25
        self.food_amount_collection = 1000

        #obstacle
        self.obstacle_color = (127,127,127)
        self.obstacle_amount = 100
        self.tree_depth = 2

        #overlay
        self.overlay_thickness = 250