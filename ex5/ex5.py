import cvxpy as cp 

x = cp.Variable(2)

constraints = [(x[0]-1)**2 + (x[1]-1)**2<= 1,
               (x[0]+1)**2 + (x[1]+1)**2 <= 1]     

obj = cp.Minimize(x[0]**2 + x[1]**2)

prob = cp.Problem(obj, constraints)
prob.solve()

print(x.value)