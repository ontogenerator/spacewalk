import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    """
    Read data from JSON file into a Pandas dataframe.
    CLean the data by removing incomplete rows and sort by date.

    Args: 
        input_file (str): The path to the JSON file.
    
    Returns:
        eva_df (pd.DataFrame): The cleaned, sorted data as a dataframe.
    """
    print(f'Reading JSON file {input_file}')
    # Read the data from a JSON file into a Pandas dataframe
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    # Clean the data by removing any incomplete rows and sort by date
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    """
    Export dataframe to output file in CSV format.

    Args:
        df (pd.DataFrame): The dataframe to be exported.
        output_file (str): The path to the output file.
    
    Returns:
        None
    """
    print(f'Saving to CSV file {output_file}')
    # Save dataframe to CSV file for later analysis
    df.to_csv(output_file, index=False)


# Main code

print("--START--")

input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

# Read the data from JSON file
eva_data = read_json_to_dataframe(input_file)

# Convert and export data to CSV file
write_dataframe_to_csv(eva_data, output_file)

def plot_cumulative_time_in_space(df, graph_file):
    """
    Calculate cumulative time spent in space and plot by date.

    Args:
        df (pd.DataFrame): The dataframe to be plotted.
        graph_file (str): The path to the output plot file.

    """
    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    # Calculate cumulative time spent in space
    df['duration_hours'] = df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    df['cumulative_time'] = df['duration_hours'].cumsum()
    # Plot cumulative time spent in space over years
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()

plot_cumulative_time_in_space(eva_data, graph_file)

print("--END--")