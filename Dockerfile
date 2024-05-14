FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c dglteam dgl=0.4.3post2
RUN conda install -c dglteam dgllife=0.2.3
RUN conda install -c pytorch pytorch=1.9.0
RUN conda install -c conda-forge typing-extensions=4.7.1
RUN conda install -c conda-forge rdkit=2022.03.2

WORKDIR /repo
COPY ./repo
