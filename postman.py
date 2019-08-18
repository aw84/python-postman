'''
Loads module passed by command line as first arg to that script
'''

import sys
import http.client
import importlib

sys.path.append('./requests')


def load_module_by_nanme(name):
    '''
    Creates module
    '''
    spec = importlib.util.find_spec(name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.modules[name] = module
    return module

def do_request(config):
    '''
    Executes HTTP request with config loaded from config
    '''
    conn = http.client.HTTPConnection(config.host)
    conn.request(config.method, config.url, headers=config.headers)
    resp = conn.getresponse()
    print((resp.status, resp.reason))
    for header in resp.getheaders():
        print("{name}: {value}".format(name=header[0], value=header[1]))
    data = resp.read()
    print(data.decode())
    conn.close()


if __name__ == '__main__':
    module = load_module_by_nanme(sys.argv[1])
    do_request(module)
