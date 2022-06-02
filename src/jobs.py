from functools import lru_cache
import csv

@lru_cache
def read(path):
    with open("jobs.csv", encoding = "utf-8") as file:
        jobs = csv.DictReader(file)
        job_list = []
        for job in jobs:
            job_list.append(job)

    return job_list
    """Reads a file from a given path and returns its contents.

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
