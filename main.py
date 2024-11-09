from flask import Flask, render_template, request, redirect, url_for, flash
import json


app = Flask(__name__)

@app.route('/')
def quiz():
    """Display the quiz form"""
    questions = load_questions()
    return render_template('quiz.html', questions=questions)

def load_questions():
    """Load questions from questions.json"""
    with open("questions.json", "r", encoding="utf-8") as f:
        return json.load(f)


@app.route('/submit', methods=['POST'])
def submit():
    """Handle quiz submission, final score"""
    questions = load_questions()
    score = 0
    results = []

    # Loop each question
    for question in questions:
        question_id = question["id"]

        # Get user's response for the question
        user_answer_key = request.form.get(f'question_{question_id}')

        # Check if the answer is None
        if user_answer_key is None:
            flash("Please answer all questions before submitting.")
            return redirect(url_for('quiz'))

        # Get the correct answer key from json
        correct_answer_key = question['answerKey']

        # Print user and correct answers for debugging purpose
        print(f"Question ID: {question_id}")
        print(f"User Answer Key: {user_answer_key}")
        print(f"Correct Answer Key: {correct_answer_key}")

        # Find the text of user's selected answer and the correct answer from json
        user_answer_text = next((option['text'] for option in question['options'] if option['key'] == user_answer_key),
                                None)
        correct_answer_text = next(
            (option['text'] for option in question['options'] if option['key'] == correct_answer_key), None)

        # Check if user or correct answer texts are found
        if user_answer_text is None or correct_answer_text is None:
            flash("An error occurred while processing the answers. Please try again.")
            return redirect(url_for('quiz'))

        # Determine if the answer is correct
        is_correct = user_answer_key == correct_answer_key
        if is_correct:
            score += 1

        # Store the results for each question
        results.append({
            "question": question["question"],
            "user_answer": user_answer_text,
            "correct_answer": correct_answer_text,
            "is_correct": is_correct
        })

    # Render the results page with the final score
    return render_template('results.html', score=score, results=results, total=len(questions))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8082)
