class Config:
    SECRET_KEY = 'dev_secret_key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:veera8432@localhost/student_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False