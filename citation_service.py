from scholarly import scholarly

def get_citation(id_scholar: str, year: int):
    author = scholarly.search_author_id(id_scholar)
    author = scholarly.fill(author, sections=["indices", "counts"])

    citations_by_year = author.get("cites_per_year", {})
    citations = citations_by_year.get(int(year), 0)

    return {
        "id_scholar": id_scholar,
        "nama": author.get("name"),
        "tahun": year,
        "jumlah": citations,
    }
