import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {"text": text_to_analyze}
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        # Convert response text into a dictionary
        response_dict = json.loads(response.text)

        # Extract emotion scores
        emotions = response_dict["emotionPredictions"][0]["emotion"]

        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]

        # Find dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        # Return formatted output
        result = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }
        return result

    else:
        return {"error": f"Request failed with status code {response.status_code}"}