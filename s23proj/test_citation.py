"""This module contains facilities for tests"""

import pytest
from s23proj import Works

RIS = """TY  - JOUR
AU  - John R. Kitchin
Y1  - 2015/06/05
PY  - 2015
DA  - 2015/06/05
N1  - doi: 10.1021/acscatal.5b00538
DO  - 10.1021/acscatal.5b00538
T2  - ACS Catalysis
JF  - ACS Catalysis
JO  - ACS Catal.
SP  - 3894
EP  - 3899
VL  - 5
IS  - 6
PB  - American Chemical Society
M3  - doi: 10.1021/acscatal.5b00538
UR  - https://doi.org/10.1021/acscatal.5b00538
ER  - """

BIBTEX = """@article{kitchin_examples_2015
title = {Examples of {Effective} {Data} {Sharing} in {Scientific} {Publishing}}
volume = {5}
issn = {2155-5435, 2155-5435}
url = {https://pubs.acs.org/doi/10.1021/acscatal.5b00538}
doi = {10.1021/acscatal.5b00538}
language = {en}
number = {6}
urldate = {2023-04-24}
journal = {ACS Catalysis}
author   = {John R. Kitchin}
month = jun
year = {2015}
pages = {3894--3899}
file = {Full Text:/home/nick/Zotero/storage/HCTQZ6R2/Kitchin - 2015 - Examples of Effective Data Sharing in Scientific P.pdf:application/pdf}
}
"""

# Arrange
@pytest.fixture
def work_ris():
    """Pytest fixture for comparing the authors in a RIS formatted citation"""
    work = Works("https://doi.org/10.1021/acscatal.5b00538")
    return work.ris.split("\n")[1]


@pytest.fixture
def work_bibtex():
    """Pytest fixture for comparing the authors in a Bibtex formatted citation"""
    work = Works("https://doi.org/10.1021/acscatal.5b00538")
    return work.bibtex.split("\n")[1]


def test_work_ris(work_ris):
    """The function for a RIS test"""
    auth_reference = RIS.split("\n")[1]

    # Assert
    assert work_ris == auth_reference


def test_work_bibtex(work_bibtex):
    """The function for a Bibtex test"""
    auth_reference = BIBTEX.split("\n")[10]

    # Assert
    assert work_bibtex == auth_reference
