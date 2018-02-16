import Configurations as conf
from src import util
from cPickle import dump, load
import os


# def genNidToPidDict():
#     nidToPidDict = {}
#     with open(conf.nidToPidDir, "r") as f:
#         for line in f:
#             if len(line)>0:
#                 arr = line.split("\t")
#                 nid = int(arr[0].strip())
#                 pid = arr[1].strip()
#                 nidToPidDict[nid] = pid
#     return nidToPidDict


def main():
    borderFiles = os.listdir(conf.addaResultFolder)

    for i, borderFile in enumerate(borderFiles):
        resultDict = {}
        nidToPidPath = os.path.join(conf.nidToPidFolder, borderFile)
        nidToPidDict = load(open(nidToPidPath, "rb"))

        addaDir = os.path.join(conf.addaResultFolder, borderFile)
        with open(addaDir, "r") as f:
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
        with open(os.path.join(conf.resultFolder, borderFile+".cpickle"), "wb") as f:
            dump(resultDict, f)


if __name__ == '__main__':
    main()
