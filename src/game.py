
def start():
    from board import Board

    import pygame, time, sys, redis

    print("This is starting")
   

    pygame.init()
    WIDTH = 660
    HEIGHT = 660

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True
    delta_time = 0.5
    x = 0
    clock = pygame.time.Clock()
    board = Board(WIDTH, HEIGHT, screen)
    board.spawnFood()
    moveTimer = 0
    moveDelay = 1.5   # higher = slower
    

    direction = ["right", "right"]
    gameRunning = True




    while gameRunning:
        while running:



            x += 50 * delta_time
            screen.fill((0, 0, 0))

            board.buildGrid()

            r = redis.Redis(host='localhost', port=6379, db=0)
            xcoordinate, ycoordinate = (r.get("key")).split()
            print("Coordinates" , int(xcoordinate), int(ycoordinate))
            print(int(ycoordinate) > 100)

            if ( int(ycoordinate) > 200) and direction[-1] != "down":
                    direction.pop()
                    direction.append("up")
            if ( int(xcoordinate) < -200 and direction[-1] != "left"):
                        direction.pop()
                        direction.append("right")
            if (int(xcoordinate) > 200) and direction[-1] != "right":
                        direction.pop()

                        direction.append("left")
            if (int(ycoordinate) < -200 and direction[-1] != "up"):
                        direction.pop()

                        direction.append("down")
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:


                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT  )and direction[-1] != "left":
                        direction.pop()
                        direction.append("right")
                    if ( int(ycoordinate) > 100)and direction[-1] != "down":
                        print("working")
                        direction.pop()

                        direction.append("up")
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and direction[-1] != "right":
                        direction.pop()

                        direction.append("left")
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN)and direction[-1] != "up":
                        direction.pop()

                        direction.append("down")
                
        
                        # ADD ANOTHER OPTION TO MOVE SNAKE HEAD WHEN TURNINH
            moveTimer += 1
            if moveTimer >= moveDelay:
                board.moveSnakeHead(direction[-1], direction[-2])
                moveTimer = 0

            if board.checkCollision():
                board.addSnakePart(direction[len(direction)-1])
            if board.validSnakeHead() == False:
                running = False
                
        
            board.addSnake()

            pygame.display.flip() 





            delta_time = clock.tick(20) / 1000
            delta_time = max(0.001, min(0.1, delta_time))
        
        board = Board(WIDTH, HEIGHT, screen)
        direction = ['right', 'right']
        running = True



    pygame.quit()

