    def _create_fleet(self):
        '''create the fleet of aliens'''
        # make an alien
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        current_x = alien_width

        while current_x < (self.settings.screen_width - 2*alien_width):
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += 2*alien_width