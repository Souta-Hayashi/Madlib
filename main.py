from sample_madlibs import love, motorcar
import random

if __name__ == "__main__":
    m = random.choice([love, motorcar])
    m.madlib()