from flask import Flask, render_template, request
import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "GEMINI_API_KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

app = Flask(__name__)

def format_fitness_plan(text):
    lines = text.split("\n")
    formatted = []
    for line in lines:
        formatted.append(line.replace("*", "").strip())
    return "\n".join(formatted)



model = genai.GenerativeModel("gemini-1.5-flash")

# Function to generate recommendations
def generate_recommendation(age, height, weight, food, activity, goal):
    prompt = f"""
    Can I suggest a comprehensive plan that includes diet and workout for better fitness?
    for this user:
    age: {age},
    height: {height},
    weight: {weight},
    food preferences: {food},
    activity level: {activity},
    fitness goal: {goal}

    Based on the user's information:

    Diet Plan: RETURN LIST
    First show the Calorie, Protein, Fat, Carbohydrates that should be taken by the user (e.g.: Calories : 2000g)
    Suggest a brief Indian diet plan using the user's food preferences, activity, and fitness goal.

    Workout Plan: RETURN LIST
    Suggest a brief workout plan considering user's age, height, weight, activity level, and fitness goal, 
    including sets, reps, duration, and intensity.

    Suggestions: RETURN LIST
    Provide five suggestions to help the user achieve their fitness goal
    """
    response = model.generate_content(prompt).text
    
    return response

# Route for the homepage (index)
@app.route('/')
def index():
    return render_template('index.html')  # Show index.html on initial visit

# Route for login page
@app.route('/login')
def login():
    return render_template('login.html')  # Show login.html when /login is accessed

@app.route('/option')
def option():
    return render_template('option.html')  # Show option.html

# Route to handle login submission
@app.route('/submit-login', methods=['POST'])
def submit_login():
    username = request.form.get('username')
    password = request.form.get('password')

   
    if username == "testuser" and password == "testpass":
        return render_template('option.html')  
    else:
        return "Invalid credentials, please try again!"




# Route to handle recommendation generation
@app.route('/recommendation', methods=['POST'])
def recommendation():
    if request.method == 'POST':
       
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        food = request.form['food_preferences']
        activity = request.form['activity_level']
        goal = request.form['fitness_goals']

       
        recommendation_text = generate_recommendation(age, height, weight, food, activity, goal)
        formatted_output = format_fitness_plan(recommendation_text)

        recommendations = {
            "Diet_Recommendations" : [],
            "Workout_Recommendations" : [],
            "Suggestions" : []
        }
        
        current_section = None
        for line in formatted_output.splitlines():
            if "Diet Plan" in line:
                current_section = 'Diet_Recommendations'
            elif "Workout Plan" in line:
                current_section = 'Workout_Recommendations'
            elif "Suggestions" in line:
                current_section = 'Suggestions'
            elif line.strip() and current_section:
                recommendations[current_section].append(line.strip())
       
        return render_template('recommendation.html', recommendations = recommendations)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
