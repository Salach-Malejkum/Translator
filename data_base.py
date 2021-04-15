import sqlalchemy as db


class LanguagesDb:
    __engine = db.create_engine(r'sqlite:///C:\Users\mateu\PycharmProjects\Translator\languages.db')
    __connection = __engine.connect()
    __metadata = db.MetaData()
    __languages = db.Table('languages', __metadata,
                           db.Column('Id', db.Integer(), primary_key=True),
                           db.Column('Name', db.String(50), nullable=False, unique=True)
                           )

    def __init__(self):
        LanguagesDb.__metadata.create_all(LanguagesDb.__engine, checkfirst=True)

    def get_languages(self):
        return self.__connection.execute(db.select([self.__languages])).fetchall()

    def add_language(self, language):
        query = db.insert(self.__languages).values(Name=language)
        self.__connection.execute(query)
