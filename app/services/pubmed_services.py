import requests
import xml.etree.ElementTree as ET


BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def get_research_from_pubmed(drug_name: str, limit: int = 5):


    search_url = f"{BASE_URL}/esearch.fcgi"

    search_params = {
        "db": "pubmed",
        "term": drug_name,
        "retmax": limit,
        "retmode": "json"
    }

    search_response = requests.get(
        search_url,
        params=search_params
    )

    if search_response.status_code != 200:
        return None

    search_data = search_response.json()

    search_result = search_data.get(
        "esearchresult",
        {}
    )

    pmids = search_result.get(
        "idlist",
        []
    )

    total_results = search_result.get(
        "count",
        "0"
    )

    if not pmids:
        return {
            "total_results": total_results,
            "papers": []
        }

    # --------------------------------
    # Step 2: Fetch article details
    # --------------------------------

    fetch_url = f"{BASE_URL}/efetch.fcgi"

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml"
    }

    fetch_response = requests.get(
        fetch_url,
        params=fetch_params
    )

    if fetch_response.status_code != 200:
        return None

    root = ET.fromstring(
        fetch_response.text
    )

    papers = []

    
    for article in root.findall(
        ".//PubmedArticle"
    ):

        pmid_element = article.find(
            ".//PMID"
        )

        title_element = article.find(
            ".//ArticleTitle"
        )

        abstract_elements = article.findall(
            ".//Abstract/AbstractText"
        )

        journal_element = article.find(
            ".//Journal/Title"
        )

        year_element = article.find(
            ".//PubDate/Year"
        )

        # Authors
        authors = []

        for author in article.findall(
            ".//AuthorList/Author"
        ):

            last_name = author.findtext(
                "LastName",
                ""
            )

            first_name = author.findtext(
                "ForeName",
                ""
            )

            if last_name or first_name:

                full_name = (
                    f"{first_name} {last_name}"
                ).strip()

                authors.append(full_name)

        # Abstract
        abstract = " ".join(
            element.text
            for element in abstract_elements
            if element.text
        )

        # DOI
        doi = None

        for article_id in article.findall(
            ".//ArticleId"
        ):

            if article_id.get(
                "IdType"
            ) == "doi":

                doi = article_id.text
                break

        papers.append({

            "pmid": (
                pmid_element.text
                if pmid_element is not None
                else None
            ),

            "title": (
                title_element.text
                if title_element is not None
                else None
            ),

            "authors": authors,

            "journal": (
                journal_element.text
                if journal_element is not None
                else None
            ),

            "publication_year": (
                year_element.text
                if year_element is not None
                else None
            ),

            "abstract": abstract,

            "doi": doi
        })

    return {

        "total_results": total_results,

        "papers": papers

    }