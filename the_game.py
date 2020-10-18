import sys
from sprites import *

pg.init()
print("start")

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(FPS) / 1000
        # pg.key.set_repeat(500, 100)
        self.bout = 0
        self.bout_list = []
        self.player1_moves = []
        self.player2_moves = []
        self.all_sprites = pg.sprite.Group()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.player1 = Player(self, 2, FLOOR, RED, ['P1ATK', 'P1DEF', 'P1BCK', 'P1FWD'])
        self.player2 = Player(self, 7, FLOOR, BLUE, ['P2ATK', 'P2DEF', 'P2BCK', 'P2FWD'])
        print("End of NEW")
        return g.run()

    def run(self):
        # game loop - set self.playing = False to end the game
        playing = True
        while playing:
            # DEAD_CHECK
            if g.player1.x < 0:
                return g.encore()
            if g.player2.x > 9:
                return g.encore()

            # BOUT_CHECK
            if len(self.bout_list) == 6:
                self.bout += 1
                print("BOUT #" + str(self.bout))
                print(self.bout_list)
                self.calc_bout(self.bout_list)
                self.bout_list.clear()
                print(self.player1.x, self.player2.x)

            # START ROUND n!
            self.events()
            # get 6 events / 3 inputs from each user or ai
            self.update()
            # register data
            self.draw()
            # show change

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

                # KEYDOWN
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

                if event.key == pg.K_p:
                    print(self.bout_list)
                if event.key == pg.K_r:
                    restart = Game()
                    restart.intro()

                # MOVE
                if event.key == pg.K_a:
                    self.bout_list.append('P1BCK')
                if event.key == pg.K_d:
                    self.bout_list.append('P1FWD')
                if event.key == pg.K_LEFT:
                    self.bout_list.append('P2FWD')
                if event.key == pg.K_RIGHT:
                    self.bout_list.append('P2BCK')
                if event.key == pg.K_w:
                    self.bout_list.append('P1ATK')
                if event.key == pg.K_UP:
                    self.bout_list.append('P2ATK')
                if event.key == pg.K_s:
                    self.bout_list.append('P1DEF')
                if event.key == pg.K_DOWN:
                    self.bout_list.append('P2DEF')

    def calc_bout(self, lst):
        #print(self.player1.actions)
        #print(self.player2.actions)
        for x in lst:
            if x in self.player1.actions:
                self.player1_moves.append(x)
            if x in self.player2.actions:
                self.player2_moves.append(x)
        self.zip_up = list(zip(self.player1_moves, self.player2_moves))
        print(self.zip_up)
        for y in self.zip_up:
            print(self.player1.x, self.player2.x)
            self.execute(list(y))
        self.zip_up.clear()
        self.player1_moves.clear()
        self.player2_moves.clear()

    def execute(self, z):
        ## How do I show each y update individually (animation)?
        #print(z)
        print(z[0], z[1])
        if self.player2.x - self.player1.x == 1:
            if z == ['P1DEF', 'P2ATK'] or ['P1ATK', 'P2FWD'] or ['P1ATK', 'P2BCK'] or ['P1DEF', 'P2BCK']:
                self.player2.move(dx=1)
            if z == ['P1ATK', 'P2DEF'] or ['P1FWD', 'P2ATK'] or ['P1BCK', 'P2ATK'] or ['P1BCK', 'P2DEF']:
                self.player1.move(dx=-1)
            if z == ['P1ATK', 'P2ATK'] or ['P1BCK', 'P2BCK']:
                self.player2.move(dx=1)
                self.player1.move(dx=-1)
            if z == ['P1FWD', 'P2BCK'] or ['P1FWD', 'P2DEF']:
                self.player2.move(dx=1)
                self.player1.move(dx=1)
            if z == ['P1BCK', 'P2FWD'] or ['P1DEF', 'P2FWD']:
                self.player2.move(dx=-1)
                self.player1.move(dx=-1)
            if z == ['P1FWD', 'P2FWD'] or ['P1DEF', 'P2DEF']:
                print("nothing_melee")
        if self.player2.x - self.player1.x > 1:
            if z == ['P1ATK', 'P2BCK'] or ['P1DEF', 'P2BCK']:
                self.player2.move(dx=1)
            if z == ['P1BCK', 'P2ATK'] or ['P1BCK', 'P2DEF']:
                self.player1.move(dx=-1)
            if z == ['P1ATK', 'P2FWD'] or ['P1ATK', 'P2FWD']:
                self.player2.move(dx=-1)
            if z == ['P1FWD', 'P2ATK'] or ['P1FWD', 'P2DEF']:
                self.player1.move(dx=1)
            if z == ['P1BCK', 'P2BCK']:
                self.player2.move(dx=1)
                self.player1.move(dx=-1)
            if z == ['P1FWD', 'P2BCK']:
                self.player2.move(dx=1)
                self.player1.move(dx=1)
            if z == ['P1BCK', 'P2FWD']:
                self.player2.move(dx=-1)
                self.player1.move(dx=-1)
            if z == ['P1FWD', 'P2FWD']:
                self.player2.move(dx=-1)
                self.player1.move(dx=1)
            elif z == ['P1ATK', 'P2ATK'] or ['P1DEF', 'P2DEF'] or ['P1DEF', 'P2ATK'] or ['P1ATK', 'P2DEF']:
                print("nothing_range")

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        ##self.draw_grid()
        self.screen.fill(BACKGROUND)
        self.all_sprites.draw(g.screen)
        pg.display.flip()

    '''
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, GREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, GREY, (0, y), (WIDTH, y))
    '''

    def intro(self):
        print("Welcome to August Falls")
        small_font = pg.font.SysFont(None, 30)
        text = small_font.render("WELCOME TO AUGUST FALLS! Press any key to continue", True, BLACK)
        text_width = text.get_width()
        text_height = text.get_height()

        # blit production intro fade to background.png
        print("--INTRO--")
        pg.time.wait(100)
        print("+++++++++")

        curtain = True
        while curtain is True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                # elif event.type == pg.click(new_game)
                # g.new()
                elif event.type == pg.KEYDOWN:
                    curtain = False
            self.screen.fill(BACKGROUND)
            self.screen.blit(text, [int((WIDTH - text_width) / 2), int((HEIGHT - text_height) / 2)])
            # time delay blit sprites for
            #   bg, title, new_game, HUD
            # buttons for new_game, HUD
            pg.display.update()

    def debut(self):
        self.screen.fill(BACKGROUND)
        # fill from intro without time delay
        #   bg, title, new_game, HUD
        new_game = True
        print("New Game?")
        if new_game is True:
            # for event in pg.event.get():
            # if event.type == pg.click(new_game):
            return self.new()
        else:
            pass

    def encore(self):
        # bg
        # play_again
        big_font = pg.font.SysFont(None, 100)
        text = big_font.render("!!!DEAD!!!", True, BLACK)
        text_width = text.get_width()
        text_height = text.get_height()

        pg.time.wait(0)

        redrum = True
        while redrum is True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                # elif event.type == pg.click(play_again)
                # g.new()
                elif event.type == pg.KEYDOWN:
                    self.all_sprites.empty()
                    return self.debut()
            self.screen.fill(RED)
            self.screen.blit(text, [int((WIDTH - text_width) / 2), int((HEIGHT - text_height) / 2)])
            pg.display.update()
            pg.time.wait(1995)


# create the game object
g = Game()
g.intro()
while True:
    g.debut()
    g.run()
    g.encore()
