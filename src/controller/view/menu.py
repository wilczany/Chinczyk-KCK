import curses

import npyscreen


class GameParams:
    players_count = int()


class Menu(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm('MAIN', MainForm())
        self.registerForm('PLAYERS_COUNT', PlayerForm())
        # self.registerForm('GAME', GameForm())

    def onCleanExit(self):
        curses.endwin()

class MainForm(npyscreen.ActionFormMinimal):
    choices = ['Graj', 'Wyjdz']

    # choises = ['Graj lokalnie', 'Graj przez siec', 'Wyjdz']

    def create(self):

        self.add(npyscreen.TitleText, name='Witaj w grze Chińczyk', editable=False)
        self.choice = self.add(npyscreen.TitleSelectOne, max_height=4, name='Wybierz opcje',
                               values=self.choices)

    def on_ok(self):
        if self.choice.get_selected_objects()[0] == 'Graj':
            self.parentApp.switchForm('PLAYERS_COUNT')
        else:
            self.parentApp.setNextForm(None)


class PlayerForm(npyscreen.ActionFormV2, npyscreen.Popup):

    def create(self):
        self.add(npyscreen.TitleText, name="Podaj liczbe graczy", editable=False)
        self.count = self.add(npyscreen.Slider, out_of=4, lowest=2, value=2, name="Gracze")

    def on_ok(self):
        GameParams.players_count = int(self.count.value)
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')


class GameForm(npyscreen.ActionFormV2):

    def create(self):
        self.names = []
        for i in range(self.parentApp.s):
            self.names.append(self.add(npyscreen.TitleText, name="Podaj imie gracza " + str(i + 1)))


