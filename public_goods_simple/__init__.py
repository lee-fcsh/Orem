"""Module pydocpython version."""
from pydoc import doc
from otree.api import *

DOC = 'Description'

class C(BaseConstants):
    """Class representing a C"""
    NAME_IN_URL = 'public_goods_simple'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 2

class Group(BaseGroup):
    """Class representing a Group"""
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()


class Player(BasePlayer):
    """Class representing a Player"""
    contribution = models.CurrencyField(
        min=0, max=C.ENDOWMENT, label="How much will you contribute?"
    )

class Subsession(BaseSubsession):
    """Class representing a S"""

# FUNCTIONS
def set_payoffs(group: Group):
    """Function et_payoffss python version."""
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
    """Class representing a Contribute"""
    form_model = 'player'
    form_fields = ['contribution']



class ResultsWaitPage(WaitPage):
    """Class representing a  ResultsWaitPage"""
    after_all_players_arrive = set_payoffs


class Results(Page):
    """Class representing a  Results"""
    form_model = 'player'


page_sequence = [Contribute, ResultsWaitPage, Results]
