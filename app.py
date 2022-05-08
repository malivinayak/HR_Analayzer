from flask import Flask , render_template , request
import analyzer


app = Flask(__name__)


@app.route("/", methods = ["GET","POST"])
def main():
    #html -> .py
    userName=""
    promoted=""
    if request.method == "POST":
        userName = request.form["name"]
        department = request.form["department"]
        region = request.form["region"]
        gender = request.form["gender"]
        recruitment_channel = request.form["recruitment_channel"]
        no_of_trainings = request.form["no_of_trainings"]
        age = request.form["age"]
        previous_year_rating = request.form["previous_year_rating"]
        length_of_service = request.form["length_of_service"]
        KPIs_met = request.form["KPIs_met"]
        awards_won = request.form["awards_won"]
        avg_training_score = request.form["avg_training_score"]

        if(department == "Sales & Marketing"):
            department  = int(0) 
        elif(department =="Operations"):
            department  = int(1)
        elif(department =="Technology"):
            department  = int(3)
        elif(department =="Procurement"):
            department  = int(4)
        elif(department =="Analytics"):
            department  = int(5)
        elif(department =="Finance"):
            department  = int(6)
        elif(department =="HR"):
            department  = int(7)
        elif(department =="Legal"):
            department  = int(8)
        else:
            department = int(9)

        if(recruitment_channel=="referred"):
            recruitment_channel = int(1)
        elif(recruitment_channel=="sourcing"):
            recruitment_channel = int(0)
        else:
            recruitment_channel = int(3)

        if(gender =="Male"):
            gender=int(1)
        else:
            gender=int(0)

        if(KPIs_met =="More than 80%"):
            KPIs_met=int(1)
        else:
            KPIs_met=int(0)

        userInput = {
            'department': [department], 
            'region': [region],
            'gender': [gender], 
            'recruitment_channel': [recruitment_channel],
            'no_of_trainings': [no_of_trainings], 
            'age': [age], 
            'previous_year_rating': [previous_year_rating], 
            'length_of_service': [length_of_service], 
            'KPIs_met >80%': [KPIs_met],
            'awards_won?': [awards_won], 
            'avg_training_score': [avg_training_score] } 

        is_promoted = analyzer.HR_analyzer(userInput)
        if(is_promoted[0]==1):
            promoted = "🎉Congratulations! "+ userName +" You can be promoted as HR"
        else:
            promoted = userName + " you can not be HR"

    # .py -> html
    return render_template("index.html", n = promoted)


if __name__ == "__main__":
    app.run(debug=True)