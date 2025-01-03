from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "sqlite:///tables/berlincharginghub.db"
#DATABASE_URL = "sqlite:///tables/berlincharginghub.db"
import os
project_dir = os.path.abspath(os.path.join(os.getcwd(), 'tables'))
DATABASE_URL = f"sqlite:///{project_dir}/berlincharginghub.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
