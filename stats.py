import math
from collections import Counter

class Stats:
    def mean(self, inputs): return sum(inputs) / len(inputs)

    def mode(self, inputs):
        d = Counter(inputs)
        return max(d, key=d.get)

    def median(self, inputs):
        l = len(inputs)
        mid = l // 2
        if l % 2 == 0: return (inputs[mid] + inputs[mid - 1]) / 2
        return inputs[mid]

    def variance(self, inputs):
        m = self.mean(inputs)
        return sum((x - m) ** 2 for x in inputs) / len(inputs)

    def s_variance(self, inputs):
        m = self.mean(inputs)
        return sum((x-m)**2 for x in inputs)/(len(inputs)-1)

    def std(self, inputs):
        """sqrt of variance"""
        return math.sqrt(self.variance(inputs))

    def q1(self, inputs):
        """
        25th percentile
         - 25/100 * (n-1) where n is the number of inputs
        """
        return (len(inputs) - 1)/4

    def q3(self, inputs):
        """
        75th percentile
         - 75/100 * (n-1) where n is the number of inputs
        """
        return (len(inputs) -1)*(3/4)

    def iqr(self, inputs):
        """
        Q3th - Q1th"""
        return self.q3(inputs) - self.q1(inputs)
        
    def lower_fence(self, inputs):
        """q1 - 1.5(IQR)"""
        return self.q1(inputs) - (1.5*(self.iqr(inputs)))

    def higher_fence(self, inputs):
        """q3 + 1.5(IQR)"""
        return self.q3(inputs) + (1.5*(self.iqr(inputs)))

    def inliers(self, inputs):
        return (self.lower_fence(inputs), self.higher_fence(inputs))

    def five_n_sum(self, inputs):
        """5 number summary"""
        inliers = self.inliers(inputs)
        return {
            "min": min(inputs),
            "1st quartile": self.q1(inputs),
            "median": self.median(inputs),
            "3rd quartile": self.q3(inputs),
            "maximum": max(inputs),
            "outliers": [i for i in inputs if i < inliers[0] or i > inliers[-1]]
        }

    def pearson_corel_coef(self, x, y):
        """ Pearson corelation coefficent """
        c = self.cov(x,y)
        x_std = self.std(x)
        y_std = self.std(y)
        return c/(x_std*y_std)

    def cov(self, x: list, y: list) -> float:
        """covariance
        if you want to print the out method in loop
        print(f"({x[i]} - {x_mean})*({y[i]}-{y_mean})")
        """
        x_mean = int(self.mean(x))
        y_mean = int(self.mean(y))
        if len(x) != len(y): raise Exception("items should be of same lenght")
        out = sum([(x[i] - x_mean)*(y[i] - y_mean) for i in range(len(x))])
        return out/len(x)

    def s_cov(self ,x: list, y: list) -> float:
        """standard covariance"""
        x_mean = int(self.mean(x))
        y_mean = int(self.mean(y))
        if len(x) != len(y): raise Exception("items should be of same lenght")
        out = sum([(x[i] - x_mean)*(y[i] - y_mean) for i in range(len(x))])
        return out/(len(x)-1)


i = [-10,1,2,3,4,5, 5 ,9 ,9 ,9 ,10 ,5 ,10 ,10,11, 44]
s = Stats()
print(f"{s.variance(i):.2f}")
print(s.s_variance(i))
print(f"{s.std(i):.2f}")
print(s.inliers(i))
print(s.five_n_sum(i))

x = [2,3,4,5,6]
y = [50,60,70,80,90]
# print(s.cov(x, y))
print(s.pearson_corel_coef(x, y))