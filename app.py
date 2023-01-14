import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        goal = request.form["goal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(goal),
            temperature=1,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(goal):
    prompt =  """Create an outline of a vertical list consisting of some ways to achieve the goal

Goal: Cat suggestions
Suggestions: 
1. Provide adequate food and water 

2. Provide a clean, comfortable environment 

3. Establish a consistent routine 

4. Provide enrichment activities 

5. Monitor health and seek veterinarian care as needed

6. Monitor health and seek veterinarian care as needed

7. Monitor health and seek veterinarian care as needed

Goal: Dog suggestions
Suggestions: 
1. Positive reinforcement training 

2. Establish a consistent routine 

3. Provide adequate exercise and mental stimulation 

4. Properly socialize 

5. Address any behavior issues promptly

6. Address any behavior issues promptly

7. Address any behavior issues 

8. Address any behavior issues promptly


Goal: Promotion suggestions
Suggestions: 
1. Increase knowledge in relevant areas 

2. Network and build relationships 

3. Take on additional responsibilities 

4. Demonstrate initiative and leadership 

5. Proactively seek feedback and performance reviews


Goal: {}
Suggestions:
""".format(goal.capitalize())
    return prompt.replace(",", "\n")
