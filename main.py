from asyncio.events import get_event_loop
from neuralnet import NeuroNetLibrary, NluCall

event_loop = get_event_loop()

nlu_call = NluCall('77789509199', 'EP')
nn = NeuroNetLibrary(nlu_call, event_loop)


if __name__ == '__main__':
    pass
