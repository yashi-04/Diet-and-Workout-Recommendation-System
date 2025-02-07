# FitSense : Optimized Fitness and Nutrition Guidance
FitSense provides a smart and personalized workout and diet recommendation system tailored to your unique profile, goals, and preferences. Say goodbye to generic advice and unstructured plans.


## Why Choose FitSense?
 With FitSense, achieve faster results with tailored workout regimens, smarter diet choices, and an enjoyable fitness journey. Simplify your path to health and fitness with actionable insights designed just for you.

---

### FitSense is a Diet and Workout Recommendation App

This is a web application that provides personalized diet and workout recommendations based on user inputs such as age, height, weight, food preferences, activity level, and fitness goals. The app uses **Google's Gemini API** to generate fitness plans and is built using **Flask**, a Python web framework.

---

## Features
- **Personalized Recommendations**:
  - Generates a diet plan tailored to the user's food preferences and fitness goals.
  - Provides a workout plan based on the user's physical attributes and activity level.
  - Offers additional suggestions to help users achieve their fitness goals.
- **User-Friendly Interface**:
  - Simple and intuitive forms for user input.
  - Displays recommendations in a clean and organized format.
- **Secure Login**:
  - Basic login functionality to access the recommendation feature.

---

## Technologies Used
- **Backend**:
  - Python
  - Flask (Web Framework)
- **AI Integration**:
  - Google Gemini API (for generating recommendations)
- **Frontend**:
  - HTML, CSS (for templates)
- **Environment**:
  - Environment variables for API key management.

---

## Prerequisites
To run this project, you need the following:
1. **Python 3.x**: Install Python from [python.org](https://www.python.org/).
2. **Google Gemini API Key**: Obtain an API key from [Google Cloud Console](https://console.cloud.google.com/).
3. **Flask**: Install Flask using pip.
4. **Google Generative AI Library**: Install the library for interacting with the Gemini API.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/diet-workout-recommendation-app.git
cd diet-workout-recommendation-app
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```plaintext
GOOGLE_API_KEY=your-api-key-here
```

---

## Usage

### 1. Run the Application
Start the Flask development server:
```bash
python app.py
```

### 2. Access the Application
Open your browser and go to:
```
http://127.0.0.1:5000/
```

### 3. Login
- Use the following credentials to log in:
  - **Username**: `testuser`
  - **Password**: `testpass`

### 4. Enter Your Details
- Fill out the form with your:
  - Age
  - Height
  - Weight
  - Food Preferences
  - Activity Level
  - Fitness Goals

### 5. View Recommendations
- The app will display:
  - A **Diet Plan** with calorie, protein, fat, and carbohydrate recommendations.
  - A **Workout Plan** with sets, reps, duration, and intensity.
  - **Suggestions** to help you achieve your fitness goals.

---

## Project Structure
```
diet-workout-recommendation-app/
│
├── app.py                  # Main Flask application
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables (API key)
├── templates/              # HTML templates
│   ├── index.html          # Homepage
│   ├── login.html          # Login page
│   ├── option.html         # Option selection page
│   └── recommendation.html # Recommendation display page
└── README.md               # Project documentation
```

---

## Customization
- **Update Login Credentials**:
  - Modify the `submit-login` route in `app.py` to use your own username and password.
- **Change API Key**:
  - Update the `GOOGLE_API_KEY` in the `.env` file.
- **Modify Prompts**:
  - Adjust the `generate_recommendation` function in `app.py` to customize the prompts sent to the Gemini API.

---

## Example Output

### Input:
```plaintext
Age: 25
Height: 170 cm
Weight: 70 kg
Food Preferences: Vegetarian
Activity Level: Moderate
Fitness Goals: Lose weight
```

### Output:
```plaintext
Diet Plan:
- Calories: 1800 kcal
- Protein: 120g
- Fat: 50g
- Carbohydrates: 200g
- Breakfast: Oats with fruits and nuts
- Lunch: Brown rice with dal and vegetables
- Dinner: Quinoa salad with tofu

Workout Plan:
- Cardio: 30 minutes of running (3 sets)
- Strength Training: Squats (3 sets of 12 reps)
- Yoga: 20 minutes of stretching

Suggestions:
1. Stay hydrated throughout the day.
2. Avoid processed foods.
3. Get at least 7 hours of sleep.
4. Track your progress weekly.
5. Stay consistent with your diet and workout.
```

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Author
Yashi Sharma
https://github.com/yashi-04
shyashi04@gmail.com

---

