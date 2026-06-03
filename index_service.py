from scholarly import scholarly

def get_index(id_scholar: str):

    author = scholarly.search_author_id(id_scholar)
    author = scholarly.fill(author, sections=["indices"])

    return {
        "id_scholar": id_scholar,
        "nama": author.get("name"),
        "h_index": author.get("hindex", 0),
        "h_index_5y": author.get("hindex5y", 0),
        "i10_index": author.get("i10index", 0),
        "i10_index_5y": author.get("i10index5y", 0),
    }
