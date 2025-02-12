from datetime import datetime
import chromadb

# add this import statement 
from chromadb.utils.embedding_functions.onnx_mini_lm_l6_v2 import ONNXMiniLM_L6_V2

# create an embedded function variable 
ef = ONNXMiniLM_L6_V2(preferred_providers=["CPUExecutionProvider"])

# connect to chroma and list the current list of collections
chroma_client = chromadb.HttpClient(host="localhost", port=8000)
print("List of collections")
print(chroma_client.list_collections())
print("")

# get the Students collection
collection = chroma_client.get_collection("Students")

# query the Students collection
results = collection.query(
    query_texts=["What is the student name?"],
    n_results=2
)

# display results of querying the Students collection
print("Display the results of querying the Students collection")
print(results)
print("")
