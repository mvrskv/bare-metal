'''
Created on 27.07.2012

@author: mrasskazov
'''


class nova(object):
    '''
    nova-api config
    '''
    
    url = 'http://localhost:9882'
    

class ipmi(object):
    '''
    ipmi configuration
    '''

    bmnodes = 
    [
        {
        'name':            'bm4'
        'ipmi_host':       'mc0n4-kha-ipmi.kha.mirantis.net',
        'ipmi_username':   'engineer',
        'ipmi_password':   'zu3aeZ1a',
        'eth0_mac' :       '00:25:90:68:7D:B8',
        },
        {
        'name':            'bm5'
        'ipmi_host':       'mc0n5-kha-ipmi.kha.mirantis.net',
        'ipmi_username':   'engineer',
        'ipmi_password':   'zu3aeZ1a',
        'eth0_mac' :       '00:25:90:68:79:88',
        }
     ]
    

class tests(object):
    '''
    tests config. describe expected reults
    '''
    pass
