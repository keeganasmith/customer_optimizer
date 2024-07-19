from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

from sqlalchemy import Column, Integer, String, Table, MetaData, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DB_Question(Base):
    __tablename__ = 'Questions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    question_type = Column(String)
    options = Column(JSON)
    option_biases = Column(JSON)
    
#Base.metadata.create_all(engine)

import pickle

def load_data(from_file):
    with open(from_file, 'rb') as f:
        data = pickle.load(f)
    return data

# Load the data from the pickle file
data = load_data('../questions/questions.pickle')

# Assuming `data` is a list of dictionaries
# for entry in data:
#     new_product = DB_Question(title=entry['title'], question_type=entry['question_type'], options=entry['options'], option_biases=entry["option_biases"])
#     session.add(new_product)

# session.commit()
# Query the database
products = session.query(DB_Question).all()

for product in products:
    print(f"Title: {product.title}, Description: {product.description}, Question Type: {product.question_type}, Options: {product.options}, option_biases: {product.option_biases}")
    # `product.tags` will be a list