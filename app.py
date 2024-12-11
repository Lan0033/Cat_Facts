from flask import Flask, render_template, request
from Cat import generate_openai_response


app = Flask(__name__)
@app.route("/")
def homepage():
     return render_template("index.html", response="")

@app.route("/", methods=["GET", "POST"])
def index():
    print ("we are here")
    response = ""
    # if request.method == "POST":
    user_question = request.form["user_question"]
    #print(user_question)
    response = generate_openai_response(user_question)
    print(response)
    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)
