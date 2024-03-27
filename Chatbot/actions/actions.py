# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List # New

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "Adelaide": "UTC+10:30",
    "Almaty": "UTC+6:00",
    "Amman": "UTC+3:00",
    "Anchorage": "UTC-9:00",
    "Antananarivo": "UTC+3:00",
    "Ashgabat": "UTC+5:00",
    "Athens": "UTC+3:00",
    "Auckland": "UTC+12:00",
    "Baghdad": "UTC+3:00",
    "Bangkok": "UTC+7:00",
    "Barcelona": "UTC+1:00",
    "Beijing": "UTC+8:00",
    "Bogota": "UTC-5:00",
    "Brasilia": "UTC-3:00",
    "Budapest": "UTC+2:00",
    "Cairo": "UTC+2:00",
    "Calgary": "UTC-7:00",
    "Cape Town": "UTC+2:00",
    "Chicago": "UTC-6:00",
    "Dar es Salaam": "UTC+3:00",
    "Dubai": "UTC+4:00",
    "Dublin": "UTC+1:00",
    "Edmonton": "UTC-7:00",
    "Geneva": "UTC+1:00",
    "Guatemala City": "UTC-6:00",
    "Helsinki": "UTC+3:00",
    "Hong Kong": "UTC+8:00",
    "Islamabad": "UTC+5:00",
    "Jakarta": "UTC+7:00",
    "Jerusalem": "UTC+3:00",
    "Kabul": "UTC+4:30",
    "Kathmandu": "UTC+5:45",
    "Khartoum": "UTC+2:00",
    "Kiev": "UTC+3:00",
    "Kingston": "UTC-5:00",
    "Lagos": "UTC+1:00",
    "Lima": "UTC-5:00",
    "Ljubljana": "UTC+1:00",
    "Luxembourg": "UTC+1:00",
    "Manila": "UTC+8:00",
    "Mexico City": "UTC-6:00",
    "Montreal": "UTC-5:00",
    "Moscow": "UTC+3:00",
    "Nairobi": "UTC+3:00",
    "Nassau": "UTC-5:00",
    "Oslo": "UTC+1:00",
    "Ottawa": "UTC-5:00",
    "Panama City": "UTC-5:00",
    "Paris": "UTC+1:00",
    "Perth": "UTC+8:00",
    "Prague": "UTC+1:00",
    "Pyongyang": "UTC+9:00",
    "Quito": "UTC-5:00",
    "Riyadh": "UTC+3:00",
    "Rome": "UTC+1:00",
    "Saint Petersburg": "UTC+3:00",
    "San Juan": "UTC-4:00",
    "Santiago": "UTC-3:00",
    "Sarajevo": "UTC+1:00",
    "Seoul": "UTC+9:00",
    "Shanghai": "UTC+8:00",
    "Singapore": "UTC+8:00",
    "Sofia": "UTC+2:00",
    "Stockholm": "UTC+1:00",
    "Sydney": "UTC+11:00",
    "Taipei": "UTC+8:00",
    "Tashkent": "UTC+5:00",
    "Tehran": "UTC+3:30",
    "Tokyo": "UTC+9:00",
    "Toronto": "UTC-5:00",
    "Tunis": "UTC+1:00",
    "Vancouver": "UTC-8:00",
    "Vienna": "UTC+1:00",
    "Vilnius": "UTC+2:00",
    "Warsaw": "UTC+1:00",
    "Wellington": "UTC+12:00",
    "Winnipeg": "UTC-6:00",
    "Zurich": "UTC+1:00",
    "London": "UTC+1:00",
    "Mumbai": "UTC+5:30",
    "Lisbon": "UTC+1:00"
}

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        city = tracker.get_slot("city")
        timezone = timezones.get(city)

        if timezone is None:
            output = "Could not find the time zone of {0}".format(city)
        else:
            output = "Time zone of {0} is {1}".format(city, timezone)
            
        dispatcher.utter_message(text=output)

        return []
