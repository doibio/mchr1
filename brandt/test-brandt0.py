from llama_index import VectorStoreIndex, SimpleDirectoryReader
import logging
import sys

import os.path
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
prompt = "Please restate the following in terms of a question : "

def process_section(section):
    response = query_engine.query(prompt + section)
    print(response, flush=True)
    print("-----")

def read_and_process_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

        sections = content.split('\n\n')

        for section in sections:
            process_section(section)

read_and_process_file('brandt-ai0.txt')
