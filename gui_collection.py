import pygame
import os
import imghdr
import random


class main_menu():
    def __init__(self, screen) -> None:
        self.display = screen
        self.background = pygame.image.load("img/main_menu_bg.png")
        self.font = pygame.font.Font(None, 36)
        self.play_but = pygame.Rect(400, 400, 200, 50)
        self.rules_but = pygame.Rect(400, 500, 200, 50)
        self.quit_but = pygame.Rect(400, 600, 200, 50)
        self.play_txt = self.font.render("Play", True, (255, 0, 0))
        self.rules_txt = self.font.render("Rules", True, (255, 0, 0))
        self.quit_txt = self.font.render("Quit", True, (255, 0, 0))
        self.hover_play = False
        self.hover_rules = False
        self.hover_quit = False

    def draw_main_menu(self):
        self.display.blit(self.background, (0, 0))
        if self.hover_play:
            pygame.draw.rect(self.display, (0, 0, 0), self.play_but)
        self.display.blit(self.play_txt, (470, 415))
        if self.hover_rules:
            pygame.draw.rect(self.display, (0, 0, 0), self.rules_but)
        self.display.blit(self.rules_txt, (470, 515))
        if self.hover_quit:
            pygame.draw.rect(self.display, (0, 0, 0), self.quit_but)
        self.display.blit(self.quit_txt, (470, 615))

    def hover_but(self, mouse):
        if self.play_but.collidepoint(mouse):
            self.hover_play = True
        else:
            self.hover_play = False
        if self.rules_but.collidepoint(mouse):
            self.hover_rules = True
        else:
            self.hover_rules = False
        if self.quit_but.collidepoint(mouse):
            self.hover_quit = True
        else:
            self.hover_quit = False


class rules():
    def __init__(self, screen) -> None:
        self.font = pygame.font.Font(None, 30)
        self.display = screen
        self.red = (255, 0, 0)
        self.back_but = pygame.Rect(400, 700, 200, 50)

    def __rule_1(self):
        rule_1_life = self.font.render("1. Life", True, self.red)
        rule_1_hp = self.font.render(
            "Your life points represent your survival.", True, self.red)
        rule_1_play_cost = self.font.render(
            "Playing a card costs life points equal to the card's value. Choose carefully.", True, self.red)
        rule_1_death = self.font.render(
            "If your life points reach zero, you lose the game.", True, self.red)
        self.display.blit(rule_1_life, (10, 20))
        self.display.blit(rule_1_hp, (10, 50))
        self.display.blit(rule_1_play_cost, (10, 80))
        self.display.blit(rule_1_death, (10, 110))

    def __rule_2(self):
        rule_2_combat = self.font.render("2. Combat", True, self.red)
        rule_2_turn = self.font.render(
            "You can only interact on your turn.", True, self.red)
        rule_2_attack = self.font.render(
            "You choose the target for the monster you want to attack with.", True, self.red)
        self.display.blit(rule_2_combat, (10, 150))
        self.display.blit(rule_2_turn, (10, 180))
        self.display.blit(rule_2_attack, (10, 210))

    def __misc(self):
        misc_1 = self.font.render("3. Misc", True, self.red)
        misc_2 = self.font.render(
            "You can't see ahead on the map since you walk through the Abyss of Death", True, self.red)
        misc_2_1 = self.font.render(
            "You can choose from 4 paths without seeing what is ahead of the path.", True, self.red)
        misc_3 = self.font.render(
            "Your Goal is to beat Death, so you can get to the world of the living.", True, self.red)
        misc_4 = self.font.render(
            "Beware the Abyss is full of grotesque monster.", True, self.red)
        self.display.blit(misc_1, (10, 240))
        self.display.blit(misc_2, (10, 270))
        self.display.blit(misc_2_1, (10, 300))
        self.display.blit(misc_3, (10, 330))
        self.display.blit(misc_4, (10, 360))

    def show_rules(self):
        self.display.fill((0, 0, 0))
        self.__rule_1()
        self.__rule_2()
        self.__misc()
        pygame.draw.rect(self.display, self.red, self.back_but)
        back_txt = self.font.render("Back", True, (0, 0, 0))
        self.display.blit(back_txt, (470, 715))


class encounter():
    def __init__(self, screen) -> None:
        self.display = screen
        self.font = pygame.font.Font(None, 30)
        self.advance_but = pygame.Rect(600, 700, 100, 50)
        self.succumb_but = pygame.Rect(200, 700, 100, 50)
        self.img_pulled = False
        self.event_trigger = False
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.__img_grab()

    def __player_health(self, player_hp):
        hp_value = self.font.render(f"HP: {player_hp}", True, self.red)
        self.display.blit(hp_value, (10, 20))

    def __img_grab(self):
        def grab_images_from_folder(folder_path):
            image_files = []
            # Traverse through the folder
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    # Check if the file is an image
                    file_path = os.path.join(root, file)
                    if is_image_file(file_path):
                        image_files.append(file)
            return image_files

        def is_image_file(file_path):
            # Check if the file is an image using imghdr
            image_type = imghdr.what(file_path)
            return image_type is not None
        folder_path = "img/encounter_img/"
        image_files = grab_images_from_folder(folder_path)
        img = random.choice(image_files)
        self.bg = pygame.image.load((folder_path+img))

    def __draw_but(self):
        self.display.blit(self.bg, (0, 0))
        pygame.draw.rect(self.display, self.red, self.succumb_but)
        pygame.draw.rect(self.display, self.red, self.advance_but)
        succumb_txt = self.font.render("SUCCUMB", True, self.black)
        advance_txt = self.font.render("ADVANCE", True, self.black)
        self.display.blit(succumb_txt, (200, 715))
        self.display.blit(advance_txt, (600, 715))

    def __draw_lore(self):
        t1 = "You won against a monster slumbering in the shadow"
        t2 = "But will you go deeper in the Abyss"
        t3 = "You gain some Life if you adventure more"
        t1_render = self.font.render(t1, True, self.red)
        t2_render = self.font.render(t2, True, self.red)
        t3_render = self.font.render(t3, True, self.red)
        self.display.blit(t1_render, (50, 50))
        self.display.blit(t2_render, (50, 80))
        self.display.blit(t3_render, (50, 110))

    def draw_encounter(self, player_hp, monster_defeated):
        self.__draw_but()
        self.__player_health(player_hp)
        self.__draw_lore()
        monster_dead = self.font.render(str(monster_defeated), True, self.red)
        self.display.blit(monster_dead, (1000, 20))


class prologue():
    def __init__(self, screen) -> None:
        self.font = pygame.font.Font(None, 30)
        self.display = screen
        self.move_forwar_but = pygame.Rect(400, 700, 200, 50)
        self.move_forward_txt = self.font.render("Move on", True, (0, 0, 0))
        self.red = (255, 0, 0)

    def show_prologue(self):
        self.display.fill((0, 0, 0))
        txt_1 = self.font.render(
            "In the forgotten corners of reality lies the Abyss, a realm teeming with eldritch horrors,", True, self.red)
        txt_2 = self.font.render(
            "grotesque monster and undescribeable things that defy the feeble understanding of mortals.", True, self.red)
        txt_3 = self.font.render(
            "Whispers of ancient evils echo through the void,", True, self.red)
        txt_4 = self.font.render(
            "drawing the daring and the desperate to its shadowy depths.", True, self.red)
        txt_5 = self.font.render(
            "Death is giving you a chance to escape the Abyss.", True, self.red)
        txt_6 = self.font.render(
            "The Offer itself is twisted. You gain the power to summon whatever is in the Abyss,", True, self.red)
        txt_7 = self.font.render(
            "but you must sacrifice a part of you Life.", True, self.red)
        txt_8 = self.font.render(
            "Will you make it to the End or will you succumb to the Abyss?", True, self.red)
        self.display.blit(txt_1, (10, 20))
        self.display.blit(txt_2, (10, 50))
        self.display.blit(txt_3, (10, 80))
        self.display.blit(txt_4, (10, 110))
        self.display.blit(txt_5, (10, 210))
        self.display.blit(txt_6, (10, 240))
        self.display.blit(txt_7, (10, 270))
        self.display.blit(txt_8, (10, 300))
        pygame.draw.rect(self.display, (self.red), self.move_forwar_but)
        self.display.blit(self.move_forward_txt, (470, 715))


class combat_gui():
    def __init__(self, screen) -> None:
        self.display = screen
        self.font = pygame.font.Font(None, 30)
        self.player_field = []
        self.cpu_field = []
        self.choose_target_1 = True
        self.choose_target_2 = True
        self.target_1 = 10
        self.target_2 = 10
        self.line_pos = []
        self.in_attack_phase = 0
        self.attacks = []
        self.highlite = None

        self.card_1 = pygame.Rect(25, 550, 150, 200)
        self.card_2 = pygame.Rect(225, 550, 150, 200)
        self.card_3 = pygame.Rect(425, 550, 150, 200)
        self.card_4 = pygame.Rect(625, 550, 150, 200)
        self.card_5 = pygame.Rect(825, 550, 150, 200)
        self.player_card_field = [
            self.card_1, self.card_2, self.card_3, self.card_4, self.card_5]

        self.c_field_1 = pygame.Rect(25, 150, 150, 200)
        self.c_field_2 = pygame.Rect(225, 150, 150, 200)
        self.c_field_3 = pygame.Rect(425, 150, 150, 200)
        self.c_field_4 = pygame.Rect(625, 150, 150, 200)
        self.c_field_5 = pygame.Rect(825, 150, 150, 200)
        self.cpu_card_field = [self.c_field_1, self.c_field_2,
                               self.c_field_3, self.c_field_4, self.c_field_5]

    def preload_player_img(self, deck):
        self.loaded_player_img = []
        for i in deck:
            x = pygame.image.load(f"img/player_creature/{i['img_path']}")
            x = pygame.transform.scale(x, (150, 200))
            self.loaded_player_img.append((i["img_path"], x))

    def preload_cpu_img(self, deck):
        self.loaded_cpu_img = []
        for i in deck:
            x = pygame.image.load(f"img/player_creature/{i['img_path']}")
            x = pygame.transform.scale(x, (150, 200))
            self.loaded_cpu_img.append((i["img_path"], x))

    def __create_player_cards(self):
        field_card_img = []
        hand_card_img = []

        self.h_card_1 = pygame.Rect(1025, 200, 150, 200)
        self.h_card_2 = pygame.Rect(1225, 200, 150, 200)
        self.h_card_3 = pygame.Rect(1025, 500, 150, 200)
        self.h_card_4 = pygame.Rect(1225, 500, 150, 200)

        field_card_pos = [self.card_1.topleft, self.card_2.topleft,
                          self.card_3.topleft, self.card_4.topleft, self.card_5.topleft]
        hand_card_pos = [self.h_card_1.topleft, self.h_card_2.topleft,
                         self.h_card_3.topleft, self.h_card_4.topleft]

        if len(self.player_field) != 0:
            for i in self.player_field:
                for f in self.loaded_player_img:
                    if i["img_path"] == f[0]:
                        field_card_img.append(f[1])
        for i in self.p_h_cards:
            for f in self.loaded_player_img:
                if i["img_path"] == f[0]:
                    hand_card_img.append(f[1])

        x = 0
        for i in field_card_img:
            self.display.blit(i, field_card_pos[x])
            x += 1
        x = 0
        for i in hand_card_img:
            self.display.blit(i, hand_card_pos[x])
            x += 1

    def __create_cpu_cards(self):
        field_card_img = []
        c_field_pos = [self.c_field_1.topleft, self.c_field_2.topleft,
                       self.c_field_3.topleft, self.c_field_4.topleft, self.c_field_5.topleft]

        if len(self.cpu_field) != 0:
            for i in self.cpu_field:
                for f in self.loaded_cpu_img:
                    if i["img_path"] == f[0]:
                        field_card_img.append(f[1])
        x = 0
        if len(field_card_img) != 0:
            for i in field_card_img:
                self.display.blit(i, c_field_pos[x])
                x += 1

    def __draw_cards(self):
        self.__create_player_cards()
        self.__create_cpu_cards()

    def __draw_hud(self):
        player_hp = self.font.render(f"hp: {self.hp}", True, (255, 0, 0))
        self.display.blit(player_hp, (1025, 20))
        cpu_hp = self.font.render(f"Enemy hp: {self.c_hp}", True, (255, 0, 0))
        self.display.blit(cpu_hp, (1225, 20))
        self.set_to_atk_but = pygame.Rect(1025, 80, 150, 50)
        self.set_to_end_but = pygame.Rect(1225, 80, 150, 50)
        if self.in_attack_phase == 0:
            set_to_atk_txt = self.font.render("Set", True, (0, 0, 0))
            pygame.draw.rect(self.display, (255, 0, 0), self.set_to_atk_but)
            self.display.blit(set_to_atk_txt, (1050, 95))
        elif self.in_attack_phase == 1:
            set_to_atk_txt = self.font.render("Attack", True, (0, 0, 0))
            pygame.draw.rect(self.display, (255, 0, 0), self.set_to_end_but)
            self.display.blit(set_to_atk_txt, (1250, 95))
        elif self.in_attack_phase == 2:
            set_to_atk_txt = self.font.render("End", True, (0, 0, 0))
            pygame.draw.rect(self.display, (255, 0, 0), self.set_to_atk_but)
            self.display.blit(set_to_atk_txt, (1050, 95))

    def __draw_lines(self):
        if len(self.line_pos) != 0:
            for i in self.line_pos:
                pygame.draw.line(self.display, (255, 0, 0), i[0], i[1])

    def draw_field(self, cpu_hp, player_hp: int, player_hand_cards: list):
        self.hp = player_hp
        self.c_hp = cpu_hp
        self.p_h_cards = player_hand_cards
        self.display.fill((0, 0, 0))
        if self.highlite != None:
            self.__draw_highlight()
        self.__draw_cards()
        self.__draw_hud()
        self.__draw_lines()

    def __draw_highlight(self):
        cards = [self.card_1.topleft, self.card_2.topleft,
                 self.card_3.topleft, self.card_4.topleft, self.card_5.topleft]
        pygame.draw.rect(self.display, (255, 0, 0),
                         (cards[self.highlite][0]-4, cards[self.highlite][1]-4, 158, 208))

    def draw_attack_lines(self):
        p1_cor_cen = [self.card_1.center, self.card_2.center,
                      self.card_3.center, self.card_4.center, self.card_5.center]
        p2_cor_cen = [self.c_field_1.center, self.c_field_2.center,
                      self.c_field_3.center, self.c_field_4.center, self.c_field_5.center]

        self.attacks.append((self.target_1, self.target_2))
        if 0 <= self.target_1 <= 4:
            p1 = p1_cor_cen[self.target_1]
        if 0 <= self.target_2 <= 4:
            p2 = p2_cor_cen[self.target_2]

        if not self.target_1 == 10 or not self.target_2 == 10:
            if (p1, p2) in self.line_pos:
                self.line_pos.remove((p1, p2))
            else:
                self.line_pos.append((p1, p2))

        self.target_1 = 10
        self.target_2 = 10
        self.choose_target_1 = True


class death_screen():
    def __init__(self, screen) -> None:
        self.display = screen
        self.font = pygame.font.Font(None, 50)
        self.main_menu_but = pygame.Rect(10, 10, 200, 50)
        self.death_img = pygame.image.load("img/death_screen.png")
        self.death_msg = self.font.render(
            "YOU      SUCCUMB     TO      DEATH", True, (255, 0, 0))
        self.main_menu_txt = self.font.render("Main Menu", True, (0, 0, 0))

    def draw_end(self):
        self.display.blit(self.death_img, (0, 0))
        self.display.blit(self.death_msg, (200, 50))
        self.display.blit(self.main_menu_txt, (10, 10))
