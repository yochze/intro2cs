from torpedo import *
from asteroid import *
from spaceship import *
from gameMaster import *
import math

class GameRunner:

    def __init__(self, amnt = 3):
        self.game = GameMaster()
        self.screenMaxX = self.game.get_screen_max_x()
        self.screenMaxY = self.game.get_screen_max_y()
        self.screenMinX = self.game.get_screen_min_x()
        self.screenMinY = self.game.get_screen_min_y()
        shipStartX = (self.screenMaxX-self.screenMinX)/2 + self.screenMinX
        shipStartY = (self.screenMaxY-self.screenMinY)/2 + self.screenMinY
        self.game.set_initial_ship_cords( shipStartX, shipStartY )
        self.game.add_initial_astroids(amnt)

    def run(self):
        self._do_loop()
        self.game.start_game()


    def _do_loop(self):
        self.game.update_screen()
        self.game_loop()
        # Set the timer to go off again
        self.game.ontimer(self._do_loop,5)

    def game_loop(self):
        """
        The main function of the game. 
        For each turn this function is being called.
        it handles the movement of the objects, shooting torpedos,
        handle collisions and check if the match should be ended according
        to predefined set of rules.
        """
        torpedos_to_remove, asteroids_to_remove = [], []
        self.move_asteroids()
        self.move_ship()
        self.move_torpedos()
        self.shooting_torpedo()
        self.add_super_torpedo() # New shape!
        pairs = self.check_collisions()
        asteroid_colided = self.ship_asteroid_collison()

        if pairs:
            # If there are colided pairs, then we should mark the 
            # torpedos and asteroids to be removed. 
            # And call the handle collisons (which adds ranking, splitting etc)
            self.handle_collisons(pairs)
            torpedos_to_remove  += [ torpedo for torpedo, asteroid in pairs ]
            asteroids_to_remove += [ asteroid for torpedo, asteroid in pairs ]
        
        if asteroid_colided:
            self.ship_collison_message()
            self.game.ship_down() # One life down
            asteroids_to_remove += [ asteroid_colided ] # Add this to removed
            

        # Remove asteroids and torpedos
        torpedos_to_remove += self.get_dead_torpedos()
        self.remove_asteroids(asteroids_to_remove)
        self.game.remove_torpedos(torpedos_to_remove)

        # Check if game should end
        self.end_game_conditions()


    def move_object(self, shape):
        """
        This function gets a BaseObject#Shape and calculates its next
        x,y coordinates based on the given formula.
        new_x = ((speedX + corX - minX )% dX) + minX (Same for Y cor)
        """
        min_x, max_x = self.game.get_screen_min_x(),self.game.get_screen_max_x()
        min_y, max_y = self.game.get_screen_min_y(),self.game.get_screen_max_y()

        dx = max_x - min_x
        dy = max_y - min_y
        inner_eq_x = shape.get_speed_x() + shape.get_x_cor() - min_x
        inner_eq_y = shape.get_speed_y() + shape.get_y_cor() - min_y 

        new_cord_x = ((inner_eq_x) % dx) + min_x
        new_cord_y = ((inner_eq_y) % dy) + min_y

        shape.move(new_cord_x, new_cord_y)

    
    def move_asteroids(self):
        """ 
        Collect all asteroids that are in the game and 
        move them with the move_object function.
        """
        asteroids = self.game.get_asteroids()
        for asteroid in asteroids:
            self.move_object(asteroid)

    def move_ship(self):
        """
        With the help of "move_object" function, this function
        checks which key is pressed by user and move the ship
        accordingly. It collects the ship X,Y of speed and position and send 
        it to the main move_object function
        """
        ship = self.game.get_ship()
        
        if self.game.is_right_pressed():
            # Right, wider angle
            ship.increase_angle()

        elif self.game.is_left_pressed():
            # Left, narrower angle
            ship.decrease_angle()

        elif self.game.is_up_pressed():
            # Up, accelerate
            deg = math.radians(ship.get_angle())
            x_speed = ship.get_speed_x() + math.cos(deg)
            y_speed = ship.get_speed_y() + math.sin(deg)

            ship.set_speed_x(x_speed)
            ship.set_speed_y(y_speed)
        
        # Move the object
        self.move_object(ship)

    def move_torpedos(self):
        """ 
        Collect all torpedosthat are in the game and 
        move them with the move_object function.
        """
        torpedos      = self.game.get_torpedos()
        for torpedo in torpedos:
            # Iterate through torpedos
            self.move_object(torpedo)

    def shooting_torpedo(self):
        """
        Shooting new torpedos based on the user input. 
        If space (fire trigger) is pressed, and the torpedos amount on screen
        didn't pass its limit (20) then the function generates
        a new torpedo, with appropriate angle, x,y position and speed.
        """
        torpedos_amount = len(self.game.get_torpedos())
        torpedos_limit = 20 # Set the torpedos limit.

        if self.game.is_fire_pressed() and (torpedos_amount < torpedos_limit):
            ship = self.game.get_ship() 

            # Collect position data for the new torpedo
            x_pos = ship.get_x_cor()
            y_pos = ship.get_y_cor()

            # Collect degrees
            org_deg = ship.get_angle()
            deg_r = math.radians(org_deg)
            
            # Collect speed
            x_speed = ship.get_speed_x() + 2 * math.cos(deg_r)
            y_speed = ship.get_speed_y() + 2 * math.sin(deg_r)

            # Call the external GameMaster#add_torpedo method to generate
            # a new torpedo.
            self.game.add_torpedo(x_pos, y_pos, x_speed, y_speed, org_deg)



    def check_collisions(self):
        """
        Check if any of the torpedos have colided with any of the asteroids
        This function works n^2 as it's iterates through all torpedos and for
        each of them it checks if any of the asteroids are intersecting.
        The function uses the external GameMaster#intersect to determine
        if two objects are intersecting.

        The function retunrs a list of colided pairs (torpedo, asteroid)
        """

        torpedos  = self.game.get_torpedos()  # Gather all torpedos
        asteroids = self.game.get_asteroids() # Gather asteroids
        colided_list = [] # Initialize the output

        for torpedo in torpedos:
            for asteroid in asteroids:
                if self.game.intersect(torpedo, asteroid):
                    # Mark asteroid and torpedo to be removed
                    colided_list.append([torpedo, asteroid])
        
        # Return the list of colided pairs
        return colided_list


    def handle_collisons(self, colided_pairs):
        """
        Handle asteroid and torpedo colision. 
        The function input is the colided list of pairs from the previous
        method, and it iterates the objects and handle them seperately
        adds ranking and split the asteroids if necassery
        """
        
        # Create a dictionary for the scoring table
        # Based on the instructions, an asteroid has a size range of (1,3)
        # Each has the according scoring points
        score_table = { 3:20, 2:50, 1:100 }

        for torpedo, asteroid in colided_pairs:
            # Iterates through all the colided pairs of torpedo and asteroids
            self.game.add_to_score(score_table[asteroid.size]) # add score 
                                                               # based on the
                                                               # asteroid size
            if asteroid.size > 1: 
                # If the asteroid is larger than the smallest size (1):
                # Generate new splitted asteroids
                x_pos = asteroid.get_x_cor()
                y_pos = asteroid.get_x_cor()
                x_speed, y_speed = self.get_new_asteroids_speed(asteroid, 
                                                                 torpedo)
                new_size = asteroid.size - 1 # Set one smaller size
                
                # Add to game first asteroid
                self.game.add_asteroid(x_pos, y_pos, x_speed, y_speed, new_size)
                # Add the second asteroid, to go in different direction
                self.game.add_asteroid(x_pos, y_pos, -x_speed, -y_speed, new_size)
        

    def get_new_asteroids_speed(self, asteroid, torpedo):
        """
        A helper function to determine the new asteroids speed.
        It is generated according to the colided asteroid and torpedo
        data.
        returns a tuple of x,y speed 
        """
        ast_x = asteroid.get_speed_x()
        ast_y = asteroid.get_speed_y()

        tor_x = torpedo.get_speed_x()
        tor_y = torpedo.get_speed_y()

        new_speed_x =  tor_x + ast_x / ( math.sqrt(ast_x**2 + ast_y**2) )
        new_speed_y =  tor_y + ast_y / ( math.sqrt(ast_x**2 + ast_y**2) )

        return(new_speed_x, new_speed_y)

    def get_dead_torpedos(self):
        """
        Collect all the dead (life_capacity is 0) and return
        a list of them.
        """
        torpedos            = self.game.get_torpedos()
        dead_torpedos       = []
        life_capacity_limit = 0

        for torpedo in torpedos:
            if torpedo.get_life_span() <= life_capacity_limit:
                dead_torpedos.append(torpedo)
        
        return dead_torpedos


    def remove_asteroids(self, asteroids):
        """
        Gets a list of N asteroids and remove each of them from the 
        game.
        """
        for asteroid in asteroids:
            self.game.remove_asteroid(asteroid)


    def ship_asteroid_collison(self):
        """
        Check if a ship has colided with an asteroid.
        The function iterates through all asteroids and run the external
        GameMaster#intersect function to determine if they hit each other.
        If so, it returns the _first_ colided asteroid.
        """
        ship = self.game.get_ship()
        asteroids = self.game.get_asteroids()

        for asteroid in asteroids:
            if self.game.intersect(ship, asteroid):
                return asteroid

    def ship_collison_message(self):
        """
        Helper function to show ship and asteroid collison message 
        to the end-user.
        """
        title = "Collison!"
        message = "Your ship has colided with an asteroid. "

        self.game.show_message(title, message)

    def add_super_torpedo(self):
        """
        Add super torpedos if it didn't pass the super_torpedos limit (10)
        inherit the position from the ship and assign it to the new
        super_torpedo

        """
        torpedos_amount = len(self.game.get_super_torpedos()) # Number of 
                                                              # super torpedos
        torpedos_limit = 10 # Set the torpedos limit.

        if self.game.is_super_torpedo_pressed() and \
                                (torpedos_amount < torpedos_limit):
            ship = self.game.get_ship() 

            # Collect position data for the new torpedo
            x_pos = ship.get_x_cor()
            y_pos = ship.get_y_cor()

            # Collect degrees
            org_deg = ship.get_angle()
            deg_r = math.radians(org_deg)
            
            # Collect speed
            x_speed = ship.get_speed_x() + 2 * math.cos(deg_r)
            y_speed = ship.get_speed_y() + 2 * math.sin(deg_r)

            # Call the external GameMaster#add_super_torpedo method to generate
            # a new super torpedo.
            self.game.add_super_torpedo(x_pos, y_pos, x_speed, y_speed, org_deg)



    def end_game_conditions(self):
        """
        The function checks if the game should be ended based on predefined
        rules. If user pressed "q", no more asteroids or no more lives.
        """
        asteroids_count = len(self.game.get_asteroids())
        lives_count     = self.game.get_num_lives()
        title = "Ending game!"
        ending = False
        
        if self.game.should_end():
            ending = True
            message = "Too bad. Maybe come again later?"
        elif asteroids_count == 0:
            ending = True
            message = "You won! You destroyed all of the asteroids!!"
        elif lives_count == 0:
            ending = True
            message = "You lost :( You have no more lives"
        
        if ending:
            self.game.show_message(title, message)
            self.game.end_game()

def main():
    runner = GameRunner()
    runner.run()

if __name__ == "__main__":
    main()
