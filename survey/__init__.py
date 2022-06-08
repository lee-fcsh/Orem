"""Module ntpath python version."""
from otree.api import *

DOC = "DESCRIPTION"

class C(BaseConstants):
    """Class representing a C"""
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    """Class representing a Subsession"""


class Group(BaseGroup):
    """Class representing a Group"""


class Player(BasePlayer):
    """Class representing a Player"""
    name = models.StringField(label='What is your name?')
    age = models.IntegerField(label='What is your age?')


# FUNCTIONS
# PAGES
class Survey(Page):
    """Class representing a Survey"""
    form_model = 'player'
    form_fields = ['name', 'age']


class Results(Page):
    """Class representing a Results"""
    form_model = 'player'
   


page_sequence = [Survey, Results]
