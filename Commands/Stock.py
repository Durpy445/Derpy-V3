import Manage
import Inventory
import matplotlib.pyplot as plt
import random
import time
def Main(User,Args):
    currentTime = time.time()
    currentDay = currentTime // 86400
    
    random.seed(currentDay)
    Today = random.randint(10,200)
    random.seed(currentDay-1)
    M1 = random.randint(10,200)
    random.seed(currentDay-2)
    M2 = random.randint(10,200)
    random.seed(currentDay-3)
    M3 = random.randint(10,200)
    random.seed(currentDay-4)
    M4 = random.randint(10,200)

    X = ["-4","-3","-2","-1","0"]
    Y = [M4,M3,M2,M1,Today]
    plt.plot(X,Y)
    plt.xlabel("History")
    plt.ylabel("Price")
    plt.title("barracuda market")
    plt.savefig('Storage/plot.png',bbox_inches='tight')
    return "plot.png"






