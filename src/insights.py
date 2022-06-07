from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_list = set()
    for job in jobs:
        job_list.add(job["job_type"])
    return job_list


def filter_by_job_type(jobs, job_type):
    list_filtered = [job for job in jobs if job["job_type"] == job_type]
    return list_filtered


def get_unique_industries(path):
    jobs = read(path)
    insdustry_list = set()
    for job in jobs:
        if job["industry"] != '':
            insdustry_list.add(job["industry"])
    return insdustry_list


def filter_by_industry(jobs, industry):
    list_filtered = [job for job in jobs if job["industry"] == industry]
    return list_filtered


def get_max_salary(path):
    jobs = read(path)
    salary_list = list()
    max_salary = 0
    for job in jobs:
        if job["max_salary"].isdigit():
            salary_list.append(int(job["max_salary"]))
            max_salary = max(salary_list)
    return max_salary


def get_min_salary(path):
    jobs = read(path)
    salary_list = list()
    min_salary = 0
    for job in jobs:
        if job["min_salary"].isdigit():
            salary_list.append(int(job["min_salary"]))
            min_salary = min(salary_list)
    return min_salary


def matches_salary_range(job, salary):
    if ("min_salary" or "max_salary") not in job:
        raise ValueError("min or max salary doesn't exist in dict")
    elif type(job["min_salary"] or job["max_salary"]) != int:
        raise ValueError("min_salary or max_salary is not a number")
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary can not be greater than max_salary")
    elif type(salary) != int:
        raise ValueError("salary is not a number")
    elif salary < job["min_salary"] or salary > job["max_salary"]:
        return False

    return True


def filter_by_salary_range(jobs, salary):
    salary_filtered = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_filtered.append(job)
        except ValueError:
            pass
    return salary_filtered
