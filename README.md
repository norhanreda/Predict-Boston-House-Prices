# Predict-Boston-House-Prices

this machine learning problem aims to  predict the price of houses in Boston using a machine learning algorithm called Linear Regression. Linear regression is a
linear approach to modeling the relationship between a scalar response(or dependent variable)
and one or more explanatory variables (or independent variables).

![image](https://github.com/norhanreda/Predict-Boston-House-Prices/assets/88630231/0dc1c442-07ec-4e4e-b31e-e156d73bba44)

# dataset url

<p>data_url = "http://lib.stat.cmu.edu/datasets/boston" </p>
 <p>raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)</p>
<p>data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]]) </p>
<p>target = raw_df.values[1::2, 2] </p>


## Contributers
<table>
  <tbody><tr>
    <td align="center">
    <a href="https://github.com/norhanreda">
   <img class="avatar rounded-2 avatar-user" src="https://avatars.githubusercontent.com/u/88630231?s=400&amp;u=52eadd25f01f8d9c6b403c087da4d345054f8e0b&amp;v=4" width="200" height="200" alt="@norhanreda">
    <br>
    <sub><b>Norhan Reda</b></sub></a>
  </td></tr>
 </tbody></table>
