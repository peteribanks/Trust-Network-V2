from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

#MyPage is now Information1
class Information1(Page):
    '''this is just an intro page it takes the promised percentage and informs the player about their own characteristics
    such as their amount of starting money and multiplier'''
    form_model = 'player'
    form_fields = ['promise']

#WaitPage1 First WaitPage between Information1 and Information2
class WaitPage1(WaitPage):
    '''wait page so that information can all be collected before pages that use
    them. such as investment and return investment'''
    def after_all_players_arrive(self):
        pass


class WaitPage2(WaitPage):
    def after_all_players_arrive(self):
        '''assigns the amount invested in self as the diffrence between endowment and amount invested'''
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        player1.investment1 = (player1.endowment - player1.investment1 - player1.investment2 - player1.investment3 - player1.investment4)
        player2.investment2 = (player2.endowment - player2.investment1 - player2.investment2 - player2.investment3 - player2.investment4)
        player3.investment3 = (player3.endowment - player3.investment1 - player3.investment2 - player3.investment3 - player3.investment4)
        player4.investment4 = (player4.endowment - player4.investment1 - player4.investment2 - player4.investment3 - player4.investment4)


class MyPageWaitPage(Page):
    '''this is only used on the first page to assign the multiplier and and starting money'''
    timeout_seconds = 1 #amount of time spent on page. player shouldnt even realize this page happened
    def before_next_page(self):
        '''if you want to change the parameters for the endowment or starting money do that here'''
        self.player.cp = random.randint(1,10)
        self.player.endowment = random.randint(50, 500)

class FinalPage(Page):
    '''page that prints results for player'''
    def vars_for_template(self):
        '''tells django the python variables that it will be using'''
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        players = [player1, player2, player3, player4] #list of players
        Final_Page_Var = {} #creates a dictonary of variables

        for player in players:
            #this is a for loop that runs through the list of players for various variables and created them.
            #similar process is used for the other for loops the only thing changed is the varables being created
            playernum = players.index(player) + 1 #uses the list of players as a way to find the player number
            string = 'promise%s' % (playernum) #defined promises for each player
            Final_Page_Var[string] = player.promise

        for player in players:
            playernum = players.index(player) + 1
            #since there are four players who each have return variables to each of the other players
            #this defined the 16 return combonations
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
    '''this page is used to defined the investment stage'''
    def vars_for_template(self):
        '''collects the player ids'''
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')
        #defines the variables for django
        players = [player1, player2, player3, player4]
        Final_Page_Var = {}

        for player in players:
            playernum = players.index(player) + 1
            string = 'promise%s' %(playernum) #pulls promises and adds them to dictonary
            Final_Page_Var[string] = player.promise

        for player in players:
            playernum = players.index(player) + 1
            string = 'player%scp' % (playernum) #pulls multiplier and adds them to dictonary
            Final_Page_Var[string] = player.cp

        for player in players:
            playernum = players.index(player) + 1
            string1 = 'p%snetworks' % (playernum) #pulls network and adds them to dictonary
            string2 = 'player%s' % (playernum)
            Final_Page_Var[string1] = self.player.network()[string2]


        return Final_Page_Var #return django variables



    form_model = 'player'
    form_fields = ['investment1', 'investment2', 'investment3', 'investment4']



    def error_message(self, values):
        '''throws up an error if you try to invest more money than you have '''
        investment1 = values['investment1']
        if investment1 == None:
            investment1 = 0
        investment2 = values['investment2']
        if investment2 == None:
            investment2 = 0
        investment3 = values['investment3']
        if investment3 == None:
            investment3 = 0
        investment4 = values['investment4']
        if investment4 == None:
            investment4 = 0

        if investment1 + investment2 + investment3 + investment4 > self.player.endowment:
            return 'You invested more money than you have'

class InvestmentReturn(Page):
    '''takes back how much money someone wants to return'''


    form_model = 'player'
    form_fields = ['return1', 'return2', 'return3', 'return4']



    def vars_for_template(self):
        '''similar process of defining variables as other page classes'''
        player1 = self.group.get_player_by_role('player1')
        player2 = self.group.get_player_by_role('player2')
        player3 = self.group.get_player_by_role('player3')
        player4 = self.group.get_player_by_role('player4')

        players = [player1, player2, player3, player4]
        Final_Page_Var = {}

        for player in players:
            if player == player1:
                player.investment_in_me_ag = player1.investment1ag + player2.investment1ag + player3.investment1ag + player4.investment1ag
            elif player == player2:
                player.investment_in_me_ag = player1.investment2ag + player2.investment2ag + player3.investment2ag + player4.investment2ag
            elif player == player3:
                player.investment_in_me_ag = player1.investment3ag + player2.investment3ag + player3.investment3ag + player4.investment3ag
            else:
                player.investment_in_me_ag = player1.investment4ag + player2.investment4ag + player3.investment4ag + player4.investment4ag

        for player in players:
            playernum = players.index(player) + 1
            string1 = 'p%snetworks' % (playernum)
            string2 = 'player%s' % (playernum)
            Final_Page_Var[string1] = self.player.network()[string2]

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
            if playernum != 1 and player.investment1 != None:
                player.investment1ag = player.investment1 * player1.cp
            else:
                player.investment1 = player.investment1ag

            if playernum != 2 and player.investment2 != None:
                player.investment2ag = player.investment2 * player2.cp
            else:
                player.investment2 = player.investment2ag

            if playernum != 3 and player.investment3 != None:
                player.investment3ag = player.investment3 * player3.cp
            else:
                player.investment3 = player.investment3ag

            if playernum != 4 and player.investment4 != None:
                player.investment4ag = player.investment4 * player4.cp
            else:
                player.investment4 = player.investment4ag

            string1 = 'player%s_investment1ag' % (playernum)
            string2 = 'player%s_investment2ag' % (playernum)
            string3 = 'player%s_investment3ag' % (playernum)
            string4 = 'player%s_investment4ag' % (playernum)

            Final_Page_Var[string1] = player.investment1ag
            Final_Page_Var[string2] = player.investment2ag
            Final_Page_Var[string3] = player.investment3ag
            Final_Page_Var[string4] = player.investment4ag

        for player in players:
            playernum = players.index(player) + 1
            string1 = 'p%snetworks' % (playernum)
            string2 = 'player%s' % (playernum)
            Final_Page_Var[string1] = self.player.network()[string2]



        return Final_Page_Var


    def before_next_page(self):
        '''defines the players final money by taking the amount of money invest minus the amount given back'''
        self.player.final_total_money = self.player.investment_in_me_ag - self.player.return1 - self.player.return2 - self.player.return3 - self.player.return4

    def error_message(self, values):
        '''throws up an error message if the player is trying to return more money than they have'''
        return1 = values['return1']
        if return1 == None:
            return1 = 0
        return2 = values['return2']
        if return2 == None:
            return2 = 0
        return3 = values['return3']
        if return3 == None:
            return3 = 0
        return4 = values['return4']
        if return4 == None:
            return4 = 0

        if return1 + return2 + return3 + return4 > self.player.investment_in_me_ag:
            return 'You are trying to return too much money'





#tells django what order to show the pages in
page_sequence = [
    MyPageWaitPage,
    Information1,
    WaitPage1,
    Invest,
    WaitPage2,
    InvestmentReturn,
    WaitPage1,
    FinalPage
]