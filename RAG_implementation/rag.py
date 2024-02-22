from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import requests
import dotenv
dotenv.load_dotenv()

# Load the document
url = "https://raw.githubusercontent.com/langchain-ai/langchain/master/docs/docs/modules/state_of_the_union.txt"
response = requests.get(url)
with open("state_of_the_union.txt", "w") as file:
    file.write(response.text)

loader = TextLoader('./state_of_the_union.txt')
documents = loader.load()

# chunk the document
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# embed and store chunks
