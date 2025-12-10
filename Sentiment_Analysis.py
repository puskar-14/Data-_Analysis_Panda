# PROJECT: Sentiment Analysis Web Application (Flask + TextBlob) 
 
# FEATURES:
#  User enters text in a web form 
#  TextBlob performs sentiment analysis # ✔ Displays: 
# Sentiment (Positive / Negative / Neutral) 
#  Polarity score # - Subjectivity score 
#  Clean and simple 


from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)

 
# HTML TEMPLATE (simple + embedded)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analysis App</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: #f2f2f2; 
            padding: 40px;
        }
        .container {
            width: 50%%; 
            margin: auto; 
            background: white; 
            padding: 25px; 
            border-radius: 10px;
            box-shadow: 0px 0px 10px #ccc;
        }
        textarea {
            width: 100%%; 
            height: 120px; 
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 22px; 
            font-size: 16px; 
            background: #007bff; 
            color: white; 
            border: none;
            border-radius: 5px; 
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .result-box {
            margin-top: 20px; 
            padding: 15px; 
            background: #e8f5e9;
            border-left: 5px solid #43a047;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Sentiment Analysis Tool</h2>
        <form method="POST">
            <label>Enter text for sentiment analysis:</label><br><br>
            <textarea name="user_text">{{ user_text }}</textarea><br><br>
            <button type="submit">Analyze</button>
        </form>

        {% if sentiment %}
        <div class="result-box">
            <h3>Results:</h3>
            <p><strong>Sentiment:</strong> {{ sentiment }}</p>
            <p><strong>Polarity:</strong> {{ polarity }}</p>
            <p><strong>Subjectivity:</strong> {{ subjectivity }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


# Sentiment Classification Logic

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity       # -1 to 1
    subjectivity = blob.sentiment.subjectivity  # 0 to 1

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, round(polarity, 3), round(subjectivity, 3)


# Flask Route

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = polarity = subjectivity = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("user_text", "")
        sentiment, polarity, subjectivity = analyze_sentiment(user_text)

    return render_template_string(
        HTML_TEMPLATE,
        sentiment=sentiment,
        polarity=polarity,
        subjectivity=subjectivity,
        user_text=user_text
    )


# Run the App


if __name__ == "__main__":
    app.run(debug=True)
