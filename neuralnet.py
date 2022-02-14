from datetime import datetime
from typing import Dict, Any
from dateutil.parser import parse
import time

UUID = 'Script identificator'


class NluCall:
    msisdn: str = None
    status: str = None
    entry_point = None

    @property
    def result(self):
        return self.status

    def __init__(self, msisdn: str, entry_point):
        self.msisdn = msisdn
        self.entry_point = entry_point


class NeuroNetLibrary:
    RESULT_DONE = True

    event_loop = None
    dialog: NluCall = None
    __env: Dict = {}

    def env(self, name=None, val=None):
        # Declaration many variables with their values [ NAME MUST BE DICT ]
        if type(name) is dict:
            for key in name.keys():
                self.__env.update({key: name[key]})

        # Set variable value
        elif name and val:
            self.__env[name] = val

        # Get_or_create Env_variable
        elif name:
            try:
                return self.__env[name]
            except KeyError:
                self.__env.update({str(name): ''})

        # Get all Env_variables
        else:
            return self.__env

    def log(self, name: str, data: str):
        pass

    def storage(self, key, *args):
        if args:
            for args_key in args:
                try:
                    return self.__env[args_key]
                except KeyError:
                    pass
        return self.__env[key]

    def call(self,
             msisdn: str,
             date: (datetime, str) = None,
             channel: str = None,
             script: (str, UUID) = None,
             entry_point: str = None,
             transport: str = 'sip',
             on_success_call: Any[None, str] = None,
             on_failed_call=None,
             proto_additional: dict = None):

        if date:
            return parse(date)
        default_date = time.strftime('%Y-%m-%d %H:%M')
        return default_date

    def __init__(self, nlu_call: NluCall, event_loop=None):
        self.dialog = nlu_call
        self.event_loop = event_loop
