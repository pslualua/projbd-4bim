import os
from pathlib import Path
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(Path(__file__).with_name(".env"))

uri = os.getenv("MONGO_URI")

cliente = MongoClient(uri, serverSelectionTimeoutMS=5000)

cliente.admin.command("ping")

banco = cliente["laboratorio_python"]

print("Conexão estabelecida com sucesso!")