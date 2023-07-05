from GaussElimination_Class import GaussElimination

#Test
Dim = list(map(int, input("행렬의 크기를 입력 (Ex: row,col) :").split(",")))

A = GaussElimination.random_matrix(Dim[0],Dim[1])
GaussElimination.gauss_jordan_elimination(A)