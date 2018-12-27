#!/usr/bin/env python

import pulp

def main():

    # Maximize 
    #     Z = 4x + 3y 
    # Subject to:
    #     x>=0
    #     y>=2
    #     2y<=25-x
    #     4y>=2x-8
    #     y<=2x-5

    my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)

    x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
    y = pulp.LpVariable('y', lowBound=2, cat='Continuous')

    # Objective function
    my_lp_problem += 4*x + 3*y, "Z"
    
    # Constraints
    my_lp_problem += 2*y + x <= 25
    my_lp_problem += 4*y - 2*x >= -8
    my_lp_problem += y - 2*x <= -5

    print my_lp_problem

    my_lp_problem.solve()
    print pulp.LpStatus[my_lp_problem.status]

    for variable in my_lp_problem.variables():
        print(variable.name + " = " + str(variable.varValue))

    print pulp.value(my_lp_problem.objective)


if __name__ == "__main__":
    main()

