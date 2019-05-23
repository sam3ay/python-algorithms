#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_algorithms` package."""

import pytest


from python_algorithms import python_algorithms
from python_algorithms import count


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_count():
    """test count function
    """
    true_string = (
                  "AGCTTTTCATTCTGACTGCAACGGGCAATATGT"
                  "CTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
            
    empty_string = ""
    true_dict = count.count_letters(true_string)
    assert isinstance(true_dict, dict)
    assert true_dict['A'] == 20
    assert true_dict['C'] == 12
    assert true_dict['G'] == 17
    assert true_dict['T'] == 21
    assert sum(count.count_letters(empty_string).values()) == 0
