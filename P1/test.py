# test.py: Podem usar este script para testar a vossa implementação. Para tal, devem correr o
# script e verificar que o output que obtêm de cada teste é igual ao apresentado no enunciado do
# projeto. Além dos testes presentes, podem acrescentar outros.

from ricochet_robots import *
from search import *

def test1():
    # Ler tabuleiro do ficheiro i1.txt:
    board = parse_instance("instances/i1.txt")

    # Imprimir as posições dos robôs:
    print(board.robot_position('Y'))
    print(board.robot_position('G'))
    print(board.robot_position('B'))
    print(board.robot_position('R'))

def test2():
    # Ler tabuleiro do ficheiro 'i1.txt':
    board = parse_instance("instances/i1.txt")


    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)

    # Criar um estado com a configuração inicial:
    initial_state = RRState(board)

    # Mover o robô azul para a esquerda:
    result_state = problem.result(initial_state, ('B', 'l'))

    # Imprimir a posição do robô azul:
    print(result_state.board.robot_position('B'))

def test3():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/i1.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)

    # Criar um estado com a configuração inicial:
    s0 = RRState(board)

    # Aplicar as ações que resolvem a instância
    s1 = problem.result(s0, ('B', 'l'))
    s2 = problem.result(s1, ('Y', 'u'))
    s3 = problem.result(s2, ('R', 'r'))
    s4 = problem.result(s3, ('R', 'u'))

    # Verificar que o robô está no alvo:
    print(problem.goal_test(s4))
    print(s4.board.robot_position('R'))

def test4():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/i0.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    processResult(solution_node)
    #print("done.")

def test5():
    board = parse_instance('instances/i3.txt')
    
    # Verificar as posições dos robôs:
    print(board.robot_position('Y'))
    print(board.robot_position('G'))
    print(board.robot_position('B'))
    print(board.robot_position('R'))
    
    # ---
    board = parse_instance('instances/i4.txt')
    
    print(board.robot_position('R'))
    print(board.robot_position('G'))
    print(board.robot_position('B'))
    print(board.robot_position('Y'))

def test6():
    board = parse_instance('instances/i1.txt')
    problem = RicochetRobots(board)
    initial_state = RRState(board)
    
    # Mover o robô azul para a esquerda (deve bater numa barreira):
    result_state = problem.result(initial_state, ('B', 'l'))
    print(result_state.board.robot_position('B'))
  
    
def test7():
    # ---
    board = parse_instance('instances/i2.txt')
    problem = RicochetRobots(board)
    initial_state = RRState(board)
    
    # Mover o robô azul para a esquerda. Não deve alterar a posição do robô:
    s1 = problem.result(initial_state, ('B', 'l'))
    print(s1.board.robot_position('B'))
    
    # Mover o robô amarelo para baixo:
    s1 = problem.result(initial_state, ('Y', 'd'))
    
    # Mover robô azul para baixo. Deve colidir com o amarelo:
    s2 = problem.result(s1, ('B', 'd'))
    
    # Imprimir a posição dos robôs:
    print(s2.board.robot_position('Y'))
    print(s2.board.robot_position('B'))
    
    # Mover robô azul para baixo. Não deve alterar a posição do robô:
    s3 = problem.result(s1, ('B', 'd'))
    print(s3.board.robot_position('Y'))

def test8():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/i1.txt")
    problem = RicochetRobots(board)
    s0 = RRState(board)
    
    # Aplicar as ações que resolvem a instância
    print(('B', 'l') in problem.actions(s0))
    s1 = problem.result(s0, ('B', 'l'))
    print(('Y', 'u') in problem.actions(s1))
    s2 = problem.result(s1, ('Y', 'u'))
    print(('R', 'r') in problem.actions(s2))
    s3 = problem.result(s2, ('R', 'r'))
    print(('R', 'u') in problem.actions(s3))
    s4 = problem.result(s3, ('R', 'u'))
    
    # Verificar que o robô está no alvo só no último estado:
    print(problem.goal_test(s0))
    print(problem.goal_test(s1))
    print(problem.goal_test(s2))
    print(problem.goal_test(s3))
    print(problem.goal_test(s4))
    print(s4.board.robot_position('R'))
    
    # ---
    # Ler tabuleiro do ficheiro "i11.txt":
    board = parse_instance("instances/i11.txt")
    problem = RicochetRobots(board)
    s0 = RRState(board)
    
    # Aplicar as ações que resolvem a instância
    print(('Y', 'l') in problem.actions(s0))
    s1 = problem.result(s0, ('Y', 'l'))
    print(('R', 'l') in problem.actions(s1))
    s2 = problem.result(s1, ('R', 'l'))
    print(('R', 'u') in problem.actions(s2))
    s3 = problem.result(s2, ('R', 'u'))
    print(('B', 'd') in problem.actions(s3))
    s4 = problem.result(s3, ('B', 'd'))
    print(('B', 'r') in problem.actions(s4))
    s5 = problem.result(s4, ('B', 'r'))
    print(('B', 'u') in problem.actions(s5))
    s6 = problem.result(s5, ('B', 'u'))
    print(('B', 'r') in problem.actions(s6))
    s7 = problem.result(s6, ('B', 'r'))
    print(('B', 'd') in problem.actions(s7))
    s8 = problem.result(s7, ('B', 'd'))
    print(('B', 'r') in problem.actions(s8))
    s9 = problem.result(s8, ('B', 'r'))

    # Verificar que o robô está no alvo só no último estado:
    print(problem.goal_test(s1))
    print(problem.goal_test(s2))
    print(problem.goal_test(s3))
    print(problem.goal_test(s4))
    print(problem.goal_test(s5))
    print(problem.goal_test(s6))
    print(problem.goal_test(s7))
    print(problem.goal_test(s8))
    print(problem.goal_test(s9))
    print(s7.board.robot_position('B'))


def moosh1():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t1.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh2():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t2.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh3():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t3.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh4():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t4.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh5():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t5.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh6():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t4.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh7():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t7.txt")

   # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh8():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t8.txt")

   # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh9():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t9.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh10():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t10.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)

def moosh11():
    # Ler tabuleiro do ficheiro "i1.txt":
    board = parse_instance("instances/t11.txt")

    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    start = time.time()

    # Obter o nó solução usando a procura A*:
    solution_node = astar_search(problem)
    end = time.time()
    processResult(solution_node)
    print(end - start)
    
    
def instanceTest():
    # Ler tabuleiro do ficheiro i1.txt:
    board = parse_instance("instances/i1.txt")
    # Criar uma instância de RicochetRobots:
    problem = RicochetRobots(board)
    board1 = parse_instance("instances/i2.txt")
    # Criar uma instância de RicochetRobots:
    problem1 = RicochetRobots(board1)
    board2 = parse_instance("instances/i3.txt")
    # Criar uma instância de RicochetRobots:
    problem2 = RicochetRobots(board2)
    board3 = parse_instance("instances/i4.txt")
    # Criar uma instância de RicochetRobots:
    problem3 = RicochetRobots(board3)

    start = time.time()

    compare_searchers(problems=[problem3],
                      header=['Searcher', 'i1','i2','i3','i4'],
                      searchers=[
                                 #breadth_first_graph_search,
                                 #depth_first_graph_search,
                                 #greedy_search,
                                 astar_search
                                 ])
    end = time.time()
    print(end - start)

def MooshaskTest():
    print("---")
    test1()
    print("---")
    test2()
    print("---")
    test3()
    print("---")
    test4()
    print("---")
    test5()
    print("---")
    test6()
    print("---")
    test7()
    print("---")
    test8()
    print("---moosh1")
    moosh1()
    print("---moosh2")
    moosh2()
    print("---moosh3")
    moosh3()
    print("---moosh4")
    moosh4()
    print("---moosh5")
    moosh5()
    print("---moosh6")
    moosh6()
    print("---moosh7")
    moosh7()
    print("---moosh8")
    moosh8()
    print("---moosh9")
    moosh9()
   

if __name__ == "__main__":
    print("Relatorio ")
    instanceTest()

