from otree.api import *

doc = "DESCRIPTION"

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label='What is your name?')
    age = models.IntegerField(label='What is your age?')


# FUNCTIONS
# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = ['name', 'age']


class Results(Page):
    form_model = 'player'
   


page_sequence = [Survey, Results]
