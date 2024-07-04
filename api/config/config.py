import os
from dotenv import load_dotenv

environment = os.getenv('ENV', 'development')

if environment == 'production':
    load_dotenv('.env.production')
else:
    load_dotenv('.env.development')

DATABASE_URL = os.getenv('DATABASE_URL')