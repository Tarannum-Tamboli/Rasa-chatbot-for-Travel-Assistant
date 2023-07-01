# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBestHotels(Action):

    def name(self) -> Text:
        return "action_best_hotels"

    def run(self, dispatcher:CollectingDispatcher,
            tracker:Tracker,
            domain:Dict[Text, Any]) ->List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        message = 'No hotels mentioned for search'
        for e in entities: 
           if e['entity'] =='city':
               city = e['value']
               if city =='pune':
                     message = 'Hotel JWmarriot, Hotel Novotel, Hotel Hayat'
               elif city=='mumbai':
                    message = 'Hotel Taj, Hotel Shalimar, Hotel Oberoi'
               elif city=='nagpur':
                    message = 'Hotel Dwarka, Hotel Sai, Hotel Kimling'    
               else:
                    message = "Sorry We do not have any Hotel for the city"
        dispatcher.utter_message(text=message)

        return []
