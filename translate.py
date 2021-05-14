from google.cloud import translate_v2
from google.oauth2 import service_account
from google.api_core.exceptions import BadRequest


def _prepare_api():
    credentials = service_account.Credentials.from_service_account_file('./translator_key.json')
    translation = translate_v2.Client(credentials=credentials)
    return translation


def translate_google_cloud_api(src, dest, text):
    translation = _prepare_api()
    try:
        return translation.translate(text, source_language=src, target_language=dest)
    except BadRequest:
        raise BadRequest


def supported_languages():
    translation = _prepare_api()
    # get_languages returns list of dict {'language': 'ww', 'name': 'Name'}
    languages = {name: short for elem in translation.get_languages() for short, name in [elem.values()]}
    return languages
