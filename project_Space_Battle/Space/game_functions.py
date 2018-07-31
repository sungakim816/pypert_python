import sys
import pygame
from Space.bullet import Bullet
from Space.alien import Alien
from time import sleep


def check_keydown_event(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.is_moving_right = True
    elif event.key == pygame.K_a:
        ship.is_moving_left = True
    elif event.key == pygame.K_w:
        ship.is_moving_up = True
    elif event.key == pygame.K_s:
        ship.is_moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_event(ship):
    ship.is_moving_down = ship.is_moving_up = ship.is_moving_left = ship.is_moving_right = False


def check_events(game_settings, screen, stats, score, play_button, ship, aliens, bullets):
    """Respond to keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_event(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, score, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(game_settings, screen, stats, score, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        # Reset Game Statistics
        stats.reset_stats()
        stats.game_active = True
        # Reset Score Board Images
        score.prep_score()
        score.prep_high_score()
        score.prep_level()
        # Empty the alien and bullets
        bullets.empty()
        aliens.empty()
        create_alien_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
    else:
        pygame.mouse.set_visible(True)


def update_screen(game_settings, stats, score, screen, ship, aliens, bullets, play_button):
    screen.fill(game_settings.bg_color)
    # Redraw all bullets behind ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    score.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def update_bullets(game_settings, stats, score, screen, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(game_settings, stats, score, screen, ship, aliens, bullets)
    number_aliens = len(aliens)
    if number_aliens == 0:
        # Destroy existing bullets and create a new fleet
        game_settings.increase_speed()
        bullets.empty()
        create_alien_fleet(game_settings, screen, ship, aliens)
        # Start a new Level
        stats.level += 1
        score.prep_level()


def create_alien_fleet(game_settings, screen, ship, aliens):
    """Create an Entire Alien Fleet"""
    # Create an Alien and Find the number of aliens in a row
    # Spacing between aliens is equal to one alien width
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(game_settings, alien_width)

    # Create First Row of Aliens
    for row_number in range(4):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(game_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = game_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(game_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(game_settings, stats, score, screen, ship, aliens, bullets):
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, score, screen, ship, aliens, bullets)
    check_aliens_bottom(game_settings, stats, score, screen, ship, aliens, bullets)


def check_fleet_edges(game_settings, aliens):
    """Respond Appropriately if an aliens have reach an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    """Drop the entire fleet and change it's direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def check_bullet_alien_collisions(game_settings, stats, score, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if collisions:
        stats.score += game_settings.alien_points
        score.prep_score()
    check_high_score(stats, score)


def ship_hit(game_settings, stats, score, screen, ship, aliens, bullets):
    # Decrement Ship Life
    if stats.ship_life > 0:
        stats.ship_life -= 1
        # update sccore board
        score.prep_ships()
        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create New Alien Fleet and center the ship
        create_alien_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(game_settings, stats, score, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, score, screen, ship, aliens, bullets)


def check_high_score(stats, score):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.prep_high_score()
