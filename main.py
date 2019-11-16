from PyQt5 import QtSql


class cofee:
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.load_genres()

    def initUI(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("image.db")
        db.open()
        model = QtSql.QSqlQueryModel(parent=None)
        model.setQuery("select * from images")
        model.query().exec_()
        self.BD.setModel(model)
        self.BD.show()
