import input_data_file as in_f
import output_matrix as out_m
import matrix_s as m_s
import matrix_isomorphic as m_i

matrix={}
n=0
m=0
(matrix,n,m)=in_f.input_data('data.txt')
matrix=m_s.return_matrix_s(matrix,n,m)
print('Задание 1')
out_m.print_matrix(matrix,n)
print('Задание 2')
matrix=matrix1={}
n=n1=0
m=m1=0
(matrix,n,m)=in_f.input_data('file1.txt')
(matrix1,n1,m1)=in_f.input_data('file2.txt')
print(m_i.isomorphic(matrix,matrix1,n,n1))
input('Нажмите Enter для выхода\n')


        
    
               
                
        
