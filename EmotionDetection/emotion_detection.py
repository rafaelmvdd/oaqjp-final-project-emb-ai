import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        dominant_emotion = 'anger'
        anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
        max_emotion = anger
        disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        if disgust > max_emotion:
            max_emotion = disgust
            dominant_emotion = 'disgust'
        fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
        if fear > max_emotion:
            max_emotion = fear
            dominant_emotion = 'fear'
        joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
        if joy > max_emotion:
            max_emotion = joy
            dominant_emotion = 'joy'
        sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        if sadness > max_emotion:
            max_emotion = sadness
            dominant_emotion = 'sadness'
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    
        
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}