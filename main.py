import pygame
import sys
import player_management
import cpu_managment
import gui_collection
import attack_managment
import music_player

pygame.init()


def main():
    # init display
    screen_width, screen_height = 1000, 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Dark Dealmakers - Pact of Death")
    clock = pygame.time.Clock()

    # init classes
    player = player_management.player()
    cpu = cpu_managment.cpu()
    main_menu_gui = gui_collection.main_menu(screen)
    main_menu_rules = gui_collection.rules(screen)
    encounter_screen = gui_collection.encounter(screen)
    beginning = gui_collection.prologue(screen)
    combat_hud = gui_collection.combat_gui(screen)
    resolver = attack_managment.resolve_attack(screen)
    death = gui_collection.death_screen(screen)
    music = music_player.Music()
    
    # game specific var
    gamestate = 10

    turn = 1
    running = True
    PLAYER_TURN = 1
    CPU_TURN = 2

    MAIN_MENU = 10
    MAIN_MENU_RULES = 11
    ENCOUNTER = 20
    PROLOGUE = 21
    COMBAT = 30
    DEATH = 40

    PLAYER_CARD_COST = 3
    
    music.choose_track()
    # main part
    while running:
        # key inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS:
                    music.vol_up()
                if event.key == pygame.K_KP_MINUS:
                    music.vol_down()
            elif event.type == pygame.USEREVENT:
                music.choose_track()
        if gamestate != COMBAT:
            screen = pygame.display.set_mode((screen_width, screen_height))
        else:
            screen = pygame.display.set_mode((1400, 800))

        # mainmenu logic, loading player img
        if gamestate == MAIN_MENU:
            main_menu_gui.hover_but(pygame.mouse.get_pos())
            main_menu_gui.draw_main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_gui.play_but.collidepoint(pygame.mouse.get_pos()):
                    gamestate = PROLOGUE
                    if len(player.deck) == 0:
                        player.deck_creation()
                        combat_hud.preload_player_img(player.deck_backup)
                elif main_menu_gui.rules_but.collidepoint(pygame.mouse.get_pos()):
                    gamestate = MAIN_MENU_RULES
                elif main_menu_gui.quit_but.collidepoint(pygame.mouse.get_pos()):
                    running = False
                    pygame.quit()
                    sys.exit()

        if gamestate == MAIN_MENU_RULES:
            main_menu_rules.show_rules()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_rules.back_but.collidepoint(pygame.mouse.get_pos()):
                    gamestate = MAIN_MENU

        # game rules, generating cpu deck, loading img,
        if gamestate == PROLOGUE:
            beginning.show_prologue()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if beginning.move_forwar_but.collidepoint(pygame.mouse.get_pos()):
                    gamestate = COMBAT
                    cpu.deck_create()
                    combat_hud.preload_cpu_img(cpu.deck)

        # state after win in combat,cpu reset,player hp reset
        if gamestate == ENCOUNTER:
            encounter_screen.draw_encounter(
                player.health, player.monster_defeated)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if encounter_screen.advance_but.collidepoint(pygame.mouse.get_pos()):
                    player.health += 15
                    cpu.reset()
                    cpu.deck_create()
                    combat_hud.preload_cpu_img(cpu.deck)
                    gamestate = COMBAT
                if encounter_screen.succumb_but.collidepoint(pygame.mouse.get_pos()):
                    player.reset()
                    gamestate = MAIN_MENU

        # combat between player and cpu, turn based
        if gamestate == COMBAT:
            if turn == PLAYER_TURN:
                if not player.cards_drawn:
                    player.draw_hand()
                    player.cards_drawn = True
                    player.set_cards = True

                combat_hud.draw_field(cpu.health, player.health, player.hand)

                if player.health <= 5:
                    player.set_cards = False
                    player.choose_target = True
                    combat_hud.in_attack_phase = 1
                
                #player choosing cards
                if player.set_cards:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if len(combat_hud.player_field) < 5:
                            if combat_hud.h_card_1.collidepoint(pygame.mouse.get_pos()):
                                if 1 <= len(player.hand):
                                    combat_hud.player_field.append(
                                        combat_hud.p_h_cards[0])
                                    player.hand.pop(0)
                                    player.health -= PLAYER_CARD_COST
                            if combat_hud.h_card_2.collidepoint(pygame.mouse.get_pos()):
                                if 2 <= len(player.hand):
                                    player.health -= 5
                                    combat_hud.player_field.append(
                                        combat_hud.p_h_cards[1])
                                    player.hand.pop(1)
                                    player.health -= PLAYER_CARD_COST
                            if combat_hud.h_card_3.collidepoint(pygame.mouse.get_pos()):
                                if 3 <= len(player.hand):
                                    combat_hud.player_field.append(
                                        combat_hud.p_h_cards[2])
                                    player.hand.pop(2)
                                    player.health -= PLAYER_CARD_COST
                            if combat_hud.h_card_4.collidepoint(pygame.mouse.get_pos()):
                                if 4 <= len(player.hand):
                                    combat_hud.player_field.append(
                                        combat_hud.p_h_cards[3])
                                    player.hand.pop(3)
                                    player.health -= PLAYER_CARD_COST
                        if combat_hud.set_to_atk_but.collidepoint(pygame.mouse.get_pos()):
                            player.set_cards = False
                            player.choose_target = True
                            combat_hud.in_attack_phase = 1

                    if len(player.hand) == 0:
                        player.set_cards = False
                        player.choose_target = True
                        combat_hud.in_attack_phase = 1

                # player choosing attacker and targets
                if player.choose_target:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if combat_hud.choose_target_1:
                            for i in range(len(combat_hud.player_field)):
                                if combat_hud.player_card_field[i].collidepoint(pygame.mouse.get_pos()):
                                    combat_hud.target_1 = i
                                    combat_hud.highlite = i
                                    combat_hud.choose_target_1 = False
                                    combat_hud.choose_target_2 = True
                        elif combat_hud.choose_target_2:
                            for i in range(len(combat_hud.cpu_field)):
                                if combat_hud.cpu_card_field[i].collidepoint(pygame.mouse.get_pos()):
                                    combat_hud.target_2 = i
                                    combat_hud.highlite = None
                                    combat_hud.choose_target_2 = False
                                if combat_hud.target_2 == 10:
                                    combat_hud.choose_target_2 = False
                                    combat_hud.choose_target_1 = True
                                    combat_hud.target_1 = 10
                                    combat_hud.target_2 = 10
                                    combat_hud.highlite = None
                                    
                    if combat_hud.choose_target_1 == False and combat_hud.choose_target_2 == False:
                        combat_hud.draw_attack_lines()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if combat_hud.set_to_end_but.collidepoint(pygame.mouse.get_pos()):
                            player.switch_turn = True
                            player.choose_target = False
                            player.set_cards = True
                            combat_hud.choose_target_1 = True
                            combat_hud.in_attack_phase = 2
                            combat_hud.highlite = None

                if player.switch_turn:
                    combat_hud.line_pos.clear()
                    combat_hud.draw_field(
                        cpu.health, player.health, player.hand)
                    if len(combat_hud.attacks) != 0:
                        combat_hud.player_field, combat_hud.cpu_field, player.health, cpu.health = resolver.resolve(
                            combat_hud.player_field, combat_hud.cpu_field, player.health, cpu.health, combat_hud.attacks)
                    player.end_turn()
                    turn = CPU_TURN
                    player.cards_drawn = False
                    player.switch_turn = False
                    combat_hud.in_attack_phase = 0
                    combat_hud.attacks.clear()

                if cpu.health <= 0:
                    player.deck = player.deck_backup.copy()
                    gamestate = ENCOUNTER

                if player.health <= 0:
                    gamestate = DEATH

            if turn == CPU_TURN:
                combat_hud.cpu_field = cpu.play_cards(
                    combat_hud.cpu_field, combat_hud.player_field)
                combat_hud.draw_field(cpu.health, player.health, player.hand)
                combat_hud.player_field, combat_hud.cpu_field, player.health, cpu.health = resolver.resolve(
                    combat_hud.player_field, combat_hud.cpu_field, player.health, cpu.health, cpu.attacks)
                cpu.end_turn()
                cpu.attacks.clear()
                turn = PLAYER_TURN

                if cpu.health <= 0 or len(combat_hud.cpu_field) == 0:
                    player.deck = player.deck_backup.copy()
                    gamestate = ENCOUNTER

                if player.health <= 0:
                    gamestate = DEATH

        if gamestate == DEATH:
            death.draw_end()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if death.main_menu_but.collidepoint(pygame.mouse.get_pos()):
                    player.reset()
                    cpu.reset()
                    gamestate = MAIN_MENU

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
