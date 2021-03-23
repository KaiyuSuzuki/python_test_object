import numpy as np


def main(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    lines = [line.replace("\n", "").split(":") for line in lines]
    i_list = [int(line[0]) for line in lines[:-1]]
    s_list = [line[1] for line in lines[:-1]]
    m = int(lines[-1][0])
    indices = np.argsort(i_list)

    ret = ""
    for index in indices:
        i = i_list[index]
        s = s_list[index]

        if m % i == 0:
            ret += s

    if ret == "":
        ret = m

    return ret

if __name__ == '__main__':
    file_name = "input.txt"
    ret = main(file_name)
    print(ret)