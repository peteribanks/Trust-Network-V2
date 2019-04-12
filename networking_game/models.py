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
    '''this defines the characteristics of the player class including the variables'''
    endowment = models.IntegerField(blank=True, initial=0)  #amount of starting money
    cp = models.IntegerField(blank=True, initial=0) #multiplier used for investing in others
    promise = models.IntegerField(min=0, max=100, initial=0) #percent that is promised as a return. This also ensures that the numebr will between 0 and 100

    #'''this is used to define the investments for the players'''
    investment1 = models.IntegerField(blank=True, initial=0) #investment in player 1
    investment1ag = models.IntegerField(blank=True, initial=0) #worth of investment in player 1 after it is multipleid by cp
    investment2 = models.IntegerField(blank=True, initial=0) #same for each of the created players
    investment2ag = models.IntegerField(blank=True, initial=0)
    investment3 = models.IntegerField(blank=True, initial=0)
    investment3ag = models.IntegerField(blank=True, initial=0)
    investment4 = models.IntegerField(blank=True, initial=0)
    investment4ag = models.IntegerField(blank=True, initial=0)

    return1 = models.IntegerField(blank=True, initial=0) #amount returned to players 1 through n
    return2 = models.IntegerField(blank=True, initial=0)
    return3 = models.IntegerField(blank=True, initial=0)
    return4 = models.IntegerField(blank=True, initial=0)

    investment_in_me_ag = models.IntegerField(blank=True, initial=0)
    #total amount invested in each player after multiplication. equals
    #investment1 for all players for player 1. this is used as an error checker for returning money to ensure that people done return more money than they are allowed to'''

    final_total_money = models.IntegerField(blank=True, initial=0) #this is the amount of money left over after the player has returned'''

    def network(self):
        network = {'player1': [2, 4], 'player2': [1, 3, 4], 'player3': [2, 4], 'player4': [1, 3, 2]}
        #'''this is the network if the key player1 has a list containing the
         #integers 1 and 4 it means they are networked with players 1 and four and so on'''

        return network

    def role(self):
        '''this function assigns the player ids used in multiple locations extremly important dont change ever'''
        if self.id_in_group == 1:
            return 'player1'
        if self.id_in_group == 2:
            return 'player2'
        if self.id_in_group == 3:
            return 'player3'
        if self.id_in_group == 4:
            return 'player4'





