#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing the following
key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns  start index and an end index"""
    return ((page - 1) * page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Use assert to verify that both arguments are integers greater than 0.
        Use index_range to find the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset
        (i.e. the correct list of rows).
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        a, z = index_range(page, page_size)
        return self.dataset()[a: z]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """hypermedia implementation"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        data = self.get_page(page, page_size)
        prev_page = page - 1 if page != 1 else None
        next_page = page + 1 if page != total_pages else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
