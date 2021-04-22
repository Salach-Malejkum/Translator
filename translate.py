from google.cloud import translate_v2
from google.oauth2 import service_account
from google.api_core.exceptions import BadRequest as BadRequest


def translate_google_cloud_api(src, dst, text):
    credentials = service_account.Credentials.from_service_account_file(
        'C:\\Users\\mateu\\PycharmProjects\\Translator\\translator_key.json')
    translation = translate_v2.Client(credentials=credentials)
    try:
        print(translation.translate(text, source_language=src, target_language=dst))
    except BadRequest as e:
        print(e)

