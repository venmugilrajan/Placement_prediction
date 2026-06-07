import pickle
import pandas as pd 
from flask import Flask, render_template,request
app=Flask(__name__)

with open("model.pkl","rb") as file:
    model=pickle.load(file)

@app.route('/')
def home():
    return render_template(
        'index.html',
        result="",
        placement_probability=0,
        recommendations=[],
        cgpa="",
        aptitude="",
        projects=""
    )
@app.route('/predict', methods=['POST'])
def predict():
    cgpa = float(request.form['cgpa'])
    aptitude = float(request.form['aptitude'])
    projects = float(request.form['projects'])

    input_data = pd.DataFrame(
        [[cgpa, aptitude, projects]],
        columns=["cgpa", "aptitude", "projects"]
    )

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    placement_probability = round(
        probability[0][1] * 100,
        2
    )

    recommendations = []

    if cgpa >= 9 and aptitude >= 85 and projects >= 5:
        recommendations.append(
            "Outstanding profile! Target top product-based companies."
        )

    if cgpa >= 8.5 and aptitude >= 75 and projects >= 4:
        recommendations.append(
            "Strong profile. Focus on mock interviews and resume building."
        )

    if cgpa >= 8 and projects >= 5:
        recommendations.append(
            "Excellent academic and project balance."
        )

    if cgpa >= 8 and aptitude < 60:
        recommendations.append(
            "Academic performance is good, but aptitude needs attention."
        )

    if cgpa < 7 and aptitude >= 80:
        recommendations.append(
            "Strong aptitude skills. Improving CGPA can significantly improve opportunities."
        )

    if cgpa < 7 and projects >= 5:
        recommendations.append(
            "Good project experience. Focus on academics to strengthen your profile."
        )

    if projects == 0:
        recommendations.append(
            "Start building projects to demonstrate practical skills."
        )

    if projects == 1:
        recommendations.append(
            "Try building at least 2-3 more projects."
        )

    if projects >= 7:
        recommendations.append(
            "Excellent project portfolio. Showcase your best projects on GitHub."
        )

    if aptitude >= 90:
        recommendations.append(
            "Exceptional aptitude performance. Practice coding interviews."
        )

    if aptitude < 50:
        recommendations.append(
            "Daily aptitude practice is strongly recommended."
        )

    if aptitude >= 70 and projects < 2:
        recommendations.append(
            "Good aptitude skills. Increase project count for a stronger profile."
        )

    if cgpa >= 9 and projects < 2:
        recommendations.append(
            "Strong academics. Add more projects to improve practical exposure."
        )

    if cgpa >= 8 and aptitude >= 75 and projects >= 3:
        recommendations.append(
            "You appear placement-ready. Start applying for internships and placements."
        )

    if cgpa >= 8 and aptitude >= 80 and projects >= 5:
        recommendations.append(
            "Consider learning system design and advanced DSA concepts."
        )

    if cgpa < 6.5 and aptitude < 50 and projects < 2:
        recommendations.append(
            "Focus on fundamentals before placement season begins."
        )

    if projects >= 3 and aptitude >= 75:
        recommendations.append(
            "Your practical and analytical skills are developing well."
        )

    if cgpa >= 8.5 and aptitude >= 85:
        recommendations.append(
            "Your profile is suitable for competitive hiring processes."
        )

    if cgpa >= 7.5 and aptitude >= 70 and projects >= 2:
        recommendations.append(
            "Maintain consistency and continue skill development."
        )

    if cgpa < 7.5 and aptitude < 70:
        recommendations.append(
            "Allocate time daily for both academics and aptitude preparation."
        )

    if cgpa >= 8 and projects >= 4 and aptitude >= 70:
        recommendations.append(
            "Start participating in hackathons and coding contests."
        )

    if projects >= 5:
        recommendations.append(
            "Create a portfolio website to showcase your work."
        )

    if projects >= 3:
        recommendations.append(
            "Keep all projects documented on GitHub."
        )

    if prediction[0] == 1:
        result = f"High Placement Chance! 👏)"
    else:
        result = f"Low Placement Chance! 😰)"

    return render_template(
        "index.html",
        result=result,
        placement_probability=placement_probability,
        recommendations=recommendations,
        cgpa=cgpa,
        aptitude=aptitude,
        projects=projects
        
    )
if __name__=="__main__":
    app.run(debug=True)