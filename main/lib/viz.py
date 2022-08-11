import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import lib.stats as st

default = 'data/iris.csv'


class viz:
    
    def __init__(self, data=default):
        self.data = st.stats(data)

    def plots(self,f1,f2,f3,f8,five_num_df,data):
        """
        Creates various kinds of plots 
        1. A pie chart to show the train-test split
        2. A table showcasing the five number summary for each feature
        3. A histogram plot using a feature of the user's choice
        4. A 2-D scatter plot using two features of the user's choice
        5. A pair plot containing all the features
        param f1,f2 : Two features for a 2-D scatter plot
              f3 : One feature for a histogram plot
              five_num_df: A DataFrame with the five number summary of the dataset
              file_name : CSV dataset
        returns : None
        """
        df = self.data.data
        pie_labels=["Train","Test"]                # Set pie labels
        train,test= self.data.split_train_test()     # Call train test split function
        fig, axs = plt.subplots(nrows=2,ncols=2)   # Setup subplots to plot various figures
    
        axs[0][0].set_title("Train-Test Split")    # Set heading for subplot 1
        axs[0][0].pie([len(train),len(test)],labels=pie_labels,autopct='%.0f%%') # Plot a pie chart
    
        axs[0][1].axis('off')
        axs[0][1].set_title("Five Number Summary")     # Set heading for subplot 2
        table=axs[0][1].table(cellText=five_num_df.values, colLabels=five_num_df.columns, loc='upper center') # Showcase a table containing five number sum
        table.auto_set_font_size(False)
        table.set_fontsize(6)                      # Set font size and scale
        table.scale(1, 2)
    
        sns.histplot(ax=axs[1][0],data=df,x=f3,hue=f8,kde=True) # PLot a histogram
        axs[1][0].set_title("Histogram")                               # Set heading for subplot 3
    
        sns.scatterplot(ax=axs[1][1],data=df,x=f1,y=f2,hue=f8); # Plot a 2-D scatter plot
        axs[1][1].set_title("2-D Scatter Plot");                       # Set heading for subplot 4
    
        plt.show(block=False)                                          # Show the whole plot
    
        g=sns.pairplot(data=self.data.data, hue=f8);                        # Plot a pairplot
        g.fig.suptitle("Pair Plots")                                   # Set heading for the pairplot
        plt.show()   
         
    def select_options(self,data):
        """
        Gives the users a list of features to choose from for a 2-D scatter plot and a histogram plot
        param file_name: CSV dataset
        returns: None
        """
        options_dict={}                         # Assign an empty dictionary
        df=self.data.data
        five_num_df = self.data.five_number_summary(df)
    
        for i in range(len(df.columns)):  
            options_dict[i+1]=df.columns[i]     # Fill up the dictonary with columns from the dataframe that can be used as features
    
        select_df = pd.DataFrame(options_dict.items(), columns=["Option","Feature"])  # Create a dataframe to display options to select for plots
    
        print(select_df.to_string(index=False))                                       # Display the options to be selected
        success=False
        while success is not True:
            try:                                    
                f1,f2=input("Select two options as features for a 2-D scatter plot: ").split()  # Ask the user to select two features for a 2-D scatter plot
                f1=options_dict[int(f1)]    # Convert the dictonary's keys into integers
                f2=options_dict[int(f2)]
                success=True
            except KeyError:                # Validate the entered choices
                print("Wrong choice, please try again")  
                print(select_df.to_string(index=False))
            except ValueError:
                print("Please enter two choices")
                print(select_df.to_string(index=False))
    
        print(select_df.to_string(index=False))  # Display the options to be selected
        success=False
        while success is not True:
            
            try:                                    
                f3=input("Select one option as a feature for a Histogram: ")                   # Ask the user to select one feature for a histogram
                f3=options_dict[int(f3)]    # Convert the dictonary's keys into an integer
                success=True
            except KeyError:                # Validate the entered choice
                print("Wrong choice, please try again")# Display the options to be selected
                df.to_string(index=False)
        print(select_df.to_string(index=False))  # Display the options to be selected
        success=False
        while success is not True:
            try:                                    
                f8=input("Select a variable for color encoding for all: ")                # Ask the user to select one feature for a histogram
                # f4=options_dict[int(f4)]    # Convert the dictonary's keys into an integer
                # f5=options_dict[int(f5)]
                # f6=options_dict[int(f6)]
                # f7=options_dict[int(f7)]
                f8=options_dict[int(f8)]
                # pair_list = [f4,f5,f6,f7]
                success=True
            except KeyError:                # Validate the entered choice
                print("Wrong choice, please try again")# Display the options to be selected
                df.to_string(index=False)
        # temp = []
        # for i in pair_list:
        #     temp.append(df[i].values)
        self.plots(f1,f2,f3,f8,five_num_df,df)  # Call the plots function
          # Call the five_number_summary function
# select_options(five_num_df,data)       # Call the select options function                  
    
    
    
    
