# Libraries
import numpy as np
from tools import csv_writer, get_config


# Main function
def generate():
    # Configuration programm
    conf = get_config()
    # Prepare file writer
    writer = csv_writer(conf['output_file'])

    for i in range(conf['N']):
        writer.send([
            i,
            np.random.randint(conf['M']),
            np.random.randint(conf['M']),
            np.random.randn(conf['N'])
        ])

    # Close writer coroutine
    writer.close()


if __name__ == "__main__":
    generate()
