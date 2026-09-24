"""
This module detects emotions in a given piece of text using
IBM Watson NLP's emotion prediction service.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Sends text to the Watson NLP emotion prediction service and
    returns a dictionary with scores for anger, disgust, fear, joy,
    sadness, and the dominant emotion.

    If the input text is blank or invalid (status code 400), all
    values are returned as None.
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {
        "grpc-metadata-mm-model-id": (
            "emotion_aggregated-workflow_lang_en_stock"
        )
    }

    response = requests.post(url, json=myobj, headers=header, timeout=10)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    emotions_dict = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
