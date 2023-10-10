import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_PRIVATE_KEY
#stripe.api_key = settings.STRIPE_PUBLIC_KEY