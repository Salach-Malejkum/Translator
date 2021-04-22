from google.cloud import translate_v2
from google.oauth2 import service_account
from google.api_core.exceptions import BadRequest as BadRequest


def prepare_api():
    credentials = service_account.Credentials.from_service_account_file(
        'C:\\Users\\mateu\\PycharmProjects\\Translator\\translator_key.json')
    translation = translate_v2.Client(credentials=credentials)
    return translation


def translate_google_cloud_api(src, dest, text):
    translation = prepare_api()
    try:
        return translation.translate(text, source_language=src, target_language=dest)
    except BadRequest:
        # Add exception handling
        pass


def supported_languages():
    translation = prepare_api()
    languages = {name: short for elem in translation.get_languages() for short, name in [elem.values()]}
    return languages
