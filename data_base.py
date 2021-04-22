import sqlalchemy as db
from translate import supported_languages
from sqlalchemy_utils import database_exists


class DataBase:
    __engine = db.create_engine(r'sqlite:///C:\Users\mateu\PycharmProjects\Translator\languages.db')
    __connection = __engine.connect()
    __metadata = db.MetaData()
    __languages = db.Table('languages', __metadata,
                           db.Column('Name', db.String(50), nullable=False, unique=True),
                           db.Column('Abbreviation', db.String(5), nullable=False, unique=True)
                           )

    def __init__(self):
        if not database_exists(self.__engine.url):
            DataBase.__metadata.create_all(DataBase.__engine)
            languages = supported_languages()
            for k, v in languages.items():
                query = db.insert(self.__languages).values(Name=k, Abbreviation=v)
                self.__connection.execute(query)

    def get_languages(self):
        lang_tuple_list = self.__connection.execute(db.select([self.__languages])).fetchall()
        return {tup[0]: tup[1] for tup in lang_tuple_list}
