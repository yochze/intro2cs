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
        #This is where your code goes!
        torpedos_to_remove, asteroids_to_remove = [], []
        self.move_asteroids()
        self.move_ship()
        self.move_torpedos()
        self.shooting_torpedo()
        pairs = self.check_collisions()
        asteroid_colided = self.ship_asteroid_collison()

        if pairs:
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
        min_x, max_x = self.game.get_screen_min_x(), self.game.get_screen_max_x()
        min_y, max_y = self.game.get_screen_min_y(), self.game.get_screen_max_y()

        dx = max_x - min_x
        dy = max_y - min_y
        
        new_cord_x = ((shape.get_speed_x() + shape.get_x_cor()) % dx) + min_x
        new_cord_y = ((shape.get_speed_y() + shape.get_y_cor()) % dy) + min_y

        shape.move(new_cord_x, new_cord_y)

    
    def move_asteroids(self):
        asteroids = self.game.get_asteroids()
        for asteroid in asteroids:
            self.move_object(asteroid)

    def move_ship(self):
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
            
            self.move_object(ship)


    def shooting_torpedo(self):
        torpedos_amount = len(self.game.get_torpedos())
        torpedos_limit = 20

        if self.game.is_fire_pressed() and (torpedos_amount < torpedos_limit):
            ship = self.game.get_ship() 
            x_pos = ship.get_x_cor()
            y_pos = ship.get_y_cor()
            org_deg = ship.get_angle()
            deg_r = math.radians(org_deg)

            x_speed = ship.get_speed_x() + 2 * math.cos(deg_r)
            y_speed = ship.get_speed_y() + 2 * math.sin(deg_r)

            self.game.add_torpedo(x_pos, y_pos, x_speed, y_speed, org_deg)

    def move_torpedos(self):
        torpedos      = self.game.get_torpedos()
        for torpedo in torpedos:
                self.move_object(torpedo)

    def check_collisions(self):
        torpedos  = self.game.get_torpedos()
        asteroids = self.game.get_asteroids()
        colided_list = []

        for torpedo in torpedos:
            for asteroid in asteroids:
                if self.game.intersect(torpedo, asteroid):
                    # Mark asteroid and torpedo to be removed
                    colided_list.append([torpedo, asteroid])

        return colided_list


    def handle_collisons(self, colided_pairs):
        
        score_table = { 3:20, 2:50, 1:100 }

        for torpedo, asteroid in colided_pairs:
            self.game.add_to_score(score_table[asteroid.size])

            if asteroid.size > 1: 
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
        ast_x = asteroid.get_speed_x()
        ast_y = asteroid.get_speed_y()

        tor_x = torpedo.get_speed_x()
        tor_y = torpedo.get_speed_y()

        new_speed_x =  tor_x + ast_x / ( math.sqrt(ast_x**2 + ast_y**2) )
        new_speed_y =  tor_y + ast_y / ( math.sqrt(ast_x**2 + ast_y**2) )

        return(new_speed_x, new_speed_y)

    def get_dead_torpedos(self):
        torpedos            = self.game.get_torpedos()
        dead_torpedos       = []
        life_capacity_limit = 0

        for torpedo in torpedos:
            if torpedo.get_life_span() <= life_capacity_limit:
                dead_torpedos.append(torpedo)
        
        return dead_torpedos


    def remove_asteroids(self, asteroids):
        for asteroid in asteroids:
            self.game.remove_asteroid(asteroid)


    def ship_asteroid_collison(self):
        ship = self.game.get_ship()
        asteroids = self.game.get_asteroids()

        for asteroid in asteroids:
            if self.game.intersect(ship, asteroid):
                return asteroid

    def ship_collison_message(self):
        title = "Collison!"
        message = "Your ship has colided with an asteroid. "

        self.game.show_message(title, message)

    def end_game_conditions(self):

        asteroids_count = len(self.game.get_asteroids())
        lives_count     = self.game.get_num_lives()

        if self.game.should_end() or asteroids_count == 0 or lives_count == 0:
            self.game.end_game()




def main():
    runner = GameRunner()
    runner.run()

if __name__ == "__main__":
    main()
