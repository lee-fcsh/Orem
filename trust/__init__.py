"""Module ntpath python version."""
from ntpath import join
from otree.api import *


DOC = """Simple trust game"""

class C(BaseConstants):
    """Class representing a C"""
    NAME_IN_URL = 'trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(10)
    MULTIPLIER = 3

class Subsession(BaseSubsession):
    """Class representing a S"""

class Group(BaseGroup):
    """Class representing a Group"""
    sent_amount = models.CurrencyField(
        min=cu(0),
        max=C.ENDOWMENT,
        label="How much do you want to send to participant B?",
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back?"
    )


class Player(BasePlayer):
    """Class representing a player"""
    sent_amount = models.CurrencyField()
    sent_back_amount = models.CurrencyField()

# FUNCTIONS
def sent_back_amount_choices(group: Group):
    """Function sent_back_amount_choices python version."""
    return currency_range(0, group.sent_amount * C.MULTIPLIER, 1)


def set_payoffs(group: Group):
    """Function payoffs python."""
    player1 = group.get_player_by_id(1)
    player2 = group.get_player_by_id(2)
    player1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    player2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount


# PAGES
class Send(Page):
    """Class representing a Send"""
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def displayed(player: Player):
        """Function displayed."""
        return player.id_in_group == 1


class WaitForP1(WaitPage):
    """Class representing a Wait"""


class SendBack(Page):
    """Class representing a SendBack"""
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def displayed(player: Player):
        """Function displayed python version."""
        return player.id_in_group == 2

    @staticmethod
    def template(player: Player):
        """Function template python version."""
        group = player.group

        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


class ResultsWaitPage(WaitPage):
    """Class representing a result"""
    after_all_players_arrive = set_payoffs


class Results(Page):
    """Class representing a result""" 

page_sequence = [Send, WaitForP1, SendBack, ResultsWaitPage, Results]
