'''A module that leverages Watson NLP Library for emotion detection'''
import requests

def emotion_detector(text_to_analyze):
    ''' Calls Watson NLP Service to analyze a text 
            parameters: the text to be analyzed
            returns: the json returned by the API. 
                see https://developer.ibm.com/apis/catalog/embeddableai--watson-natural-language-processing-apis/api/API--embeddableai--watson-natural-language-processing-apis#EmotionPredict
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header_dict = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } } 
    response = requests.post(url, json = payload, headers=header_dict)
    return response.text
    