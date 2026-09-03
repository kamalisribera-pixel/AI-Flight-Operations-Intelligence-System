from src.database.database import Database


class DatabaseBuilder:

    @staticmethod
    def build(database=None):
        return database or Database()


if __name__ == "__main__":
    DatabaseBuilder.build()
