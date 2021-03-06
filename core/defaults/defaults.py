from data.data import get_data_file
from core.json import default
settings_file = default
settings = {
    'tokens': {
        'discord': [],
        'twitch': {
            'owner': '',
            'pw': []
        }
    },
    'api': {
        'host': '127.0.0.1',
        'port': 5000,
    },
    'secure': {
        'extractors': {
            'youtube': None,
            'twitch': None
        }
    },
    'activity': {
        'default': {
            'name': 'games',
            'type': 0
        }
    },
    'settings': {
        'logging': {
            'console': {
                'level': 'default'
            },
            'file': {
                'level': 'default',
                'override': False,
                'file': 'log.txt'
            }
        },
        'database': {
            'path': None,
            'file': 'data.sqlite'
        }
    }
}
