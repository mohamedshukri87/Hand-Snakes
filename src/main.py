from square import Square
import random
import pygame
from food import Food
from snakeObject import Snake
import redis




from board import Board
from game import start 

print("this is running")

if __name__ == '__main__':

    r = redis.Redis(host='localhost', port=6379, db=0)

    r.set("test", "password")
    start()