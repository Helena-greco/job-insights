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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
