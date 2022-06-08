"""Module environ."""
from os import environ


SESSION_CONFIGS = [
    dict(
        name='survey',
        display_name="Survey Simple ",
        app_sequence=['survey'],
        num_demo_participants=1
    ),
     dict(
        name='public_goods_simple',
        display_name="MyPublicGood ",
        app_sequence=['public_goods_simple'],
        num_demo_participants=3
    ),
    dict(
        name='trust',
        display_name="My trust",
        app_sequence=['trust'],
        num_demo_participants=2,
    ),

    
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
        name='econ102',
        display_name='Econ 102 class',
        participant_label_file='_rooms/econ102.txt',
        use_secure_urls=True
    ),
    dict(
        name='econ103',
        display_name='Econ 103 class',
        participant_label_file='_rooms/econ103.txt',
        use_secure_urls=True
    )
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '9724087574725'

INSTALLED_APPS = ['otree']
