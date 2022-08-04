# Exploratory-Data-Analysis

## Summary:

Data is the currency of the Digital Age, and it is imperative to have tools that allow us to
explore and utilize it in an effective and efficient manner. One of the most important
aspects of Data Analysis is Exploratory Data Analysis (EDA), an approach that
involves summarizing the main characteristics of the data at hand with descriptive
statistics and visualizations.
The objective is to encapsulate all the necessary functionalities for EDA into a singular,
useful package. To this effect, our package will conduct all the important steps such as
Feature Engineering, Statistical Training and Testing, and the key final step of Data
Visualization. This package will allow users to obtain a summary of key descriptive
statistics and visualizations of the dataset provided by them with a single line of code.

## Proposed design:

As summarized above, Exploratory Data Analysis can be split into three important
steps with unique functionalities. Feature Engineering class includes formatting column
headers, displays and drops/fills the missing/duplicate values and drops outliers, which
will come under the data_cleanup() method. It also includes conducting the required
feature splitting, normalization, encoding required to make the data manageable and
ready for training and testing, which will come under the data_engineering().

Statistical Training and Testing class includes a sample dataset for users under the
data_sample() function. It includes the data_train_test() function that will split, train and
test data to find the ideal tuning. It also has the data_compute() function that will be
used to run the statistical and quantitative non-graphical analysis that will be used for the
final data summary.

Data Visualization class includes the data_summary() function that prepares the
summary of graphical and non-graphical visualizations based on the type of analysis
required (univariate or multivariate). It displays key descriptive statistics such as the
five-number summary, distributions and plots based on target/label and information on
the train-test split of the dataset.

The novelty in the project lies in our team doing various steps of EDA encapsulated
within set functions that combine different external libraries such as pandas, sklearn,
matplotlib and seaborn. We aim to use the salient features of these diverse libraries to
create a package capable of producing quality Exploratory Data Analysis. The potential
challenges we face are making the package generic enough to be applicable to all
tabular datasets, identifying the correct methods of engineering the data, and ensuring
that the summary is coherent and useful.

## Creators
```
Sadasivam Natanakumar
Prerna Chander
Saurav Krishna
```
