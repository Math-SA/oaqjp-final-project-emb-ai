'''A module that leverages Watson NLP Library for emotion detection'''
import json
import requests


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
    api_host='https://sn-watson-emotion.labs.skills.network'
    url = api_host +'/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header_dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    emotions = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    #Don't bother sending empty strings to Watson API
    if text_to_analyze == '':
        return emotions
    payload = { "raw_document": { "text": text_to_analyze } }
    try:
        watson_response = requests.post(url, json = payload, headers=header_dict, timeout=5)
        #Return None for all values if satus code is 400
        if watson_response.status_code == 400:
            return emotions
    except requests.exceptions.Timeout:
        return emotions
    #process Watson response
    watson_response = json.loads(watson_response.text)
    dominant = (0,"")
    watson_emotions = watson_response['emotionPredictions'][0]['emotion']
    for emotion, score in watson_emotions.items():
        if score > dominant[0]:
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
        