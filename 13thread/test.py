from concurrent.futures import ThreadPoolExecutor


def run():
    sum=0
    while True:
        sum+=1


executor = ThreadPoolExecutor(max_workers=4)
executor.submit(run)
executor.submit(run)
executor.submit(run)
executor.submit(run)


