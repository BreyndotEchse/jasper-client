# -*- coding: utf-8-*-
import datetime
import re
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = ["UHR"]


def handle(text, mic, profile):
    """
        Reports the current time based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    tz = getTimezone(profile)
    now = datetime.datetime.now(tz=tz)
    hours = now.strftime("%H").lstrip("0")
    if not len(hours):
        hours = "Null"
    response = "Es ist jetzt %s Uhr" % hours
    
    minutes = now.strftime("%M").lstrip("0")
    if len(minutes):
        response += " %s" % minutes
    mic.say(response)


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\buhr\b', text, re.IGNORECASE))
