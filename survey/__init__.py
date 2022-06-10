"Module to create the app in Otree, experimental economy functions are developed."
from otree.api import *

doc = "Survey Economy Experiment"

class C(BaseConstants):
    "constants for the game Survey"
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    "Classes needed for the experiment"
    pass


class Group(BaseGroup):
    "Classes needed for the experiment"
    pass


class Player(BasePlayer):
    "This class contains the participants of the experiment, state name and age, return none"
    name = models.StringField(label='What is your name?')
    age = models.IntegerField(label='What is your age?')


# FUNCTIONS
# PAGES
class Survey(Page):
    "This class for the page with the forms, return none"
    form_model = 'player'
    form_fields = ['name', 'age']


class Results(Page):
    "this class fills the results page, return none"
    form_model = 'player'
   


page_sequence = [Survey, Results]
