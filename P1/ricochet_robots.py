# ricochet_robots.py: Template para implementação do 1º projeto de Inteligência Artificial 2020/2021.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 48:
# 71015 Ricardo Jose Duarte Nunes

from search import Problem, Node, astar_search, breadth_first_tree_search, \
    depth_first_tree_search, greedy_search
import sys
import numpy as np
import copy
import time

class RRState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = RRState.state_id
        RRState.state_id += 1

    def __lt__(self, other):
    	""" Este método é utilizado em caso de empate na gestão da lista de abertos nas procuras informadas. """
    	return self.id < other.id


class BoardElement( object ):
    """ Representacao interna de um tabuleiro de Ricochet Robots. """
    def getPos(self):
        return self.pos
    
    def setPos(self,x,y):
        self.pos=(int(x),int(y))
       
    pass

class Robot( BoardElement ):
    """ Representacao interna de um tabuleiro de Ricochet Robots. """
    def __init__(self,x,y,color,boardLim,isObjective):
        self.color=color
        self.limit=boardLim
        self.setPos(x,y)
        self.isObjective=isObjective

    def getColor(self):
        return self.color

    def getObjective(self):
        return self.isObjective
    
    def setColor(self, color):
        self.color=color

    def isRobot():
        return True
    
    def isBoardLimitBump(self,move):
        if(move=='u' and self.pos[0]-1==0):
            return False
        if(move=='d' and self.pos[0]+1==self.limit+1):
            return False
        if(move=='l' and self.pos[1]-1==0):
            return False
        if(move=='r' and self.pos[1]+1==self.limit+1):
            return False
        return True
    
    def isRobotBump(self,pos,move):
        if(move=='u' and self.pos[0]==pos[0]-1 and self.pos[1]==pos[1]):
            return True
        if(move=='d' and self.pos[0]==pos[0]+1 and self.pos[1]==pos[1]):
            return True
        if(move=='l' and self.pos[1]==pos[1]-1 and self.pos[0]==pos[0]):
            return True
        if(move=='r' and self.pos[1]==pos[1]+1 and self.pos[0]==pos[0]):
            return True
        return False

    def isWallBump(self,wall,posX,posY,direction):

        return (self.pos[0],self.pos[1])==(wall[0],wall[1]) and  wall.direction==direction
    
    pass

class Objective( BoardElement ):
    """ Representacao interna de um tabuleiro de Ricochet Robots. """
    def __init__(self,x,y,color):
        self.color=color
        self.setPos(x,y)

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color=color
    
    def isObjective(self,pos,color):
        return pos == self.getPos() and  color == self.getColor()
    pass

class Wall( BoardElement ):
    """ Representacao interna de um tabuleiro de Ricochet Robots. """
    def __init__(self,direction,x,y):
        self.setPos(x,y)
        self.direction=direction

    def getLocation(self):
        return self.direction
    
    def setLocation(self, direction):
        self.direction=direction

    def display(self):
        print(self.direction + str(self.pos[0]) + str(self.pos[1]))

    def isWallBump(self,posX,posY,direction):    
        return (self.pos[0],self.pos[1])==(posX, posY) and  self.direction==direction
    
    def isWall():
        return True
        
    pass
    
class Board:
    """ Representacao interna de um tabuleiro de Ricochet Robots. """
    
    def __init__(self, boardString,boardLimit,obj,lim):
        self.robotArr=boardString
        self.wallBoard=boardLimit
        self.objective=obj
        self.boardBound=lim

    def printWallBoard(self):
        displayBoard=np.chararray((self.boardBound, self.boardBound))
        displayBoard[:] = ' '

        for r in self.wallBoard:
            print(r.getLocation(),r.getPos())
        
    def printBoard(self):
        displayBoard=np.chararray((self.boardBound, self.boardBound))
        displayBoard[:] = ' '

        for r in self.robotArr:
            displayBoard[r.getPos()[0]-1,r.getPos()[1]-1]=r.getColor()

        return displayBoard

    def isRobot(self,pos,color):
      
        for r in self.robotArr:
            if(r.color == color):
                continue
            if(r.pos==pos):
                return True
            else:
                continue
        return False
    
    def robot_position(self, robot: str):
        """ Devolve a posição atual do robô passado como argumento. """
        for robotInstance in self.robotArr:
            if(robotInstance.getColor()==robot):
                return robotInstance.getPos()
        pass

def parse_instance(filename: str) -> Board:
    """ Lê o ficheiro cujo caminho é passado como argumento e retorna
    uma instância da classe Board. """

    f=open(filename, "r")
    N=int(f.readline())

    robotArr=[]
    wallArr=[]
    
    for i in range(0,4):
        line=f.readline()
        robot=line.split()        
        robotArr.append(Robot(robot[1],robot[2],robot[0],N,False))
        
    line=f.readline()
    objString=line.split()
    objective=Objective(objString[1],objString[2],objString[0])

    
    numWalls=int(f.readline())
             
    for i in range(0,numWalls):
        line=f.readline()
        wall=line.split()
        if(wall[2]=='r'):
            wallArr.append(Wall(wall[2],int(wall[0]),int(wall[1])))
            wallArr.append(Wall('l',int(wall[0]),int(wall[1])+1))
        if(wall[2]=='l'):
            wallArr.append(Wall(wall[2],int(wall[0]),int(wall[1])))
            wallArr.append(Wall('r',int(wall[0]),int(wall[1])-1))
        if(wall[2]=='u'):
            wallArr.append(Wall(wall[2],int(wall[0]),int(wall[1])))
            wallArr.append(Wall('d',int(wall[0])-1,int(wall[1])))
        if(wall[2]=='d'):
            wallArr.append(Wall(wall[2],int(wall[0]),int(wall[1])))
            wallArr.append(Wall('u',int(wall[0])+1,int(wall[1])))
            
    return Board(robotArr,wallArr,objective,N)
    pass



class RicochetRobots(Problem):
    def __init__(self, board: Board):
        """ O construtor especifica o estado inicial. """
        self.initial = RRState(board)
        pass

    def actions(self, state: RRState):
        """ Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento. """
        stBoard=state.board
        walls=stBoard.wallBoard
        actions = []
        robots = ['Y', 'R', 'G', 'B']
        robotActions = ['u', 'l', 'd', 'r']
        tempActions= []

        
        
        """ Cria uma lista com todas as accoes possiveis para todos os robots sem restrições """
        for r in stBoard.robotArr:
            for move in robotActions:
                if(r.isBoardLimitBump(move)):
                    actions.append((r.getColor(),move))

        
        tempActions=actions.copy()
        
        """ Deteta accoes que nao podem ser executadas por causa de barreiras. """
        for a in actions:
            for w in walls:
                robotPos=stBoard.robot_position(a[0])
                if( w.isWallBump(robotPos[0],robotPos[1],a[1])):
                    tempActions.remove(a)
       
        actions=tempActions.copy()
        
        """ Deteta accoes que nao podem ser executadas por causa de outros robots """
        for a in actions:
            for r in stBoard.robotArr:
                        robot2Pos=stBoard.robot_position(a[0])
                        if( r.isRobotBump(robot2Pos,a[1])):
                            tempActions.remove(a)
                            
        actions=tempActions.copy()
        return actions
        pass

    def result(self, state: RRState, action):
        """ Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação retornada deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state). """

        rrsBoard=copy.deepcopy(state.board)
        robotColor=action[0]
        robotMove=action[1]
        wall= Wall('u',0,0)
        
        for r in rrsBoard.robotArr:
            if(r.getColor()==robotColor):
                robot=r
                break

        while(1):
            botPos=rrsBoard.robot_position(robotColor)
            
            robotTemp= Robot(botPos[0],botPos[1],robotColor,rrsBoard.boardBound,False)
            if(robotMove == 'u'):
                robotTemp.setPos(botPos[0]-1,botPos[1])
            if(robotMove == 'd'):
                robotTemp.setPos(botPos[0]+1,botPos[1])
            if(robotMove == 'l'):
                robotTemp.setPos(botPos[0],botPos[1]-1)
            if(robotMove == 'r'):
                robotTemp.setPos(botPos[0],botPos[1]+1)

            
            for w in rrsBoard.wallBoard:
                if(w.getPos()==robot.getPos() and w.direction==robotMove):
                    wall=w
                    break
    
            if(not(robot.isBoardLimitBump(robotMove))
               or rrsBoard.isRobot(robotTemp.getPos(),robotColor)
               or wall.isWallBump(robot.getPos()[0],robot.getPos()[1],robotMove)):
                
                break
            else:
                rrsBoard.robotArr.remove(robot)
                rrsBoard.robotArr.append(robotTemp)
                robot=robotTemp
                
        return RRState(rrsBoard)
    

    def goal_test(self, state: RRState):
        """ Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se o alvo e o robô da
        mesma cor ocupam a mesma célula no tabuleiro. """

        rrsBoard=state.board
        objective = rrsBoard.objective
        robotPos=rrsBoard.robot_position(objective.getColor())
        if(objective.isObjective(robotPos,objective.getColor())):
            state.board.printBoard()
        return objective.isObjective(robotPos,objective.getColor())
        pass

    def h(self, node: Node):
        """ Função heuristica utilizada para a procura A*. """
        
        h=0

        obj=node.state.board.objective
        objPos=node.state.board.objective.getPos()
        wallArr=node.state.board
        botArr=node.state.board.robotArr
        objRobotPos=node.state.board.robot_position(obj.getColor())
        
        for r in botArr:
            h=h+(abs(obj.getPos()[0] - r.getPos()[0]) + abs(obj.getPos()[1] - r.getPos()[1]))
       
        #Manhattham distance        
        return h

        pass

def processResult(node: Node):
    i=0
    processNode=node
    solList = []
    while 1:
        i=i+1
        solList.append(processNode.action)
        if(processNode.depth == 1):
            break;
        processNode=processNode.parent
    print(i)
    for i in reversed(solList):
        print(i[0]+" "+i[1])
    
if __name__ == "__main__":
    fileInput=sys.argv[1]
    board = parse_instance(fileInput)
    problem = RicochetRobots(board)
    solution_node = astar_search(problem)
    processResult(solution_node)
    pass
