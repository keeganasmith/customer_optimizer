import sys
import os
sys.path.append(os.getcwd())
from questions.Question import Question, Questions
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
        "packages": {"12 oz cans" : 1}
    },
    20 : {
        "brands" : {},
        "packages": {"Glass 8oz": 1}
    }
}
restaurant_options = [
    "Quick Serve", 
    "Full Serve",
    "Bar/Tavern"]
restaurant_option_biases = {
    "Quick Serve": {
        "brands": {},
        "packages" : {}
    },
    "Full Serve": {
        "brands": {},
        "packages" : {}
    },
    "Bar/Tavern": {
        "brands": {},
        "packages": {"Bar gun": 1}
    }
}

type_of_food_options = [
    "Burger", "Pizza", "Mexican"
]
type_of_food_biases = {
    "Burger": {
        "brands" : {},
        "packages" : {}
    },
    "Pizza": {
        "brands": {},
        "packages" : {}
    },
    "Mexican" : {
        "brands" : {},
        "packages" : {}
    }
}

food_question = Question(title = "Types of food sold", question_type="checkbox", options = type_of_food_options, option_biases=type_of_food_biases)
demographic_question = Question(title = "Customer Ethnicity", question_type="checkbox", options = demographic_options, option_biases=demographic_option_biases)
volume_question = Question(title="Outlet Volume", question_type="number", description="Enter the total volume for this outlet. If this is a new outlet please enter 0.", option_biases=volume_option_biases)
restaurant_options = Question(title="Type of Restaurant", question_type="dropdown", options = restaurant_options, option_biases=restaurant_option_biases)
my_questions = Questions()
my_questions.add_question(demographic_question)
my_questions.add_question(volume_question)
my_questions.add_question(restaurant_options)
my_questions.add_question(food_question)
