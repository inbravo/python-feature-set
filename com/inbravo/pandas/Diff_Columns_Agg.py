"""Class to test the aggregation function in Python pandas library"""

import pandas as pd

# Create a DataFrame with some sample data
# The DataFrame is then converted to a pandas DataFrame using the pd.DataFrame() function
# The DataFrame contains three columns: Maths, English, and Science
# Each column contains three rows of data
# The DataFrame is created using a list of lists, where each inner list represents a row of data
# The columns are specified using the columns parameter
df = pd.DataFrame(
    [[100, 95, 87], [94, 92, 81], [75, 74, 78], [95, 87, 98], [90, 82, 93]],
    columns=["Maths", "English", "Science"],
)
print(df)

# Now let us try to see the total numbers scored by each student in all the subjects
# The agg() function is used to apply the sum function to each column of the DataFrame
# In this case, the sum function is applied to each column of the DataFrame
# Aggregating sum along axis 1
total_score_df = df.agg(["sum"], 1)
print(total_score_df)

# Now let us try to get the average marks of students across all subjects.
avg_score_df = df.agg(["average"], 0)
print(avg_score_df)
