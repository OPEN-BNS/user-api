import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import dotenv_values

env = {
    **os.environ
}

URL_DATABASE = 'mysql+pymysql://root:'+env["MYSQL_PASSWORD"]+'@mysql_container:3306/user_dir_app'
engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()