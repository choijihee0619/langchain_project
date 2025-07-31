import meilisearch

client = meilisearch.Client('http://localhost:7700', 'aSampleMasterKey')

def stock_search(query):
    return client.index('nasdaq').search(query)
