import os

# Bot Configuration
TOKEN = '7913243499:AAGiHTvlWK8x2SCIRN6LAZZqHPNyE0ULBjU'  # Replace with your actual bot token
OWNER_ID = int(os.getenv('OWNER_ID', '7042535787'))
ADMINS = [int(admin_id) for admin_id in os.getenv('ADMINS', '6521935712').split(',')]
LOG_CHANNEL = os.getenv('LOG_CHANNEL', '-1002216221045')

# Subscription Plans
SUBSCRIPTION_PLANS = {
    'platinum': {
        'limit': 10 * 1024 * 1024  # 10GB
    },
    'basic': {
        'limit': 2 * 1024 * 1024  # 2GB
    }
}

# MongoDB Configuration
MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://funtoonsmultimedia: funtoonsmultimedia@ftmgram.l3uji.mongodb.net/?retryWrites=true&w=majority&appName=ftmgram')
DB_NAME = 'ftmgram'

# Premium Users
PREMIUM_USERS = {
    # user_id: expiry_date
    # Example: 123456789: '2024-12-31'
}

# Other settings
