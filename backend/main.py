from flask import Flask, jsonify, request
from flask_cors import CORS
from questions.Question import Questions, Question
app = Flask(__name__)
cors = CORS(app)
my_questions = Questions()
@app.route('/retrieve_questions', methods=["GET"])
def retrieve_questions():
    result = my_questions.get_questions_as_dict()
    return jsonify(result), 200
@app.route('/retrieve_question_types', methods=["GET"])
def retrieve_question_types():
    return jsonify(["checkbox", "dropdown", "number"]), 200
@app.route('/retrieve_customer_recommendations', methods=["GET"])
def retrieve_customer_recommendations():
    question_answers = request.args.to_dict()
    
    for key in list(question_answers.keys()):
        question = my_questions.get_question(key)
        if(question.question_type == "checkbox"):
            question_answers[key] = question_answers[key].split(',')
            for i in range(0, len(question_answers[key])):
                question_answers[key][i] = question_answers[key][i].strip()
    
    brand_options = {}
    package_options = {}
    
    current_questions = my_questions.get_questions()
    for question in current_questions:
        question_answer = question_answers[question.title]
        question_points = question.return_biases(question_answer)
        for package in list(question_points["packages"].keys()):
            if(not (package in package_options)):
                package_options[package] = 0
            package_options[package] += question_points["packages"][package]
        for brand in list(question_points["brands"].keys()):
            if(not (brand in brand_options)):
                brand_options[brand] = 0
            brand_options[brand] += question_points["brands"][brand]
    result = {
        "brands": sorted(brand_options.items(), key=lambda x: x[1], reverse=True),
        "packages" : sorted(package_options.items(), key=lambda x: x[1], reverse=True)
    }
    print("result was, ", result)
    return jsonify(result), 200
@app.route('/create_or_edit_question', methods=["POST"])
def create_or_edit_question():
    #title = "", description = "", question_type = "", options = None, option_biases = None
    title = request.args.get("title")
    description = request.args.get("description")
    question_type = request.args.get("question_type")
    options = request.args.get("options")
    option_biases = request.args.get("option_biases")
    new_question = Question(title, description, question_type, options, option_biases)
    my_questions.add_question(new_question)
    return 200
@app.route('/', methods=["GET"])
def home():
    return "Hello world", 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)