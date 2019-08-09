from random import *
from math import*
characters = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm ";

target = input("Enter a word: ");
matingpool = [];
children = [];
fitnesses = [];
words = [];
popSize = 400;
mutationRate = 0.1;
best = 0;
bestWord = ""


def crossover(parentA,parentB):
    c = ""
    for i in range(len(parentA)):
        if(random() < 0.5):
            c += parentA[i]
        else:
            c += parentB[i]
    return c;

def mutate(word):
    w = ""
    for i in range(len(word)):
        if(random() < mutationRate):
            w += characters[floor(random() * len(characters))];
        else:
            w += word[i]
    return w;
            

for i in range(popSize):
    s = "";
    for j in range(len(target)):
        s += characters[floor(random()*len(characters))]

    words.append(s);

while bestWord != target:

    for word in words:
        x = 0;
        for i in range(len(word)):
            if(word[i] == target[i]):
                x += 1;
        if(x > best):
            best = x;
            bestWord = word;
        fitnesses.append(x);

    for i in range(len(words)):
        for j in range(fitnesses[i]):
            matingpool.append(words[i])

    while len(children) < popSize:
        parentA = choice(matingpool)
        parentB = choice(matingpool)
        while parentA == parentB:
            parentA = choice(matingpool)
            parentB = choice(matingpool)
        child = crossover(parentA,parentB)
        child = mutate(child)
        children.append(child)

    words = children

    children = []
    matingpool = []
    fitnesses = []

    print(bestWord); 



