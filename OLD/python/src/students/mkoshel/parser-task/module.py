import re
from collections import Counter

FILENAME = '/tmp/log.log'
PATTERN_STRING = '\"([A-Z]+)\s(\/.+?)(\?.+)?\s(HTTP\/1.1)\"'
NOT_PARSED = []
ALL_STRINGS_COUNT = 0

if __name__ == '__main__':
    result = {}
    common_counter = Counter()
    pattern = re.compile(PATTERN_STRING)
    logfile = open(FILENAME)
    for line in logfile:
        ALL_STRINGS_COUNT +=1
        matched = pattern.findall(line)
        if matched:
            matched = matched[0]
            method, url = matched[0], matched[1]
            if method in result:
                result[method][url] +=1
            else: 
                result[method] = Counter()
                result[method][url] += 1
        else:
            NOT_PARSED.append(line)
    for key in result:
        common_counter.update(result[key])
        print("Count of unique {} requests: {}".format(
                key,
                len(result[key].keys())
            )
        )
    for pos in common_counter.most_common(20):
        print(pos)
    print("total count is {}".format(ALL_STRINGS_COUNT))
    assert sum(common_counter[x] for x in common_counter) == ALL_STRINGS_COUNT
#
# for pos in result['PUT']:
#     print(pos)