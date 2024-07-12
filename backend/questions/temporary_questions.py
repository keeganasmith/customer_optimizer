import sys
import os
sys.path.append(os.getcwd())
from questions.Question import Question, Questions
brands = ['Coke', 'Coke Zero', 'Diet Coke', 'Sprite', 'Seagram’s', 'MM Lemonade', 'Gold Peak', 'Dasani', 'Coke de Mexico', 'Fanta Orange', 'Topo Chico']
demographic_options = [
    "White", 
    "African American", 
    "Asian American", 
    "Hispanic American"
]

demographic_option_biases = {
    "White" : {
        "brands" : {"Topo Chico": 1},
        "packages": {}
    },
    "African American" : {
        "brands" : {"Coke": 1},
        "packages" : {}
    },
    "Hispanic American": {
        "brands" : {"Fanta Orange": 1},
        "packages" : {}
    },
    "Asian American" : {
        "brands": {"Gold Peak": 1},
        "packages" : {}
    }
}
volume_option_biases = {
    1 : {
        "brands" : {},
        "packages" : {}
    },
    10 : {
        "brands" : {},
        "packages": {"can" : 1}
    },
    20 : {
        "brands" : {},
        "packages": {"glass": 1}
    }
}
restaurant_options = [
    "Fine Dining",
    "Casual Dining",
    "Fast Casual",
    "Fast Food",
    "Buffet",
    "Cafeteria",
    "Food Truck"]
restaurant_option_biases = {
    "Fine Dining" : {
        "brands" : {},
        "packages" : {"glass" : 1}
    },
    "Casual Dining" : {
        "brands" : {},
        "packages" : {"fountain" : 1}
    },
    "Fast Food" : {
        "brands" : {},
        "packages" : {"fountain" : 1}
    },
    "Buffet" : {
        "brands" : {},
        "packages" : {"fountain" : 1}
    },
    "Cafeteria" : {
        "brands" : {},
        "packages" : {"fountain" : 1}
    },
    "Food Truck": {
        "brands" : {},
        "packages" : {"bar gun" : 1, "can" : 1}
    }
}

demographic_question = Question(title = "Customer Ethnicity", question_type="checkbox", options = demographic_options, option_biases=demographic_option_biases)
volume_question = Question(title="Outlet Volume", question_type="number", description="Enter the total volume for this outlet. If this is a new outlet please enter 0.", option_biases=volume_option_biases)
restaurant_options = Question(title="Type of Restaurant", question_type="dropdown", options = restaurant_options, option_biases=restaurant_option_biases)
my_questions = Questions()
my_questions.add_question(demographic_question)
my_questions.add_question(volume_question)
my_questions.add_question(restaurant_options)

