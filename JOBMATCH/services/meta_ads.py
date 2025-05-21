from django.conf import settings
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign

def crear_campania_facebook(campania):
    FacebookAdsApi.init(
        app_id=settings.FACEBOOK_APP_ID,
        app_secret=settings.FACEBOOK_APP_SECRET,
        access_token=settings.FACEBOOK_ACCESS_TOKEN,
    )

    params = {
        'name': campania.nombre,
        'objective': 'OUTCOME_TRAFFIC',
        'status': 'PAUSED' if campania.estado == 'pausada' else 'ACTIVE',
        'special_ad_categories': [],
    }

    try:
        facebook_campaign = Campaign(parent_id=settings.FACEBOOK_AD_ACCOUNT_ID)
        facebook_campaign.remote_create(params)
        return facebook_campaign['id']
    except Exception as e:
        raise Exception(f'Error Facebook API: {str(e)}')