from flask import Flask, jsonify, request
from flask_cors import CORS
from questions.Question import Questions, Question
from constants import PACKAGES, BRANDS
app = Flask(__name__)
cors = CORS(app)
my_questions = Questions()
@app.route('/retrieve_questions', methods=["GET"])
def retrieve_questions():
    result = my_questions.get_questions_as_dict()
    return jsonify(result), 200
@app.route('/retrieve_question_types', methods=["GET"])
def retrieve_question_types():
    return jsonify(["checkbox", "dropdown"]), 200
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
    return jsonify(result), 200
@app.route('/create_or_edit_question', methods=["POST"])
def create_or_edit_question():
    #title = "", description = "", question_type = "", options = None, option_biases = None
    question_json = request.get_json()
    curr_question = Question()
    curr_question.from_dict(question_json)
    my_questions.add_question(curr_question)
    return jsonify({"status": 200})
@app.route('/remove_question', methods=["POST"])
def remove_question():
    payload = request.get_json()
    question_title = payload["title"]
    my_questions.remove_question_from_title(question_title)
    return jsonify({"status": 200})
@app.route('/', methods=["GET"])
def home():
    return "Hello world", 200
@app.route('/get_package_options', methods=["GET"])
def get_package_options():
    return jsonify(PACKAGES), 200
@app.route('/get_brand_options', methods=["GET"])
def get_brand_options():
    return jsonify(BRANDS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)