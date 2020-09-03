# This file is a template
default = 'settings.json'
settings = {
    'discord': {
        'prefix': '.',
        'tokens': [],
        'default': {
            'activity': {
                'name': 'games',
                'type': 0
            }
        }
    },
    'twitch': {
        'prefix': '!',
        'tokens': []
    },
    'api': {
        'host': '127.0.0.1',
        'port': 5000,
    },
    'external': {
        'youtube': None,
        'twitch': None
    },
    'settings': {
        'logging': {
            'console': {
                'level': 'default'
            },
            'file': {
                'level': 'default',
                'name': 'log.txt',
                'mode': 'a+'  # Too much freedom
            }
        },
        'database': {
            'engine': 'sqlite',
            'address': '/'
        }
    },
    'permissions': {},
    'revision': '2020.09.03'  # Remember to always update this when changes are made to this file
}
