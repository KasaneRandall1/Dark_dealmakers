import random,pygame

class resolve_attack():
    def __init__(self,screen) -> None:
        self.player_roll = 0
        self.cpu_roll = 0
        self.display = screen
        self.font = pygame.font.Font(None,30)

    def resolve(self,player_field:list,cpu_field:list,player_hp:int,cpu_hp:int,attacks:list):
        self.p_hp = player_hp
        self.c_hp = cpu_hp
        self.p_field = player_field.copy()
        self.c_field = cpu_field.copy()
        self.p_survival = []
        self.c_survival = []
        self.p_dead = []
        self.c_dead = []
        self.p_attacked = []
        self.c_attacked = []

        for self.i in attacks:
            if self.i[0] not in self.p_dead or self.i[1] not in self.c_dead:
                self.__roll_dice()
                self.__set_matches()
                if self.i[0] not in self.p_attacked:
                    self.p_attacked.append(self.i[0])
                if self.i[1] not in self.c_attacked:
                    self.c_attacked.append(self.i[1])
        self.p_attacked.sort(reverse=True)
        self.c_attacked.sort(reverse=True)

        for i in self.p_attacked:
            self.p_field.pop(i)
        for i in self.c_attacked:
            self.c_field.pop(i)
        
        for i in self.p_field:
            self.p_survival.append(i)
        for i in self.c_field:
            self.c_survival.append(i)
        
        player_field = self.p_survival.copy()
        cpu_field = self.c_survival.copy()
        player_hp = self.p_hp
        cpu_hp = self.c_hp

        return player_field,cpu_field,player_hp,cpu_hp
    
    def __set_matches(self):
        if self.player_roll > self.cpu_roll:
            if self.p_field[self.i[0]] not in self.p_survival:
                self.p_survival.append(self.p_field[self.i[0]])
            if self.c_field[self.i[1]] in self.c_survival:
                self.c_survival.remove(self.c_field[self.i[1]])
            self.c_dead.append(self.c_field[self.i[1]])
            self.c_hp -= (self.player_roll-self.cpu_roll)
            self.p_hp += (self.player_roll-self.cpu_roll)

        elif self.player_roll < self.cpu_roll:
            if self.c_field[self.i[1]] not in self.c_survival:
                self.c_survival.append(self.c_field[self.i[1]])
            if self.p_field[self.i[0]] in self.p_survival:
                self.p_survival.remove(self.p_field[self.i[0]])
            self.p_dead.append(self.p_field[self.i[0]])
            self.c_hp += (self.cpu_roll-self.player_roll)
            self.p_hp -= (self.cpu_roll-self.player_roll)
        
        if self.player_roll-self.cpu_roll > 0:
            player_color = (0,255,255)
            cpu_color = (255,0,0)
        elif self.player_roll-self.cpu_roll == 0:
            player_color = (255,255,255)
            cpu_color = (255,255,255)
        else:
            player_color = (255,0,0)
            cpu_color = (0,255,255)
        player_hp_change = self.font.render(f"{self.player_roll-self.cpu_roll}",True,player_color)
        cpu_hp_change = self.font.render(f"{self.cpu_roll-self.player_roll}",True,cpu_color)

        self.display.blit(player_hp_change,(1025,50))
        self.display.blit(cpu_hp_change,(1225,50))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.draw.rect(self.display,(0,0,0),(1025,50,30,30))
        pygame.draw.rect(self.display,(0,0,0),(1225,50,30,30))
        pygame.display.flip()

    def __roll_dice(self):
        self.player_roll = random.randint(1,6) + random.randint(1,6)
        self.cpu_roll = random.randint(1,6) + random.randint(1,6)
        self.__draw_roll()

    def __draw_roll(self):
        player_roll_pos = [(25,520),(225,520),(425,520),(625,520),(825,520)]
        cpu_roll_pos = [(25,370),(225,370),(425,370),(625,370),(825,370)]
        if self.player_roll > self.cpu_roll:
            player_color = (0,255,255)
            cpu_color = (255,0,0)
        elif self.player_roll == self.cpu_roll:
            player_color = (255,255,255)
            cpu_color = (255,255,255)
        else:
            player_color = (255,0,0)
            cpu_color = (0,255,255)
        player_dice_roll_value = self.font.render(f"{self.player_roll}",True,player_color)
        cpu_dice_roll_value = self.font.render(f"{self.cpu_roll}",True,cpu_color)
        self.display.blit(player_dice_roll_value,player_roll_pos[self.i[0]])
        self.display.blit(cpu_dice_roll_value,cpu_roll_pos[self.i[1]])
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.draw.rect(self.display,(0,0,0),(player_roll_pos[self.i[0]][0],player_roll_pos[self.i[0]][1],30,30))
        pygame.draw.rect(self.display,(0,0,0),(cpu_roll_pos[self.i[1]][0],cpu_roll_pos[self.i[1]][1],30,30))
        pygame.display.flip()
        