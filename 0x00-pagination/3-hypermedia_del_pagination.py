#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary for deletion-resilient pagination"""
        assert type(index) is int and index >= 0
        assert type(page_size) is int and page_size > 0

        indexed_dataset = self.indexed_dataset()
        data = []
        next_index = index
        while len(data) < page_size and next_index < len(indexed_dataset):
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data,
        }

