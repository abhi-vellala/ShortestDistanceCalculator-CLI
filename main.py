import ast
import matplotlib.pyplot as plt
from tsp import TravellingSalesmanProblem
import time

def print_screen(nodes,min_dist,fastest_route):
    print(f"Nodes in the current Network: {nodes}")
    # print(f"Starting Point: {starting_point}")
    print(f"Minimum distance to visit all the nodes: {min_dist}")
    print(f"Fastest route to visit all the nodes: {fastest_route}")
    print("Check the plot for the graph of current network")
    print("Exit the plot to continue")


if __name__ == '__main__':
    print("\n\nWelcome to Travelling Salesperson Problem Interactive Demo!")
    graph = {(1, 2): 10, (2, 3): 35, (3, 1): 15, (3, 4): 30, (1, 4): 20, (2, 4): 25}
    # graph = {(1, 2): 0, (2, 3): 0, (3, 1): 0, (3, 4): 0, (1, 4): 0, (2, 4): 1}
    # starting_point = int(input("Enter your starting point: "))
    # graph = ast.literal_eval(graph)
    starting_point = 1
    travel_sales = TravellingSalesmanProblem()
    nodes,min_dist,fastest_route = travel_sales.TSP(graph, starting_point)
    print_screen(nodes,min_dist,fastest_route)
    travel_sales.plotGraph(graph)
    plt.show()
    main_check = True
    while main_check:
        print("\nOperations")
        print("\nAdd a node: \n  1. Enter the node you wanted to add\n  2. Enter distances between new node to other nodes in the graph as prompted\n"
              "  3. Enter the starting point from which you want to calculate the shortest distance from updated nodes\n"
              "     Syntax: \n        Enter new node to add: 5 \n        Enter distance from 1 to 5: 20 \n        ..... \n"
              "        Enter your starting point: 1")
        print("Delete a node: \n  1. Enter the node you wanted to delete \n"
              "  2. Enter the starting point from which you want to calculate the shortest distance from updated nodes\n"
              "      Syntax: \n        Enter node to delete: 5 \n        Enter your starting point for updated nodes: 1")
        check1 = False
        while not check1:
            try:
                choice = int(input("Choose your operation: 1. Add a node   2. Delete a node  3. End Program\n"))
            except ValueError:
                print("Enter only int type between 1,2 or 3")
            else:
                if choice in [1,2,3]:
                   user_choice = choice
                   check1 = True
                else:
                    print("Choose only 1,2 or 3")

        if user_choice == 1:
            check2 = False
            while not check2:
                try:
                    new_node = int(input("Enter new node to add: "))
                except ValueError:
                    print("Enter node of int type")
                else:
                    if travel_sales.node_check(new_node):
                        # if travel_sales.node_check(new_node):
                        print(f"{new_node} is valid")
                        check2 = True

            check3 = False
            while not check3:
                graph_add_node,nodes = travel_sales.add_node(graph,new_node)
                graph = graph_add_node
                check3 = True
            check4 = False
            while not check4:
                print(f"Updated nodes in the graph: {nodes}")
                try:
                    starting_point = int(input("Enter your starting point from the above nodes: "))
                except ValueError:
                    print("Enter the type int")
                else:
                    if starting_point in nodes:
                        nodes, min_dist, fastest_route = travel_sales.TSP(graph, starting_point)
                        # nodes = updated_nodes
                        print_screen(nodes, min_dist, fastest_route)
                        travel_sales.plotGraph(graph)
                        plt.show()
                        # plt.show(block=False)
                        # plt.sleep(0.001)
                        check4 = True
                    else:
                        print(f"Starting point {starting_point} is not available in the nodes")

        if user_choice == 2:
            if len(nodes) > 2:
                check5 = False
                while not check5:
                    print(f"Current nodes in the graph: {nodes}")
                    try:
                        del_choice = int(input("Enter the node you wanted to delete from above: "))
                    except ValueError:
                        print("Enter the type int")
                    else:
                        if del_choice in nodes:
                            updated_graph, updated_nodes = travel_sales.delete_node(del_choice, graph, nodes)
                            graph = updated_graph
                            nodes = updated_nodes
                            check6 = False
                            while not check6:
                                print(f"Updated nodes in the graph: {nodes}")
                                try:
                                    starting_point = int(input("Enter your starting point from the above nodes: "))
                                except ValueError:
                                    print("Enter the type int")
                                else:
                                    if starting_point in nodes:
                                        nodes, min_dist, fastest_route = travel_sales.TSP(graph, starting_point)
                                        print_screen(nodes, min_dist, fastest_route)
                                        travel_sales.plotGraph(graph)
                                        plt.show()
                                        check6 = True
                                        check5 = True
                                    else:
                                        print(f"Starting point {starting_point} is not available in the nodes")
                        else:
                            print(f"Node {del_choice} is not available in the graph")

            else:
                print("Need at least two nodes to calculate distance! Try adding nodes")


        if user_choice == 3:
            print("Thank you for using Travelling Salesperson Problem Interactive Demo. See you Later!")
            main_check = False


