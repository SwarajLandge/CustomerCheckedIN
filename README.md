# CustomerCheckedIN
This web application will help you to see how many customers have been checked in hotel per booking.

# Part 1 code
part1.ipynb file contain the task or python code given to extract number from dictionary conatining list.

# Part 2 code
part2_EDA.ipynb contains EDA of given dataset.
part2_pipeline.ipynb contains pipeline made to preprocess and model(ML) development.
part2_dl.ipynb contains Neural Network model build to predict as asked to do in task.
Also i have provide streamlit code to deploy.

# Question and Answer asked :
## Q.1 )Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution).

Ans - Recently, i was on New York Cab Driver Demand dataset to predict whether in the particular area the probability of getting pickup of customer is high or low for cab Driver.Intially, i have extract the dataset from their website .Then after cleaning and preprocessing the data i have cleaned and extracted all the necessary feature from the dataset.
The main Challange was it was a time series data.I have never worked on time series data before.So i have to look for the material and resources to how to preprocess time series data and analyse it.I know we can use RNN from Deep Learning but processing and extracting information from DateTime column was hard and cumbersome.The common problem associated with time series data is unordered timestamp, missing values ,finding out outliers and noise in the data.Handling Missing value was the most difficult process among all .Our regular Imputation strategy won’t work here.So from online resource i learnt that Interpoalation is a technique that can handle missing value by estimating using two surrounding known points.Then i denoise the data.Outliers here can be detected when there is a sudden drop in trend line.Then it was taken care of using K-Mean clustering and identifying points which are not in clusters are outliers.
For me it was recent problem which i came across and i have learnt so many new stuffs and nearly took a week to understand and implement it successfully.


## Q.2 ) Explain back propagation and tell us how you handle a dataset if 4 out of 30 parameters have null values more than 40 percentage 

Ans - i ) Backpropagation : To calculate gradients efficiently for our neural network we use method known as Backpropagation.The main idea of backpropagation algorithm is to propagate errors from the output layer back to the input layer by a chain rule.The chain rule is similar to the one which we uses to calculate derivatives if our function is F(G(x)).Propagate the error from the cost function back to each layer and update weights of them according to the error message.It uses iterative, recursive and efficient method to update weights (parameters, bias)and improve neural network .

	ii)To handle data if 4 out of 30 parameters have null values more than 40 percentage :
Just Deleting a particular row will be a bad idea here because we will lose data information as more than 50% are not NULL value for a particular column.Our Dataset may add some bias due to deletion.
For Numerica Data we can replace with mean or median or mode of particular column using Column Transformer and SimpleImputer function.Stratergy will depend on which type of value we have for continuous numeric value it is better to use mean or median (median is less affected by outliers ), if we have categorical numeric value we can use mode stratergy replacing NULL value with most frequent occurring value.
We can predict the Missing value with the help of Machine Learning algorithm.We can predict the missing value from the datset who do not contain NULL value.The type of algorithm will depend on feature/column type and which gives better accuracy.
The best still now i used was using KNN algorithm and replace missing value.KNN algorithm using some K value and distance measure can be used to impute estimation.But we may have to take care of Curse of Dimensionality.

