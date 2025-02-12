from datetime import datetime
import chromadb

# add this import statement 
from chromadb.utils.embedding_functions.onnx_mini_lm_l6_v2 import ONNXMiniLM_L6_V2

# create an embedded function variable 
ef = ONNXMiniLM_L6_V2(preferred_providers=["CPUExecutionProvider"])

# connect to chroma and list the current collections
chroma_client = chromadb.HttpClient(host="localhost", port=8000)
print(chroma_client.list_collections())

# create a new collection and list the current collections
collection = chroma_client.create_collection(name="Students", embedding_function=ef)
print(chroma_client.list_collections())

# student_info document to be added to the collection
student_info = """
Alexandra Thompson, a 19-year-old computer science sophomore with a 3.7 GPA,
is a member of the programming and chess clubs who enjoys pizza, swimming, and hiking
in her free time in hopes of working at a tech company after graduating from the University of Washington.
"""

# club_info document to be added to the collection
club_info = """
The university chess club provides an outlet for students to come together and enjoy playing
the classic strategy game of chess. Members of all skill levels are welcome, from beginners learning
the rules to experienced tournament players. The club typically meets a few times per week to play casual games,
participate in tournaments, analyze famous chess matches, and improve members' skills.
"""

# university_info document to be added to the collection
university_info = """
The University of Washington, founded in 1861 in Seattle, is a public research university
with over 45,000 students across three campuses in Seattle, Tacoma, and Bothell.
As the flagship institution of the six public universities in Washington state,
UW encompasses over 500 buildings and 20 million square feet of space,
including one of the largest library systems in the world.
"""

# add the documents in the newly created collection
collection.add(
    documents = [student_info, club_info, university_info],
    metadatas = [{"source": "student info"},{"source": "club info"},{'source':'university info'}],
    ids = ["id1", "id2", "id3"]
)
print("")
print("collection.peek")
print(collection.peek(limit=5))
print("")

# query the collection
results = collection.query(
    query_texts=["What is the student name?"],
    n_results=2
)


# print the results of the query
print("")
print("collection.query")
print(results)
print("")
