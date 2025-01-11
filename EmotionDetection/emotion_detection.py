'''A module that leverages Watson NLP Library for emotion detection'''
import requests
import json

def emotion_detector(text_to_analyze):
    ''' Calls Watson NLP Service to analyze a text 
            parameters: the text to be analyzed
            returns: 
            {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': '<name of the dominant emotion>'
            }
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header_dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } } 
    watson_response = json.loads(requests.post(url, json = payload, headers=header_dict).text)
    dominant = (0,"")
    watson_emotions = watson_response['emotionPredictions'][0]['emotion']
    for emotion, score in watson_emotions.items():
        if (score > dominant[0]):
            dominant = (score, emotion)
    #formatting the response to be clompliant with the instructions
    emotions = {
        'anger': watson_emotions['anger'],
        'disgust': watson_emotions['disgust'],
        'fear': watson_emotions['fear'],
        'joy': watson_emotions['joy'],
        'sadness': watson_emotions['sadness'],
        'dominant_emotion': dominant[1]
    }
    return emotions
        