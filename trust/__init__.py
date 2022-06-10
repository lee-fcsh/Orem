#pylint: disable=import-error
"Module to create the app in Otree, experimental economy functions are developed."
from otree.api import *


DOC = """Simple trust game  Economy Experiment"""

class C(BaseConstants): # pylint: disable=locally-disabled, invalid-name
    "Constants for the game simple trust game"
    NAME_IN_URL = 'trust'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(10)
    MULTIPLIER = 3

class Subsession(BaseSubsession):
    "Classes needed for the experiment"


class Group(BaseGroup):
    """This class contains,
    arguments for the amount the player sends and the amount the player receives
    return none
    """
    sent_amount = models.CurrencyField(
        min=cu(0),
        max=C.ENDOWMENT,
        label="How much do you want to send to participant B?",
    )
    sent_back_amount = models.CurrencyField(
        label="How much do you want to send back?"
    )


class Player(BasePlayer):
    "This class contains the participants of the experiment"
    sent_amount = models.CurrencyField()
    sent_back_amount = models.CurrencyField()

# FUNCTIONS
def sent_back_amount_choices(group: Group):
    """this function is to fill the dropdown dynamically
       return the range
    """
    return currency_range(0, group.sent_amount * C.MULTIPLIER, 1)


def set_payoffs(group: Group):
    """
    function so that they can calculate the payments of the players
    arguments: player, player2,  are group player
    Return:None
    """
    player = group.get_player_by_id(1)
    player2 = group.get_player_by_id(2)
    player.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
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


class WaitForplayer(WaitPage):
    "This function waits for other players to respond, return none"

class SendBack(Page):
    """Class representing a SendBack"""
    form_model = 'group'
    form_fields = ['sent_back_amount']

def is_displayed(player: Player):
    "We use is_displayed() to only show this to player; P2 skips the page"
    return player.id_in_group == 2

def vars_for_template(player: Player):
    """We use vars_for_template() to pass the variable tripled_amount to the template,
    return a map key value"""
    group = player.group
    return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)

class ResultsWaitPage(WaitPage):
    "This function waits for other players to respond, return none"
    after_all_players_arrive = set_payoffs


class Results(Page):
    "this class fills the results page, return none"


page_sequence = [Send, WaitForplayer, SendBack, ResultsWaitPage, Results]
