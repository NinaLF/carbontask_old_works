
from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'carbon_footprint_assessment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    CARBON_FOOTPRINT = {
        'footprint_1': { '1': 0.59, '2': 0.44 , '3':0.3 , '4': 0.15, '5': 0.04},
        'footprint_2': {'1': 1.73, '2': 1.16, '3': 0.58, '4': 0.28, '5':0.11, '6': 0.03 } ,
        'footprint_3': { '1': 0.12, '2': 0.1 , '3':0.05 , '4': 0.03 },
        'footprint_4': {'1': 1.45, '2': 1.21, '3':0.63, '4': 0.34, '5':0.14, '6': 0.06 } ,
        'footprint_5': { '1': 0.01, '2': -0.05 , '3': -0.1 },
        'footprint_6': {'1': 0.17, '2': 0, '3': -0.1}  ,

        'footprint_7': {'1': 5.6, '2': 3.73, '3': 1.87, '4': 0.93, '5':0.37, '6': 0 } ,
        'footprint_8': {'1': 0, '2': -0.97, '3': -1.66, '4': -3.94, '5': -4.22  } ,
        'footprint_9': {'1': 0.7, '2': 0.47, '3': 0, '4': -0.35, '5': -0.47, '6': 0.0 } ,
        'footprint_10': {'1': 0.89, '2': 0.53, '3':0.33, '4': 0.18, '5':0.08, '6': 0.03, '7': 0 } ,
        'footprint_11': {'1': 13.48, '2': 6.74, '3': 3.59, '4': 2.07, '5':0.9, '6': 0.36, '7': 0 } ,
        'footprint_12': {'1': 2.38, '2': 1.19, '3': 0.6, '4': 0.24, '5': 0 } ,

        'footprint_13': {'1': 1.44, '2': 1.11, '3': 1.08, '4': 0.84, '5':0.71, '6': 0.48, '7': 0.2, '8': 0.14, '9': 1.11 } ,
        'footprint_14': {'1': 0.07, '2': -0.18, '3':-0.35, '4': -0.66, '5': -0.75, '6': -0.02} ,
        'footprint_15': {'1': 3.6, '2': 2.82, '3': 1.65, '4': 1.06, '5':0.67, '6': 0.28, '7': -0.11, '8': -0.5, '9': -0.59 } ,
        'footprint_16': {'1': 0.81, '2': 0, '3': -0.26, '4': -0.4, '5': -0.47, '6': -0.52, '7': -0.56 } ,
        'footprint_17': {'1': 0.1, '2': 0.02 }  ,
        'footprint_18': { '1': 0, '2': -0.05 , '3': -0.11 , '4': 0 },

        'footprint_19': {'1': 0.81, '2': 0.41, '3':0.33, '4': 0.16, '5':0.07 } ,
        'footprint_20': {'1': 1.7, '2': 1.13, '3':0.74, '4': 0.43, '5':0.14 } ,
        'footprint_21': {'1': 2.13, '2': 1.42, '3':0.89, '4': 0.53, '5':0.18 } ,
        'footprint_22': {'1': 1.62, '2': 1.08, '3':0.68, '4': 0.27, '5':0.14 } ,



    }



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):


    # questionnaire
    footprint_1 = models.IntegerField(choices=[['1', 'Less than a quarter'],['2', 'About a quarter'],
                                             ['3', 'About half'],['4', 'About three quarters'],
                                             ['5', 'the largest part of my fruit and vegetables is local and seasonal ']],
                                             label = '<b>How much seasonal fruit and vegetables do you purchase?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                             )
    footprint_2 = models.IntegerField(choices=[['1', 'More than four times daily'],['2', '2-4 times daily'],
                                             ['3', '1-2 times daily'],['4', '4-6 times weekly'],
                                             ['5', '1-3 times weekly'], ['6', 'Never']],
                                             label = '<b>How often do you consume milk and dairy products such as yoghurt, cheese, butter, or cream?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                             )
    footprint_3 = models.IntegerField(choices=[['1', 'More than twice a day'],['2', '1-2 times daily'],
                                             ['3', '5-6 times weekly'],['4', 'Never or up to 4 times weekly ']],
                                             label = '<b>How often do you eat eggs or foods containing eggs (e.g., gratins, desserts, mayonnaise)?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                             )
    footprint_4 = models.IntegerField(choices=[['1', 'More than three times daily'],['2', '2-3 times daily'],
                                             ['3', 'once per day'],['4', '4-6 times weekly'],
                                             ['5', '1-3 times weekly '], ['6','less than once a week or never']],
                                             label = '<b>How often do you eat meals containing meat or fish (e.g., spaghetti bolognese, salmon roll, etc.)?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                             )
    footprint_5 = models.IntegerField(choices=[['1', 'Less than a quarter'],['2', 'A quarter to three quarters '],['3', 'I uniquely cook using labeled products ']],
                                             label = '<b>What is the share of labeled products (bio, MSC, Fair Trade) of your total grocery shopping goods?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_6 = models.IntegerField(choices=[['1', 'Several times weekly'],['2', 'It happens every now and then'],['3', 'Practically never ']],
                                             label = '<b>How frequently do you trash food products?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    

    footprint_7 = models.IntegerField(choices=[['1', 'More than 30,000 km'],['2', '12,500 - 30,000 km'],['3', '7,500 - 12,499 km'],
                                             ['4', '2,000 - 7,499 km'], ['5', '1 - 2,000 km'],['6', 'I never use a car or motorcycle']],
                                             label = '<b>How many kilometers do you annually drive in a car or on a motorcycle (outside of work times, both driving and as a passenger)?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_8 = models.IntegerField(choices=[['1', 'Gasoline/Diesel/Hybrid '],['2', 'Natural gas '],['3', 'Biogas'] ,
                                               ['4', 'Electric (conventional energy)'], ['5', 'Electric (green energy)'] ],
                                             label = '<b>Which kind of fuel does your car operate on?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_9 = models.IntegerField(choices=[['1', 'More than 12l/100km (32kWh/100km)'],['2', '9-12l/100km (28kWh/100km)'],['3', '6-8l/100km 100km (20kWh/100km)'],
                                             ['4', '4-5l/100km 100km (14kWh/100km)'], ['5', 'less than 4l/100km (12kWh/100km)'],['6', 'I don’t know']],
                                             label = '<b>What is the real fuel consumption of your private car?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    
    footprint_10 = models.IntegerField(choices=[['1', 'More than 600 km'],['2', '360 - 600 km'],['3', '240 - 359 km'] ,
                                               ['4', '80 -239 km'], ['5', '60 - 79 km'],  ['6', '1 - 59 km '],['7', 'I never use public transport']  ],
                                             label = '<b>How many kilometers do you commute weekly in public transport (train, bus, etc.) or an e-bike? Please calculate all private journeys including the work commute, but not business travels.</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_11 = models.IntegerField(choices=[['1', 'More than 50 hours per year'],['2', '25 - 49 hours per year'],['3', '15 - 24 hours per year'],
                                             ['4', '8 - 14 hours per year'], ['5', '2 - 7 hours per year'],['6', '0.1 - 2 hours per year'], ['7', 'I did not fly in the last five years'] ],
                                             label = '<b>How many hours did you fly by plane in the last five years on average?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_12 = models.IntegerField(choices=[['1', 'More than two weeks per year'],['2', '1 - 2 weeks per year'],['3', '4 - 6 days per year'],
                                             ['4', '1 - 3 days per year'], ['5', 'I have not been on a cruiseship in the last five years '] ],
                                             label = '<b>How many days have you spent on a cruiseship on average in the last five years?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    
    footprint_13 = models.IntegerField(choices=[['1', 'Oil heating'],['2', 'Natural gas heating'],['3', 'Oil heating with solar panel'] ,
                                               ['4', 'Gas heating with solar panel'], ['5', 'District heating'],  ['6', 'Electric heating'],
                                               ['7', 'Heat pump '],['8', 'Wood (pellets, wood plus solar, etc.)'] ,['9', 'I don’t know']   ],
                                             label = '<b>How do you heat your home in the winter?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_14 = models.IntegerField(choices=[['1', 'Year of construction/renovation prior to 1980'],['2', 'year of construction/renovation 1980 - 1990'],
                                                ['3', 'year of construction/renovation 1991 - 2008 '],['4', 'new building after 2009 '], ['5', 'Minergie (low energy home) '], ['6', 'I don’t know']   ],
                                             label = '<b>What is the standard of your house?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_15 = models.IntegerField(choices=[['1', 'More than 300'],['2', '201 - 300'],['3', '151 - 200'],
                                             ['4', '126 - 150'], ['5', '101 - 125'], ['6', '76 - 100'],
                                             ['7', '51 - 75 '], ['8', '30 - 50'],['9', 'smaller than 30 '],],
                                             label = '<b>How large is your apartment/your house (heated square meters (sqm) of apartment and holiday apartments without garage, basement, attic)? </b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_16 = models.IntegerField(choices=[['1', '1'],['2', '2'],['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7 or more' ]  ],
                                             label = '<b>How many people live in your household (you included)?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_17 = models.IntegerField(choices=[['1', 'More than one fridge or freezer'],['2', 'combined fridge or freezer'] ],
                                             label = '<b>Which kind of freezer/fridge do you have in your home?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_18 = models.IntegerField(choices=[['1', 'I don’t have green electricity '],['2', 'I partly use green electricity'] , 
                                                ['3', ' I use green electricity entirely'], ['4', 'I don’t know']   ],
                                             label = '<b>Which share of "green electricity" with the label "naturemade star" do you use?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    

    footprint_19 = models.IntegerField(choices=[['1', 'I spend more than 250 GBP per month on average'],['2', 'I spend about 125 GBP per month on average'],
                                                ['3', 'I spend about 100 GBP per month on average '], ['4', 'I spend about 50 GBP per month on average'], ['5', 'I spend less than 20 GBP per month on average '] ],
                                             label = '<b>Which category best reflects your spending behavior on clothing and shoes?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_20 = models.IntegerField(choices=[['1', 'I spend more than 600 GBP per month'],['2', 'I spend about 400 GBP per month'],['3', 'I spend about 260 GBP per month'],
                                                ['4', 'I spend about 150 GBP per month '], ['5', 'I spend less than 50 GBP per month']  ],
                                             label = 'Which category best reflects your spending behavior for leisure and culture (pets, fitness memberships, magazines, consumer electronics, streaming subscriptions, other hobbies, etc.)?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_21 = models.IntegerField(choices=[['1', 'I spend more than 300 GBP per month'],['2', 'I spend about 200 GBP per month'] ,
                                                ['3', 'I spend about 125 GBP per month '], ['4', 'I spend about 75 GBP per month '], ['5', 'I spend less than 25 GBP per month'] ],
                                             label = '<b>Which category best reflects your spending behavior for furniture and household appliances??</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    footprint_22 = models.IntegerField(choices=[['1', 'I spend more than 600 GBP per month'],['2', 'I spend about 400 GBP per month'] , 
                                                ['3', 'I spend about 250 GBP per month'], ['4', 'I spend about 100 GBP per month '] , ['5', 'I spend less than 50 GBP per month']   ],
                                             label = '<b>Which category best reflects your spending behavior for restaurants, canteens, or take-aways, as well as nights spend elsewhere (hotels, airnbn, etc.)?</b>',
                                             widget=widgets.RadioSelectHorizontal,
                                              )
    total_co2 = models.FloatField()

    def calculate_total_co2(self):
        total_co2 = 0
        for field_name, choice in self.__dict__.items():
            if field_name.startswith('footprint_'):
                question = field_name
                selected_choice = str(choice)
                co2_value = C.CARBON_FOOTPRINT.get(question, {}).get(selected_choice, 0)
                total_co2 += co2_value
        return total_co2
        


# FUNCTIONS



# PAGES

class questions_food(Page):
    form_model = 'player'
    form_fields = ['footprint_1', 'footprint_2', 'footprint_3', 'footprint_4', 'footprint_5', 'footprint_6']

class questions_transport(Page):
    form_model = 'player'
    form_fields = ['footprint_7']


class questions_transport2(Page):
    form_model = 'player'
    form_fields = [ 'footprint_8', 'footprint_9']
    
    @staticmethod
    def is_displayed(player: Player):
        return player.footprint_7 != 'I never use a car or motorcycle'
    ## not working!! still shows it regardless
    
class questions_transport3(Page):
    form_model = 'player'
    form_fields = [ 'footprint_10', 'footprint_11', 'footprint_12']

class questions_household(Page):
    form_model = 'player'
    form_fields = [ 'footprint_13', 'footprint_14', 'footprint_15', 'footprint_16', 'footprint_17', 'footprint_18']


class questions_consumption(Page):
    form_model = 'player'
    form_fields = [  'footprint_19', 'footprint_20', 'footprint_21', 'footprint_22']
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        footprint_total = player.calculate_total_co2()  # Calculate the total CO2 emissions
        player.total_co2 = round(footprint_total, 1)  # Store the total in the player's field


       
class display_footprint(Page):
    form_model = 'player'
    form_fields = ['total_co2']

    def get_form_fields(self):
        # Make the total_co2 field read-only
        return ['total_co2']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            'total_co2': player.total_co2
        }
    




# Page sequence
page_sequence = [
    questions_food,
    questions_transport, questions_transport2, questions_transport3,
    questions_household,
    questions_consumption,
    display_footprint

    
]




