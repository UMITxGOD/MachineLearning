class linearRegression:
    def __init__(self) -> None:
        pass
    
    def mean(self,x):
        return sum(x)/float(len(x))
    
    def cov(self,x,y):
        diff_x_mean = diff_y_mean =result= 0
        x_mean = self.mean(x)
        y_mean = self.mean(y)
        for x_Data , y_Data in zip(x,y):
            diff_x_mean = x_Data - x_mean
            diff_y_mean = y_Data - y_mean
            result +=diff_x_mean*diff_y_mean
        return ((result)/(len(x) - 1))
    
    def var(self,x):
        mean_squared_value = temp = 0 
        x_mean=self.mean(x)
        for x_Data in x:
            temp = x_Data - x_mean
            mean_squared_value += temp ** 2 
        return ((mean_squared_value) / (len(x) - 1 ) )
    
    def W1(self,x,y):
        cov_xy =  self.cov(x,y)
        var_x  = self.var(x)
        return cov_xy/var_x
    
    def W0(self,x,y,W1):
        y_mean = self.mean(y)
        x_mean = self.mean(x)
        return y_mean - (W1*x_mean)
    def predict(self,x,W0,W1): 
        result=[]
        for predict_data in x :
           result.append( W0 + W1*predict_data) 
        return result

model = linearRegression()

Independent_data = []
for i in range(1,101,1):
	Independent_data.append(i)	

print("Given Independent Data is ",Independent_data)

dependent_data =  []

for i in range(1,101,1):
	dependent_data.append(i*2)

print("Given Dependent Data is ",dependent_data)

testing_data = [1000,2000,3000]
print("Given Testing Data is ",testing_data)


W1=model.W1(Independent_data,dependent_data)
W0=model.W0(Independent_data,dependent_data,W1)


equation_formed = "EQUATION FORMED : Y = {} + {}\tX"

print(equation_formed.format(W0,W1))

result=model.predict(testing_data,W0,W1)

print("Predicted Result is ", result)

from matplotlib.pyplot import show,scatter,plot 
scatter(Independent_data,dependent_data)
plot(testing_data,result,"o--r")
show()


