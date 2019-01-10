A = importdata('cancer.dt');


[Weights, Bias] = Training(A.data);
Validation(A.data,Weights,Bias);