from tools import get_config, timer
import pandas as pd


@timer
def count_incedents():
    # Getting configuration of programm
    conf = get_config()
    # Reading all data
    all_data = pd.read_csv(conf['input_file'], sep=';', index_col='id')
    # Calculate incedents
    dt = conf['delta_time']
    ci = []
    for index, row in all_data.iterrows():
        # Fields of curent incedents
        f1 = int(row['feature1'])
        f2 = int(row['feature2'])
        t = row['time']
        # Search valid incedents
        valid_incedents = all_data.query("feature1 == @f1 & feature2 == @f2 & @t-time>0 & @t-time<=@dt")
        # Count incedents
        if valid_incedents.empty:
            lenght = 0
        else:
            lenght, _ = valid_incedents.shape
        # Append number of incedents
        ci.append([lenght])
    # Create DataFrame with counts
    cincd = pd.DataFrame(ci, columns=['counts'])
    # Save counted incedents to output file
    cincd.to_csv(conf['output_file'], index_label='id')


if __name__ == "__main__":
    count_incedents()
