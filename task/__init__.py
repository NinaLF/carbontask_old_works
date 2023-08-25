import random
import json

from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'task'
    PLAYERS_PER_GROUP = None
    payment_per_correct_answer = .1
    FOOTPRINT_COMBINATIONS = [
        ['This person follows a <b>vegetarian diet.</b>', 'They have <b>renewable-based heating</b>', 'They <b> recycle everything comprehensively </b>',
         'They buy and consume <b>only regional food</b>', 'They commute the 20km to work <b>by bike</b>', 'This person <b> does not fly </b> to go on vacation'],
        ['This person follows a <b>vegetarian diet.</b>', 'They have <b>renewable-based heating</b>', 'They <b> recycle everything comprehensively </b>',
         'They buy and consume <b>regional and imported food</b>', 'They commute the 20km to work <b>by bus</b>',	'This person <b> does not fly </b> to go on vacation'],
        ['This person follows an <b>omnivorous diet.</b>',	'They have <b>renewable-based heating</b>',	'They <b> do not specifically recycle</b>',
         'They buy and consume <b>regional and imported food</b>',	'They commute the 20km to work <b>by bike</b>',	'This person <b> does not fly </b> to go on vacation'],
        ['This person follows an <b>omnivorous diet.</b>', 'They have <b>renewable-based heating</b>',	'They <b> do not specifically recycle</b>',
         'They buy and consume <b>only regional food</b>', 'They commute the 20km to work <b>by bus</b>', 'This person <b> does not fly </b> to go on vacation'],
        ['This person follows a <b>vegetarian diet.</b>', 'They have <b>gas or oil-based heating</b>', 'They <b> do not specifically recycle</b>',
         'They buy and consume <b>only regional food</b>', 'They commute the 20km to work <b>by bike</b>', 'This person <b> does not fly </b> to go on vacation'],
        ['This person follows a <b>vegetarian diet.</b>', 'They have <b>renewable-based heating</b>',	'They <b> do not specifically recycle</b>',
            'They buy and consume <b>regional and imported food</b>',	'They commute the 20km to work <b>by bike</b>',	'To go on vacation this person <b>flies twice a year</b>'],
        ['This person follows a <b>vegetarian diet.</b>', 'They have <b>gas or oil-based heating</b>', 'They <b> do not specifically recycle</b>',
         'They buy and consume <b>regional and imported food</b>',	'They commute the 20km to work <b>by bus</b>',	'This person <b> does not fly </b> to go on vacation'],
        ['This person follows an <b>omnivorous diet.</b>', 'They have <b>gas or oil-based heating</b>',	'They <b> recycle everything comprehensively </b>',
         'They buy and consume <b>regional and imported food</b>', 'They commute the 20km to work <b>by bike</b>',	'This person <b> does not fly </b> to go on vacation'],
        ['This person follows a <b>vegetarian diet.</b>', 'They have <b>renewable-based heating</b>', 'They <b> do not specifically recycle</b>',
         'They buy and consume <b>only regional food</b>',	'They commute the 20km to work <b>by bus</b>',	'To go on vacation this person <b>flies twice a year</b>'],
        ['This person follows an <b>omnivorous diet.</b>',	'They have <b>renewable-based heating</b>',	'They <b> recycle everything comprehensively </b>',
         'They buy and consume <b>only regional food</b>',	'They commute the 20km to work <b>by bike</b>',	'To go on vacation this person <b>flies twice a year</b>'],
        ['This person follows an <b>omnivorous diet.</b>',	'They have <b>gas or oil-based heating</b>',	'They <b> recycle everything comprehensively </b>',
         'They buy and consume <b>only regional food</b>',	'They commute the 20km to work <b>by bus</b>',	'This person <b> does not fly </b> to go on vacation'],
        ['This person follows an <b>omnivorous diet.</b>',	'They have <b>renewable-based heating</b>', 'They <b> recycle everything comprehensively </b>',
         'They buy and consume <b>regional and imported food</b>',	'They commute the 20km to work <b>by bus</b>',	'To go on vacation this person <b>flies twice a year</b>'],
        ['This person follows a <b>vegetarian diet.</b>',	'They have <b>gas or oil-based heating</b>',	'They <b> recycle everything comprehensively </b>',
         'They buy and consume <b>regional and imported food</b>', 'They commute the 20km to work <b>by bike</b>', 'To go on vacation this person <b>flies twice a year</b>'],
        ['This person follows a <b>vegetarian diet.</b>',	'They have <b>gas or oil-based heating</b>',	'They <b> recycle everything comprehensively </b>',
         'They buy and consume <b>only regional food</b>', 'They commute the 20km to work <b>by bus</b>', 'To go on vacation this person <b>flies twice a year</b>'],
        ['This person follows an <b>omnivorous diet.</b>',	'They have <b>gas or oil-based heating</b>',	'They <b> do not specifically recycle</b>',
         'They buy and consume <b>only regional food</b>',	'They commute the 20km to work <b>by bike</b>',	'To go on vacation this person <b>flies twice a year</b>'],
        ['This person follows an <b>omnivorous diet.</b>',	'They have <b>gas or oil-based heating</b>',	'They <b> do not specifically recycle</b>',
         'They buy and consume <b>regional and imported food</b>',	'They commute the 20km to work <b>by bus</b>', 'To go on vacation this person <b>flies twice a year</b>']
    ]
    FOOTPRINT_COMBINATIONS_TABLE = [
        ['<b>vegetarian diet</b>', '<b>renewable-based heating</b>', '<b> recycle everything comprehensively </b>',
         '<b>only regional food</b>', '<b>by bike</b>', '<b> does not fly </b> '],
        ['<b>vegetarian diet</b>', '<b>renewable-based heating</b>', '<b> recycle everything comprehensively </b>',
         '<b>regional and imported food</b>', '<b>by bus</b>','<b> does not fly </b> '],
        ['<b>omnivorous diet</b>','<b>renewable-based heating</b>','<b> do not specifically recycle</b>',
         '<b>regional and imported food</b>','<b>by bike</b>','<b> does not fly </b> '],
        ['<b>omnivorous diet</b>', '<b>renewable-based heating</b>','<b> do not specifically recycle</b>',
         '<b>only regional food</b>', '<b>by bus</b>', '<b> does not fly </b> '],
        ['<b>vegetarian diet</b>', '<b>gas or oil-based heating</b>', '<b> do not specifically recycle</b>',
         '<b>only regional food</b>', '<b>by bike</b>', '<b> does not fly </b> '],
        ['<b>vegetarian diet</b>', '<b>renewable-based heating</b>','<b> do not specifically recycle</b>',
            '<b>regional and imported food</b>','<b>by bike</b>',' <b>flies twice a year</b>'],
        ['<b>vegetarian diet</b>', '<b>gas or oil-based heating</b>', '<b> do not specifically recycle</b>',
         '<b>regional and imported food</b>','<b>by bus</b>','<b> does not fly </b> '],
        ['<b>omnivorous diet</b>', '<b>gas or oil-based heating</b>','<b> recycle everything comprehensively </b>',
         '<b>regional and imported food</b>', '<b>by bike</b>','<b> does not fly </b> '],
        ['<b>vegetarian diet</b>', '<b>renewable-based heating</b>', '<b> do not specifically recycle</b>',
         '<b>only regional food</b>','<b>by bus</b>',' <b>flies twice a year</b>'],
        ['<b>omnivorous diet</b>','<b>renewable-based heating</b>','<b> recycle everything comprehensively </b>',
         '<b>only regional food</b>','<b>by bike</b>',' <b>flies twice a year</b>'],
        ['<b>omnivorous diet</b>','<b>gas or oil-based heating</b>','<b> recycle everything comprehensively </b>',
         '<b>only regional food</b>','<b>by bus</b>','<b> does not fly </b> '],
        ['<b>omnivorous diet</b>','<b>renewable-based heating</b>', '<b> recycle everything comprehensively </b>',
         '<b>regional and imported food</b>','<b>by bus</b>',' <b>flies twice a year</b>'],
        ['<b>vegetarian diet</b>','<b>gas or oil-based heating</b>','<b> recycle everything comprehensively </b>',
         '<b>regional and imported food</b>', '<b>by bike</b>', ' <b>flies twice a year</b>'],
        ['<b>vegetarian diet</b>','<b>gas or oil-based heating</b>','<b> recycle everything comprehensively </b>',
         '<b>only regional food</b>', '<b>by bus</b>', ' <b>flies twice a year</b>'],
        ['<b>omnivorous diet</b>','<b>gas or oil-based heating</b>','<b> do not specifically recycle</b>',
         '<b>only regional food</b>','<b>by bike</b>',' <b>flies twice a year</b>'],
        ['<b>omnivorous diet</b>','<b>gas or oil-based heating</b>','<b> do not specifically recycle</b>',
         '<b>regional and imported food</b>','<b>by bus</b>', ' <b>flies twice a year</b>']
    ]
    NUM_ROUNDS = len(FOOTPRINT_COMBINATIONS)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rating0 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], widget=widgets.RadioSelectHorizontal,
                                  label='On a scale from 1 to 10, how carbon intensive do you think these behaviors are in total ?')
    vignetteNumber = models.IntegerField(initial= 0)
    order_behavior_types = models.StringField()
   

# FUNCTIONS
# for random order of tasks
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(0, C.NUM_ROUNDS))
            random.shuffle(round_numbers)
            p.participant.task_rounds = round_numbers

# for this all to work, need to add 'task_rounds' as PARTICIPANT_FIELDS in settings.py!!
# PAGES

class task_page00(Page):

    # 0 is diet, 1 is heating, 2 is recycling, 3 is regional food, 4 is commute, 5 vacation
    form_model = 'player'
    form_fields = ['rating0']
    @staticmethod
    def vars_for_template(player: Player):
        # this determines which vignette
        task_in_round = player.participant.task_rounds[player.round_number - 1]
        player.vignetteNumber = task_in_round
        my_vignette = C.FOOTPRINT_COMBINATIONS[task_in_round]
        my_vignette_table = C.FOOTPRINT_COMBINATIONS_TABLE[task_in_round]
        # this determines which order within vignette
        random_behavior_order = list(range(0,6))
        random.shuffle(random_behavior_order)
        current_footprint_shuffled = []
        current_footprint_table_shuffled = []
        behavior_types = ["Diet", "Heating", "Recycling", "Food", "Commute", "Vacation"]
        order_behavior_types = []
        for i in random_behavior_order:
            current_footprint_shuffled.append(my_vignette[i])
            current_footprint_table_shuffled.append(my_vignette_table[i])
            order_behavior_types.append(behavior_types[i])
        player.order_behavior_types = str(order_behavior_types)
        return {
            "current_footprint" : current_footprint_shuffled,
            "current_footprint_table": current_footprint_table_shuffled,
            "random_behavior_order": random_behavior_order
        }


# Page sequence
page_sequence = [
    task_page00
]
