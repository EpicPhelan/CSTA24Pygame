from turtle import Turtle


class Bullet(Turtle):
    bullets = []
    
    def __init__(self, heading):
        super().__init__()
        self.shape('square')
        self.pu()
        self.color('white')
        self.setheading(heading)
        self.move_speed = 10
        self.shoot = False
        Bullet.bullets.append(self)
    
    # The @ tells python this is a special type of function
    # These are called decorators
    @staticmethod  
    def shoot(ship_heading):
        ''' We won't call this method on the object
        We will call it on the class. That means it is a class method
        '''
        if len(Bullet.bullets) < 4:
            # Creates a bullet with the heading argument
            # appends the bullet to the class variable bullets
            Bullet.bullets.append(Bullet(ship_heading))
        
        # after the bullets are made
        for bullet in Bullet.bullets:
            if bullet.shoot != True:
                bullet.shoot = True
                bullet.setheading(ship_heading)
                break
    
    def move(self):
        self.forward(self.move_speed)
        
        # detect if it goes off screen and set shoot to false
        # send it back to the ship
        if self.xcor() > 300 or self.xcor() < -300:
            self.shoot = False
        if self.ycor() > 300 or self.ycor() < -300:
            self.shoot = False