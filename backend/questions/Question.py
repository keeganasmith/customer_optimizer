import pickle
from constants import PACKAGES, BRANDS
#question types: checkbox, number, dropdown
class Question:
    def __init__(self, title = "", description = "", question_type = "", options = None, option_biases = None):
        self.title = title
        self.description = description
        self.question_type = question_type
        self.options = options
        self.option_biases = {}
        if(self.options):
            for temp_option in self.options:
                self.option_biases[temp_option] = {}
                self.option_biases[temp_option]["packages"] = {}
                self.option_biases[temp_option]["brands"] = {}
                for package in PACKAGES:
                    self.option_biases[temp_option]["packages"][package] = 0
                for brand in BRANDS:
                    self.option_biases[temp_option]["brands"][brand] = 0
            #self.option_biases.update(option_biases)
            if(option_biases):
                for option in self.options:
                    other_package_biases = option_biases[option]["packages"]
                    other_brand_biases = option_biases[option]["brands"]
                    for package in list(other_package_biases.keys()):
                        self.option_biases[option]["packages"][package] = other_package_biases[package]
                    for brand in list(other_brand_biases.keys()):
                        self.option_biases[option]["brands"][brand] = other_brand_biases[brand]
            print(self.option_biases)
        else:
            self.option_biases = option_biases
    def to_dict(self):
        return self.__dict__
    def __eq__(self, other_question):
        if(isinstance(other_question, Question) and self.title == other_question.title):
            return True
        return False
    def from_dict(self, dictionary):
        for key in list(dictionary.keys()):
            setattr(self, key, dictionary[key])
    
    def return_biases(self, answer):
        brands = {}
        packages = {}
        if(self.question_type == "checkbox"):
            for item in answer:
                bias = self.option_biases[item]
                for brand in list(bias["brands"].keys()):
                    if(not (brand in brands)):
                        brands[brand] = 0
                    brands[brand] += bias["brands"][brand]
                for package in list(bias["packages"].keys()):
                    if(not (package in packages)):
                        packages[package] =0
                    packages[package] += bias["packages"][package]
        if(self.question_type == "dropdown"):
            brands = self.option_biases[answer]["brands"]
            packages = self.option_biases[answer]["packages"]
        if(self.question_type == "number"):
            answer = float(answer)
            sorted_keys = sorted(list(self.option_biases.keys()))
            for key in sorted_keys:
                if answer < key:
                    brands = self.option_biases[key]["brands"]
                    packages = self.option_biases[key]["packages"]
                    break;
        return {"brands": brands, "packages": packages}
class Questions:
    def __init__(self, questions_file_path = "./questions/questions.pickle"):
        try:
            with open(questions_file_path, "rb") as my_file:
                question_dictionaries = pickle.load(my_file)
        except:
            print("file for questions not found. Creating one")
            with open(questions_file_path, "wb") as my_file:
                pickle.dump([], my_file)
                question_dictionaries = []
            
        self.questions = []
        self.questions_file_path = questions_file_path
        for question_dict in question_dictionaries:
            my_question = Question()
            my_question.from_dict(question_dict)
            self.questions.append(my_question)
    def load_questions(self):
        curr_questions = []
        with open(self.questions_file_path, "rb") as my_file:
            question_dictionaries = pickle.load(my_file)
            for question_dict in question_dictionaries:
                my_question = Question()
                my_question.from_dict(question_dict)
                curr_questions.append(my_question)
        return curr_questions
    def write_questions(self, curr_questions):
        with open(self.questions_file_path, "wb") as my_file:
            question_dicts = []
            for question in curr_questions:
                question_dict = question.to_dict()
                question_dicts.append(question_dict)
            pickle.dump(question_dicts, my_file)
    def check_if_question_exists(self, curr_questions, question):
        for temp_question in curr_questions:
            if(question == temp_question):
                return True
        return False
    def add_question(self, question): #takes a question object
        curr_questions = self.load_questions()
        already_exists = self.check_if_question_exists(curr_questions, question)
        if(already_exists):
            self.edit_question(question)
            return False
        curr_questions.append(question)
        self.write_questions(curr_questions)
        return True
    def get_question(self, question_title):
        curr_questions = self.load_questions()
        for question in curr_questions:
            if(question.title == question_title):
                return question
        return None
    def remove_question(self, question):
        curr_questions = self.load_questions()
        for i in range(0, len(curr_questions)):
            if(curr_questions[i] == question):
                del curr_questions[i]
                self.write_questions(curr_questions)
                return True
        return False
    def remove_question_from_title(self, question_title):
        curr_questions = self.load_questions()
        for i in range(0, len(curr_questions)):
            if(curr_questions[i].title == question_title):
                del curr_questions[i]
                self.write_questions(curr_questions)
                return True
        return False
    def edit_question(self, question):
        curr_questions = self.load_questions()
        for i in range(0, len(curr_questions)):
            if(curr_questions[i] == question):
                curr_questions[i] = question
                self.write_questions(curr_questions)
                return True
        return False
    
    def get_questions(self):
        curr_questions = self.load_questions()
        return curr_questions
    
    def get_questions_as_dict(self):
        curr_questions = self.load_questions()
        result = []
        for question in curr_questions:
            result.append(question.to_dict())
        return result;