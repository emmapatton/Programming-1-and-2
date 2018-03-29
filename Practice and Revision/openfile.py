# Emma Patton 2018-03-02
# Read and Write files 

with open("data/iris.csv") as f:
    for line in f:
        print(line.split(',')[1])

