def extract_full_text(item_url):
    import requests
    from readability import Document

    response = requests.get(item_url)
    if response.status_code == 200:
        doc = Document(response.text)
        return doc.summary()
    else:
        return None