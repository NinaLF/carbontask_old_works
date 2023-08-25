from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):


    def make_field(label):
        return models.IntegerField(
        choices=[['6', 'Agree completely'], ['5', 'Agree'], ['4', 'Somewhat agree '], 
                 ['3', 'Somehat disagree'], ['2', 'Disagree'], ['1', 'Completely disagree'] ],                                
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

    # questionnaire
    climate_change_concern1 = make_field('I concerned')
    climate_change_concern2 = make_field('I xxx')
    climate_change_concern3 = make_field('I do not')
    climate_change_concern4 = make_field('I  ')


# FUNCTIONS
# PAGES

class cc_concern(Page):
    form_model = 'player'
    form_fields = ['climate_change_concern1', 'climate_change_concern2', 'climate_change_concern3', 'climate_change_concern4']
class policy_support(Page):
    form_model = 'player'
    form_fields = []
    



# Page sequence
page_sequence = [
    cc_concern  #,   policy support  
]
