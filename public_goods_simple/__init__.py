"Module to create the app in Otree, experimental economy functions are developed."
from otree.api import *

doc = 'Public Good Economy Experiment'

class C(BaseConstants):
    "constants for the public good simple"
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 2


class Subsession(BaseSubsession):
    "Classes needed for the experiment"
    pass


class Group(BaseGroup):
    "This class contains the participants of the game with your total of contributions, return none"
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    "this class contains the amount the player can contribute, return none"
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute?"
    )

class Subsession(BaseSubsession):
    """Class representing a S"""

# FUNCTIONS
def set_payoffs(group: Group):
    """
    function so that they can calculate the payments of the players
    arguments: group: Group
    Return:None
    """
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.individual_share = (
        group.total_contribution * C.MULTIPLIER / C.PLAYERS_PER_GROUP
    )
    for p in players:
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share


# PAGES
class Contribute(Page):
    "Form page for contributions, return none"
    form_model = 'player'
    form_fields = ['contribution']



class ResultsWaitPage(WaitPage):
    "This function waits for other players to respond, return none"
    after_all_players_arrive = set_payoffs


class Results(Page):
   "This page contains the result"
   form_model = 'player'


page_sequence = [Contribute, ResultsWaitPage, Results]
