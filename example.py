import argparse
import json
from pathlib import Path
import matplotlib.pyplot as plt

from utils import load_image, draw_annotation

parser = argparse.ArgumentParser()
parser.add_argument('--root', help='path to the folder with data', default='~/CT_LUNGCANCER_500')
args = parser.parse_args()

with open(Path(__file__).parent / 'annotation/RLAD42D007-22975_RLS6A01002SVR_2418297.json') as file:
    annotation = json.load(file)

# we'll assume the dataset is in the home folder
#  change the path if needed
image = load_image(Path(args.root).expanduser(), annotation)
draw_annotation(image, annotation)
plt.savefig('RLAD42D007-22975_RLS6A01002SVR_2418297.png')
