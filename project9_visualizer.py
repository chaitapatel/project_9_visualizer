import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
        self.last_fig = None

    def __del__(self):
        # Destructor to perform any cleanup if necessary
        pass

    def load_data(self, file_path):
        try:
            print(f"\n== Load Dataset ==")
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print(f"Error loading file: {e}")

    def explore_data(self):
        if self.data is None:
            print("Please load a dataset first!")
            return
        
        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to Main Menu")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                print(self.data.head())
            elif choice == 2:
                print(self.data.tail())
            elif choice == 3:
                print(self.data.columns.tolist())
            elif choice == 4:
                print(self.data.dtypes)
            elif choice == 5:
                print(self.data.info())
            elif choice == 6:
                break
            else:
                print("Invalid choice! Please try again.")

    def perform_dataframe_operations(self):
        if self.data is None:
            print("Please load a dataset first!")
            return
        print("\n== Perform DataFrame Operations ==")
        print("1. Convert columns to Numpy arrays")
        print("2. Mathematical Operations")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            col_name = input("Enter column name to convert to numpy array: ")
            if col_name in self.data.columns:
                arr = self.data[col_name].to_numpy()
                print("Converted Numpy Array:")
                print(arr)
            else:
                print("Column not found!")

    def handle_missing_data(self):
        if self.data is None:
            print("Please load a dataset first!")
            return
        
        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            missing = self.data[self.data.isnull().any(axis=1)]
            if missing.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing)
        elif choice == 2:
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Missing values filled with mean successfully!")
        elif choice == 3:
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped successfully!")
        elif choice == 4:
            val = input("Enter value to replace missing data: ")
            self.data.fillna(val, inplace=True)
            print("Missing values replaced successfully!")

    def generate_descriptive_statistics(self):
        if self.data is None:
            print("Please load a dataset first!")
            return
        print("\n== Descriptive Statistics ==")
        print(self.data.describe())

    def visualize_data(self):
        if self.data is None:
            print("Please load a dataset first!")
            return
            
        print("\n== Data Visualization ==")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")
        choice = int(input("Enter your choice: "))
        
        self.last_fig = plt.figure(figsize=(8, 5))
        
        if choice == 1:
            x = input("Enter x-axis column name: ")
            y = input("Enter y-axis column name: ")
            plt.bar(self.data[x], self.data[y])
            plt.title(f"Bar Plot of {y} vs {x}")
            plt.xlabel(x)
            plt.ylabel(y)
        elif choice == 2:
            x = input("Enter x-axis column name: ")
            y = input("Enter y-axis column name: ")
            plt.plot(self.data[x], self.data[y], marker='o')
            plt.title(f"Line Plot of {y} vs {x}")
            plt.xlabel(x)
            plt.ylabel(y)
        elif choice == 3:
            x = input("Enter x-axis column name: ")
            y = input("Enter y-axis column name: ")
            print("Generating scatter plot...")
            plt.scatter(self.data[x], self.data[y])
            plt.title(f"Scatter Plot of {y} vs {x}")
            plt.xlabel(x)
            plt.ylabel(y)
            print("Scatter plot displayed successfully!")
        elif choice == 4:
            col = input("Enter column name for pie chart: ")
            self.data[col].value_counts().plot.pie(autopct="%1.1f%%")
            plt.title(f"Pie Chart of {col}")
        elif choice == 5:
            col = input("Enter column name for histogram: ")
            plt.hist(self.data[col].dropna(), bins=10)
            plt.title(f"Histogram of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            
        plt.tight_layout()
        plt.show()

    def save_visualization(self):
        if self.last_fig is None:
            print("No visualization found to save. Please generate a plot first!")
            return
        file_name = input("Enter file name to save the plot (e.g., scatter_plot.png): ")
        self.last_fig.savefig(file_name)
        print(f"Visualization saved as {file_name} successfully!")

def main():
    analyzer = SalesDataAnalyzer()
    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("==========================================================")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            path = input("Enter the path of the dataset (CSV file): ")
            analyzer.load_data(path)
        elif choice == 2:
            analyzer.explore_data()
        elif choice == 3:
            analyzer.perform_dataframe_operations()
        elif choice == 4:
            analyzer.handle_missing_data()
        elif choice == 5:
            analyzer.generate_descriptive_statistics()
        elif choice == 6:
            analyzer.visualize_data()
        elif choice == 7:
            analyzer.save_visualization()
        elif choice == 8:
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()