# Predict-Boston-House-Prices

this machine learning problem aims to  predict the price of houses in Boston using a machine learning algorithm called Linear Regression. Linear regression is a
linear approach to modeling the relationship between a scalar response(or dependent variable)
and one or more explanatory variables (or independent variables).

![image](https://github.com/norhanreda/Predict-Boston-House-Prices/assets/88630231/0dc1c442-07ec-4e4e-b31e-e156d73bba44)

# dataset url

<p>data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2] </p>
