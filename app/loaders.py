from langchain_community.document_loaders import WebBaseLoader

def load_page(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    result = docs[0].metadata
    result["page_content"] = docs[0].page_content
    return result