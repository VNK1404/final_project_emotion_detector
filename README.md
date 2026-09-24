# Final Project: Emotion Detection with Watson NLP

**Project Name:** Final Project - Emotion Detection Application Using Watson NLP  
**Course Repository:** `oaqjp-final-project-emb-ai`

An AI-powered Flask web application that analyzes user-provided text using IBM Watson NLP's Emotion Prediction Service to detect emotions (anger, disgust, fear, joy, sadness) and identify the dominant emotion.

## Table of Contents
- [Project Name & Overview](#project-name--overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Unit Testing](#unit-testing)
- [Static Code Analysis](#static-code-analysis)
- [Error Handling](#error-handling)

## Project Name & Overview
**Project Name:** Final Project  
This application interfaces with IBM Watson NLP's Emotion Predict library to extract emotional sentiment from natural language text. The system extracts confidence scores for five primary emotions:
- Anger
- Disgust
- Fear
- Joy
- Sadness

It determines the dominant emotion with the highest score and provides both a Python package and a web-based user interface built with Flask, HTML5, and JavaScript.

## Project Structure
```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── test_emotion_detection.py
├── server.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone this repository to your local environment:
   ```bash
   git clone https://github.com/VNK1404/oaqjp-final-project-emb-ai.git
   cd oaqjp-final-project-emb-ai
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Running the Flask Server
To launch the application server:
```bash
python server.py
```
Open your web browser and navigate to `http://localhost:5000` or `http://127.0.0.1:5000` to interact with the web interface.

### Running via Python Package
You can import the `emotion_detector` function directly in your Python code:
```python
from EmotionDetection.emotion_detection import emotion_detector

response = emotion_detector("I am so happy today!")
print(response)
```

## Unit Testing
To execute the automated unit test suite:
```bash
python -m unittest test_emotion_detection.py
```

## Static Code Analysis
To verify code styling and quality against PEP8 standards:
```bash
pylint server.py EmotionDetection/emotion_detection.py EmotionDetection/__init__.py test_emotion_detection.py
```

## Error Handling
The application gracefully handles blank, invalid, or malformed inputs. When invalid input is submitted (HTTP 400), the detector returns `None` for all emotion scores and the web interface displays:
```text
Invalid text! Please try again!
```
