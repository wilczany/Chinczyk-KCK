import random

from .keyboardHandler import Action, GetUserAction
from src.controller.model.Board import Board
from src.controller.model.Player import Pawn
from src.controller.view.view import GameView
from src.controller.view.view_classes import Message


class LocalGame:

    def __init__(self, players_names: [str]):
        self.players_names = players_names
        self.players = len(players_names)
        self.board = Board(self.players)
        self.view = GameView(self.players)
        self.ac = GetUserAction()

    def start(self):

        end = False
        while not end:

            players_in_game = self.board.get_players()

            for player in range(players_in_game):

                self.view.display_message(Message.PLAYER_TURN, self.players_names[player])
                dice_action = self.ac.get_action()
                while dice_action != Action.SELECT:
                    dice_action = self.ac.get_action()

                dice = random.randint(1, 6)

                self.view.dice_show(dice)

                self.player_move(player, dice)
                if dice == 6:
                    self.view.display_message(Message.EXTRA_TURN, self.players_names[player])
                    self.player_move(player, dice)
                    if dice == 6:
                        self.view.display_message(Message.LOST_TURN, self.players_names[player])

    def player_move(self, player: int, dice: int):
        possible_moves = self.board.get_moves(player, dice)

        cursor_positions = []
        ln = len(possible_moves)
        if ln == 0:
            # view.no_moves(player)
            return

        i = 0
        for pawn in possible_moves:
            if pawn.at_base:
                cursor_positions.append([-1, player])
            elif pawn.at_home:
                cursor_positions.append([pawn.position, player])
            else:
                cursor_positions.append([pawn.position, ])

        action = None

        self.view.set_cursor(*cursor_positions[i])
        while action != Action.SELECT:

            action = self.ac.get_action()
            if action == Action.LEFT:
                i = (i - 1) % ln

                self.view.set_cursor(*cursor_positions[i])

            elif action == Action.RIGHT:
                i = (i + 1) % ln
                self.view.set_cursor(*cursor_positions[i])
        self.view.remove_cursor()
        chosen_pawn = possible_moves[i]

        if chosen_pawn.at_base:
            self.view.move_from_base(player)
        elif chosen_pawn.next_move_finish(dice):
            if chosen_pawn.at_home:
                self.view.finish(player, chosen_pawn.position, True)
            else:
                self.view.finish(player, chosen_pawn.position, False)
        elif chosen_pawn.next_move_home(dice):
            if chosen_pawn.at_home:
                self.view.move_from_h_to_h(player, chosen_pawn.position, chosen_pawn.position + dice)
            else:
                next_pos = (chosen_pawn.position + dice) % 10
                self.view.move_to_home(player, chosen_pawn.position, next_pos)
        else:
            next_pos = (chosen_pawn.position + dice) % 40
            self.view.move_on_track(chosen_pawn.position, next_pos)

        self.board.move(player, chosen_pawn, dice)
