(session8/workflow-tools)=
# Workflow Tools

Two great tools that I use in my own workflows are:

* `kedro`: https://github.com/quantumblacklabs/kedro
* `prefect`: https://github.com/PrefectHQ/prefect


## `kedro`

`kedro` is a package that helps manage data pipelines from transforming data from raw data to clean data and to analysis.

It helps ensure that the steps used to arrive at an analysis are replicable and provides some convenience funtions that allow us to access and update the data easily


## `prefect`

`prefect` is a DAG management tool. It allows you to define particular operations and specify a schedule on which you'd like those operations executed.

There are other tools that do this, `cron` for example... So why `prefect`? `prefect` is built on the idea of "negative engineering" -- `cron` is a perfectly acceptable solution to schedule tasks when everything works, but what happens when things break? `prefect` is built on the premise that your pipeline is likely to break for any variety of reasons - It keeps detailed logs of what broke when and presents a relatively clean GUI interface for task management.


## Things should run on the cloud

It might seem convenient to run tasks or host a postgres server locally, but it's not a particularly good idea to do that... It requires that you have someone competent enough not to accidentally expose security risks (which I wouldn't trust myself not to do...) and maintain your computer/network. The cloud is "someone else's" problem -- If the network goes down (which, at the level of maturity we've reached in the cloud tooling, is a rare event for cloud based services), then you complain about it and someone else fixes it.

All of the cloud providers deliver similar quality services... I personally like Google Cloud, but, if it saved money, then I would gladly switch to an alternative.


## Example workflow

1. Github repository that contains scrapers and code.
2. DAGs uploaded to a cloud instance running `prefect`.
3. As DAGs run, ensure that data is saved at every step! This is important because if anything ever broke on the database side, we would be able to reconstruct the data at any snapshot in time.
4. Use `kedro` and other tools to interface with the storage bucket or postgrest database and help manage analysis steps
