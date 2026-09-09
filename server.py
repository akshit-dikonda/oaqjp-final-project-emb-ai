"""Flask server for the Emotion Detection application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions in the submitted text."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!."

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# Static code analysis
# Run: pylint server.py
