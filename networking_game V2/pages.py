from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

#MyPage is now Information1
class Information1(Page):
    form_model = 'player'
    form_fields = ['promise']

#WaitPage1 First WaitPage between Information1 and Information2
class WaitPage1(WaitPage):
    def after_all_players_arrive(self):
        pass

class MyPageWaitPage(Page):
    timeout_seconds = 1
    def before_next_page(self):
        self.player.cp = random.randint(1,10)
        self.player.endowment = random.randint(50, 500)

class FinalPage(Page):
    def vars_for_template(self):
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        players = [player1, player2, player3, player4]
        Final_Page_Var = {}

        for player in players:
            playernum = players.index(player) + 1
            string = 'promise%s' % (playernum)
            Final_Page_Var[string] = player.promise

        for player in players:
            playernum = players.index(player) + 1
            string1 = 'player%s_return1' % (playernum)
            string2 = 'player%s_return2' % (playernum)
            string3 = 'player%s_return3' % (playernum)
            string4 = 'player%s_return4' % (playernum)

            Final_Page_Var[string1] = player.return1
            Final_Page_Var[string2] = player.return2
            Final_Page_Var[string3] = player.return3
            Final_Page_Var[string4] = player.return4


        for player in players:
            playernum = players.index(player) + 1
            string1 = 'p%snetworks' % (playernum)
            string2 = 'player%s' % (playernum)
            Final_Page_Var[string1] = self.player.network()[string2]


        return Final_Page_Var

class Invest(Page):
    def vars_for_template(self):
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        players = [player1, player2, player3, player4]
        Final_Page_Var = {}

        for player in players:
            playernum = players.index(player) + 1
            string = 'promise%s' %(playernum)
            Final_Page_Var[string] = player.promise

        for player in players:
            playernum = players.index(player) + 1
            string = 'player%scp' % (playernum)
            Final_Page_Var[string] = player.cp

        for player in players:
            playernum = players.index(player) + 1
            string1 = 'p%snetworks' % (playernum)
            string2 = 'player%s' % (playernum)
            Final_Page_Var[string1] = self.player.network()[string2]

        return Final_Page_Var

    form_model = 'player'
    form_fields = ['investment1', 'investment2', 'investment3', 'investment4']

class InvestmentReturn(Page):

    form_model = 'player'
    form_fields = ['return1', 'return2', 'return3', 'return4']

    def vars_for_template(self):
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        players = [player1, player2, player3, player4]
        Final_Page_Var = {}

        for player in players:
            playernum = players.index(player) + 1
            string1 = 'player%s_investment1' % (playernum)
            string2 = 'player%s_investment2' % (playernum)
            string3 = 'player%s_investment3' % (playernum)
            string4 = 'player%s_investment4' % (playernum)

            Final_Page_Var[string1] = player.investment1
            Final_Page_Var[string2] = player.investment2
            Final_Page_Var[string3] = player.investment3
            Final_Page_Var[string4] = player.investment4


        for player in players:
            playernum = players.index(player) + 1
            string1 = 'p%snetworks' % (playernum)
            string2 = 'player%s' % (playernum)
            Final_Page_Var[string1] = self.player.network()[string2]

        return Final_Page_Var


class Information2(Page):
    pass



page_sequence = [
    MyPageWaitPage,
    Information1,
    WaitPage1,
    Information2,
    WaitPage1,
    Invest,
    WaitPage1,
    InvestmentReturn,
    WaitPage1,
    FinalPage
]