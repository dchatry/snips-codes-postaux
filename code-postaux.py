#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import simplejson
import requests


def intent_received(hermes, intentMessage):
    """ Write the body of the function that will be executed once the intent is recognized. 
    In your scope, you have the following objects : 
    - intentMessage : an object that represents the recognized intent
    - hermes : an object with methods to communicate with the MQTT bus following the hermes protocol. 
    - conf : a dictionary that holds the skills parameters you defined 

    Refer to the documentation for further details. 
    """ 

    # if len(intentMessage.slots.ville) > 0:
    #     ville = int(intentMessage.slots.ville.first().value)
    #     response = requests.get("https://public.opendatasoft.com/api/records/1.0/search/?dataset=correspondance-code-insee-code-postal&q="+ville+"&facet=insee_com&facet=nom_dept&facet=nom_region&facet=statut")
    #     json_data = simplejson.loads(response.text)
    #     codepostal = json_data['records'][0]['fields']['postal_code']

        # result_sentence = "Le code postal de {} est {} .".format(ville, codepostal)
    #     result_sentence = ville
    # else:
        # result_sentence = "je ne te connais pas"
    if intent_message.intent.intent_name == 'codepostal':
        result_sentence = "test"
    else:
        return

    current_session_id = intentMessage.session_id
    hermes.publish_end_session(current_session_id, result_sentence)


with Hermes("localhost:1883") as h:
    h.subscribe_intents(intent_received).start()        