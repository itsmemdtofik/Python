
#! Pickling and Unpickling in Python


#** Convert python object into the byte stream called pickling (Serialization).
#** Restore them back into the python object is called unpickling (Deserialization).

import pickle

# Pickling (Serialize to bytes)
data = {"name": "Alice", "age": 30}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)  # Saves to file

# Unpickling (Deserialize back to Python object)
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)  # Restores original object

print(loaded_data)  # Output: {'name': 'Alice', 'age': 30}