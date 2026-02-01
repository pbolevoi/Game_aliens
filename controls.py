import pygame
import sys
from bullet import Bullet
from alien import Alien
import time


def events(screen, gun, bullets):
    """обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:  # вправо
                gun.mright = True
            elif event.key == pygame.K_LEFT:  # влево
                gun.mleft = True
            elif event.key == pygame.K_SPACE:  # пуля
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:  # вправо
                gun.mright = False
            elif event.key == pygame.K_LEFT:  # влево
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, aliens, bullets):
    """обновление экрана"""

    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output_gun()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, aliens, bullets):
    """обновление позиции пуль"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += 10
        sc.image_score()
        check_high_score(stats, sc)
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def update_aliens(stats, screen, gun, aliens, bullets):
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, gun, aliens, bullets)
    aliens_check(stats, screen, gun, aliens, bullets)


def aliens_check(stats, screen, gun, aliens, bullets):
    """проверка конечной точки 'game over'"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, aliens, bullets)
            break


def gun_kill(stats, screen, gun, aliens, bullets):
    """столкновение пушки(смерть)"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_new_gun()
        time.sleep(1.5)
    else:
        stats.run_game = False
        sys.exit()


def create_army(screen, aliens):
    """армия пришельцев"""

    alien = Alien(screen)
    alien_widht = alien.rect.width + 2.5
    number_alien_x = int((700 - 2 * alien_widht) / alien_widht)
    alien_height = alien.rect.height
    number_alien_y = int((700 - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):

        for number_alien in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_widht + alien_widht * number_alien
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)


def check_high_score(stats, sc):
    """check new records"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
