import logging
import os
import statistics
import time


NUM_TESTS = int(os.environ['NUM_TESTS'])

logger = logging.getLogger()


def tests(count):
    logging.basicConfig(level=logging.WARNING)

    for _ in range(count):
        start = time.perf_counter()
        logger.error('this is a log')
        end = time.perf_counter()

        yield end - start


if __name__ == '__main__':
    times = list(tests(NUM_TESTS))

    print('Average: {0:.12f}ms'.format(statistics.mean(times) * 1000))
    print('Median:  {0:.12f}ms'.format(statistics.median(times) * 1000))
    print('Min:     {0:.12f}ms'.format(min(times) * 1000))
    print('Max:     {0:.12f}ms'.format(max(times) * 1000))
