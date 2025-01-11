''' Flask server to provide an UI for the Emotion Detector app '''
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector app. Powered by IBM Watson NLP Service")

#Routes
@app.route("/emotionDetector")
def analyze():
    #get parameter textToAnalyze and analyze
    emotion = emotion_detector(request.args.get('textToAnalyze'))
    response = f"For the given statement, the system response is \
        'anger': {emotion['anger']},\
        'disgust': {emotion['disgust']},\
        'fear': {emotion['fear']}, \
        'joy': {emotion['joy']} and \
        'sadness': {emotion['sadness']}. \
        The dominant emotion is <b>{emotion['dominant_emotion']}</b>."
    return response

@app.route("/")
def index():
    return render_template('index.html')
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)