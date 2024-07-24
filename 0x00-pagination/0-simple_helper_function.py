#!/usr/bin/env python3
"""
Simple helper function to calculate start and end index
"""
def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    
    Args:
    page (int): the page number.
    page_size (int): the number of items per page.

    Returns:
    tuple: a tuple containing the start and end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

