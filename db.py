
import configparser 
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


file_config = pathlib.Path(__file__).parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

username =  config.get("DB", "USER")
password =  config.get("DB", "PASSWORD")
database_name =  config.get("DB", "DATABASE")
domain =  config.get("DB", "DOMAIN")
port =  config.get("DB", "PORT")
url  = f"postgresql://{username}:{password}@{domain}:{port}/{database_name}"
engine = create_engine(url, echo = True)

DBSession = sessionmaker(bind = engine)
session = DBSession()






