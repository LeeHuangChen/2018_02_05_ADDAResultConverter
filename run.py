import Configurations as conf
from src import util
from cPickle import dump
import os


def genNidToPidDict():
    nidToPidDict = {}
    with open(conf.nidToPidDir, "r") as f:
        for line in f:
            if len(line)>0:
                arr = line.split("\t")
                nid = int(arr[0].strip())
                pid = arr[1].strip()
                nidToPidDict[nid] = pid
    return nidToPidDict


def main():
    resultDict = {}
    nidToPidDict = genNidToPidDict()

    with open(conf.addaResultDir, "r") as f:
        for line in f:
            arr = line.split("\t")
            nid = int(arr[0].strip())
            s = int(arr[1].strip())
            e = int(arr[2].strip())
            pid = nidToPidDict[nid]

            if pid in resultDict.keys():
                # adda did not provide domain family info, so I just put '1' here
                resultDict[pid].append([1, s, e])
            else:
                resultDict[pid] = [[1, s, e]]

    util.generateDirectories(conf.resultFolder)
    with open(os.path.join(conf.resultFolder, "result.cpickle"), "wb") as f:
        dump(resultDict, f)


if __name__ == '__main__':
    main()
