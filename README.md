# Coloring molecules for plasma protein binding prediction

By combining a Message-Passing Graph Neural Network (MPGNN) and a Forward fully connected Neural Network (FNN) with an integrated gradients explainable artificial intelligence (XAI) method, the authors developed MolGrad and tested it on a number of ADME predictive tasks. MolGrad incorporates explainable features to facilitate interpretation of the predictions. In this model, they train MolGrad with data from a Plasma-protein binding assay (PPB) to predict the fraction bound in plasma of small molecules.

This model was incorporated on 2021-10-19.

## Information
### Identifiers
- **Ersilia Identifier:** `eos6ao8`
- **Slug:** `molgrad-ppb`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `ADME`, `Fraction bound`, `Chemical graph model`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Fraction (%) bound in plasma

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| fraction_bound | float | high | Fraction bound to plasma protein |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6ao8](https://hub.docker.com/r/ersiliaos/eos6ao8)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6ao8.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6ao8.zip)

### Resource Consumption
- **Model Size (Mb):** `15`
- **Environment Size (Mb):** `2418`
- **Image Size (Mb):** `2379.4`

**Computational Performance (seconds):**
- 10 inputs: `33.49`
- 100 inputs: `28.82`
- 10000 inputs: `783.4`

### References
- **Source Code**: [https://github.com/josejimenezluna/molgrad/](https://github.com/josejimenezluna/molgrad/)
- **Publication**: [https://pubs.acs.org/doi/10.1021/acs.jcim.0c01344](https://pubs.acs.org/doi/10.1021/acs.jcim.0c01344)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [AGPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos6ao8
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos6ao8
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
