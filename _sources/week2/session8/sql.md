(session8/sql)=
# SQL

These notebooks introduce the ideas of a relational database using grocery order data.

The dataset was released as part of a Kaggle competition. Instacart described the dataset by saying,

> The dataset for this competition is a relational set of files describing customers' orders over time. The goal of the competition is to predict which products will be in a user's next order. The dataset is anonymized and contains a sample of over 3 million grocery orders from more than 200,000 Instacart users. For each user, we provide between 4 and 100 of their orders, with the sequence of products purchased in each order. We also provide the week and hour of day the order was placed, and a relative measure of time between orders. For more information, see the blog post accompanying its [public release](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2).

### Data Description

We begin by working through a notebook that describes the dataset and computes a few objects of interest. 

You can download the {download}`notebook from here <../../../notebooks/session8/data_description.ipynb>` or [launch the notebook](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession8%2Fdata_description.ipynb)

If you download it locally, you can launch it via

```bash
cd ~/Downloads
jupyter notebook data_description.ipynb
```

### SQL

After introducing the dataset, we learn some of the basics behind operating SQL and then use SQL to replicate some of the analysis done in the data description notebook.

You can download the {download}`notebook from here <../../../notebooks/session8/sql.ipynb>` or [launch the notebook](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession8%2Fsql.ipynb)

If you download it locally, you can launch it via

```bash
cd ~/Downloads
jupyter notebook sql.ipynb
```
