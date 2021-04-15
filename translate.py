import google_trans_new


LANGKEYS = dict((v, k) for k, v in google_trans_new.LANGUAGES.items())


def translate(text, source, destination):
    global LANGKEYS
    translator = google_trans_new.google_translator()
    translation = translator.translate(text, lang_src=LANGKEYS[source], lang_tgt=LANGKEYS[destination])
    return translation
