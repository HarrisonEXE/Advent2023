import os
import re


def extractNumsFromLine(line):
    nums = re.findall("[0-9]", line)
    combined_num = str(nums[0]) + str(nums[-1])
    return int(combined_num)


def processInput(filename):
    with open(filename) as f:
        sum = 0
        for line in f.readlines():
            sum += extractNumsFromLine(line)
        print(sum)


if __name__ == '__main__':
    os.chdir('Day 1')
    processInput('input.txt')
