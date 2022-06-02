from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        jobs = csv.DictReader(file)
        job_list = []
        for job in jobs:
            job_list.append(job)

    return job_list


read("src/jobs.csv")
