import os

# Bot Configuration
TOKEN = 'your-bot-token'  # Replace with your actual bot token
OWNER_ID = int(os.getenv('OWNER_ID', 'your-owner-id'))
ADMINS = [int(admin_id) for admin_id in os.getenv('ADMINS', 'admin-id1,admin-id2').split(',')]
LOG_CHANNEL = os.getenv('LOG_CHANNEL', 'your-log-channel-id')

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
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = 'ftm_ultra_bot'

# Premium Users
PREMIUM_USERS = {
    # user_id: expiry_date
    # Example: 123456789: '2024-12-31'
}

# Other settings
