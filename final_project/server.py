"""Flask web server for Emotion Detection."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    """Render the index page."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_api():
    """Handle emotion detection requests."""
    text = (request.args.get("textToAnalyze") or "").strip()
    if not text:
        return "Invalid text! Please try again!", 200

    result = emotion_detector(text)
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 200

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
    