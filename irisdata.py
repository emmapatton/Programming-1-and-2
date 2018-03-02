# Emma Patton, 2018-03-02
# Iris data set numerical values printed and formatted
# Data obtained from: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

with open("data/iris.csv") as f:
    for line in f:
        irisnum = line.split(',')[:4]

        print('{}  {}  {}  {}'.format(*irisnum))
