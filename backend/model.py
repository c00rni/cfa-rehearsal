from pymongo import MongoClient, InsertOne
from dotenv import dotenv_values
import logging
from backend.data import data

config = dotenv_values(".env")

class Model:

   def __init__(self, password, user):
      CHAÎNE_DE_CONNEXION = "mongodb+srv://{user}:{password}@swisssaver.7dnttgm.mongodb.net/?retryWrites=true&w=majority&appName=swisssaver".format(password=password, user=user)
      logging.info("Starting connexion to database...")
      client = MongoClient(CHAÎNE_DE_CONNEXION)
      logging.debug("Successfully connected to database")
      self.db = client.cfa

   def insertQuestion(self,
                      statement: str,
                      responses: list[str],
                      awnser_index: int,
                      difficulty_level: int,
                      cfa_level: int,
                      topic_index: int):
      if len(responses) != 3:
         raise Exception("A question must contain 3 responses.")
      if statement == "":
         raise Exception("The questions statement cannot be empty.")
      if awnser_index < 0 or awnser_index > 2:
         raise Exception("Awnser index out of range ( must be between 0 and 2)")
      if difficulty_level < 0 or difficulty_level > 5:
         raise Exception("Proficiency index out of range ( must be between 0 and 5)")
      
      question = {
         "statement":statement,
         "candidates": responses,
         "awnser": awnser_index,
         "difficulty_level": difficulty_level,
         "cfa_level": cfa_level,
         "topic": topic_index
      }
      
      try:
         record = self.db.questions.insert_one(question).inserted_id
         logging.debug("Question created : {record}".format(record=record))
      except:
         logging.error("The question couldn't be created.")

   def upadeQuestion(self,
                     id: str,
                     statement: str,
                     responses: list[str],
                     awnser_index: int,
                     difficulty_level: int,
                     cfa_level: int,
                     topic_index: int):
      
      question = {
         "statement":statement,
         "candidates": responses,
         "awnser": awnser_index,
         "difficulty_level": difficulty_level,
         "cfa_level": cfa_level,
         "topic": topic_index
      }

      try:
         record = self.db.questions.update_one({'_id': ObjectId(id)}, {"$set": question}).inserted_id
         logging.debug("Question created : {record}".format(record=record))
      except:
         logging.error("The question couldn't be created.")

"""
#Insert many
model = Model(config["MONGODB_PWD"], "corni")
operations = [InsertOne(item) for item in data["items"]]
results = model.db.questions.bulk_write(operations)
print(results)

# InsertOne
responses = ["Hello", "Aurevoir", "Salut"]
model.insertQuestion("What is CFA ?", responses, 0, 0, 1, 0)

#Get data
model = Model(config["MONGODB_PWD"], "corni")
print(list(model.db.questions.find({})))
"""
