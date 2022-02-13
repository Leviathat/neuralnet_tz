from typing import List, Dict


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

    def storage(self, key, *args):
        if args:
            for args_key in args:
                try:
                    return self.__env[args_key]
                except KeyError:
                    pass
        return self.__env[key]

    def log(self, name: str, data: str):
        pass

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

    def __init__(self, nlu_call: NluCall, event_loop=None):
        self.dialog = nlu_call
        self.event_loop = event_loop
