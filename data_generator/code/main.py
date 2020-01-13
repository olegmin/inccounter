# Libraries
import numpy as np
from tools import csv_writer, get_config


# Main function
def generate():
    # Configuration programm
    conf = get_config()
    # Prepare file writer
    writer = csv_writer(conf['output_file'])
    # Print output file
    print(f"Write data in file: {conf['output_file']}")
    # Generate data
    counter = 0
    for i in range(conf['N']):
        # Write to file new line with data
        writer.send([
            i,
            np.random.randint(conf['M']),
            np.random.randint(conf['M']),
            np.random.uniform(0.01, 1.0)
        ])
        # Count itterations and print status
        counter += 1
        if counter % 1000 == 0:
            print(f"\twrite {counter} / {conf['N']} lines.")
    # Close writer coroutine
    writer.close()


if __name__ == "__main__":
    generate()
