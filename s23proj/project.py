"""This module contains the Works class, with functionality for Bibtex and RIS citation formats"""

import requests


class Works:
    """The Works class, which gets citation data from OpenAlex, and outputs citations in
    plain text, RIS or Bibtex"""

    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def __str__(self):
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]

        if len(_authors) == 1:
            authors = _authors[0]
        elif len(_authors) == 0:
            authors = ""
        else:
            authors = ", ".join(_authors[0:-1]) + " and "  # + _authors[-1]

        title = self.data["title"]

        volume = self.data["biblio"]["volume"]

        issue = self.data["biblio"]["issue"]
        if issue is None:
            issue = ", "
        else:
            issue = ", " + issue
        year = self.data["publication_year"]
        citedby = self.data["cited_by_count"]

        o_a = self.data["id"]
        string_rep = f"""{authors}, {title}, {volume}{issue}, ({year}),
        {self.data["doi"]}. cited by: {citedby}. {o_a}"""

        return string_rep

    def __repr__(self):
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]
        if len(_authors) == 1:
            authors = _authors[0]
        else:
            authors = ", ".join(_authors[0:-1]) + " and" + _authors[-1]

        title = self.data["title"]

        volume = self.data["biblio"]["volume"]

        issue = self.data["biblio"]["issue"]
        if issue is None:
            issue = ", "
        else:
            issue = ", " + issue

        pages = "-".join(
            [self.data["biblio"]["first_page"], self.data["biblio"]["last_page"]]
        )
        year = self.data["publication_year"]
        citedby = self.data["cited_by_count"]

        o_a = self.data["id"]
        string_rep = f"""{authors}, {title}, {volume}{issue}{pages}, ({year}),
        {self.data["doi"]}. cited by: {citedby}. {o_a}"""
        return string_rep

    @property
    def ris(self):
        """Function that returns a string, containing a citation in the RIS format"""
        fields = []
        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        ris = "\n".join(fields)
        return ris

    @property
    def bibtex(self):
        """Function that returns a string, containing a citation in the BibTex format"""
        fields = []
        if self.data["type"] == "journal-article":
            fields += [
                "@article{"
                + self.data["authorships"][0]["author"]["display_name"].split()[-1]
                + str(self.data["publication_year"])
            ]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        fields += [
            "author   = {"
            + ",".join(
                [
                    author["author"]["display_name"]
                    for author in self.data["authorships"]
                ]
            )
            + "}"
        ]
        fields += [f"title   = {{{self.data['title']}}}"]
        fields += [f"journal = {{{self.data['host_venue']['display_name']}}}"]
        fields += [f"volume  = {{{self.data['biblio']['volume']}}}"]
        fields += [f"year    = {{{self.data['publication_year']}}}"]
        fields += [
            f"pages   = {{{self.data['biblio']['first_page']}--{self.data['biblio']['last_page']}}}"
        ]
        fields += [f"doi     = {{{self.data['doi']}}}"]
        bibtex = "\n".join(fields)

        return bibtex
