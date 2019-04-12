from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Banks and Fraser'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Trust_Network_Game'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    endowment = models.IntegerField(blank=True)
    cp = models.IntegerField(blank=True)
    promise = models.IntegerField(blank=True)

    investment1 = models.IntegerField(blank=True)
    investment2 = models.IntegerField(blank=True)
    investment3 = models.IntegerField(blank=True)
    investment4 = models.IntegerField(blank=True)

    return1 = models.IntegerField(blank=True)
    return2 = models.IntegerField(blank=True)
    return3 = models.IntegerField(blank=True)
    return4 = models.IntegerField(blank=True)

    def network(self):
        network = {'player1': [2, 4], 'player2': [1, 3, 4], 'player3': [2, 4], 'player4': [1, 3, 2]}

        return network

    def role(self):
        if self.id_in_group == 1:
            return 'player1'
        if self.id_in_group == 2:
            return 'player2'
        if self.id_in_group == 3:
            return 'player3'
        if self.id_in_group == 4:
            return 'player4'





