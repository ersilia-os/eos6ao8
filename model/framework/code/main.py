import sys
import os
import csv

ROOT = os.path.dirname(os.path.abspath(__file__))
print(ROOT)
sys.path.append(os.path.join(ROOT, "molgrad"))

infile = sys.argv[1]
print(infile)
outfile = sys.argv[2]
print(outfile)
#checkpoints_dir = sys.argv[3]

from molgrad.net import MPNNPredictor
from molgrad.train import DEVICE
from rdkit import Chem

model_pt = os.path.abspath(os.path.join(ROOT, "..", "..","checkpoints", "ppb_noHs.pt")) 
#model_pt = os.path.join(checkpoints_dir, "ppb_noHs.pt")

from molgrad.prod import predict

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    mols = []
    for r in reader:
        print(r[0])
        mols += [Chem.MolToInchi(Chem.MolFromSmiles(r[0]))]

preds = predict(mols, model_pt, progress=True)[:,0]

with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["fraction_bound"])
    for p in preds:
        writer.writerow([float(p)])
