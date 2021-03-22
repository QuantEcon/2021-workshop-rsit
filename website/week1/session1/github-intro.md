(session1/github)=
# GitHub

```{admonition} Aims / Outcomes / Expectations:
1. Provide an overview of `GitHub` and `git`
2. Demo: `GitHub` and features recommended for this workshop
3. Provide resources for interested participants
```

## What is GitHub?

:::{margin}
The competitors are mainly:
1. [Gitlab](https://about.gitlab.com)
1. [Atlassian BitBucket](https://bitbucket.org)
:::

It is a website that hosts Git projects and adds an interface for:

1. tracking issues,
2. reduce complexity of code reviews, and
3. simplifies collaboration on projects
4. enables web integrations (i.e. automated workflows)

:::{margin}
`GitHub` is ideally suited to software projects, but it is general enough to be used for any
projects (with a particular emphasis on text based files).
:::

GitHub consists of `users` (individuals) and `organisations` for
grouping projects in an organisation setting such as [QuantEcon](https://github.com/QuantEcon)

Here are the [2020 year in review statistics](https://octoverse.github.com)

There is a useful [training guide](https://lab.github.com/githubtraining/introduction-to-github) that is
put together by the `GitHub` team. 

Another access option is to use [Github Desktop](https://desktop.github.com/) but I find the website to be
my preferred access option coupled with `terminal based workflows with git`.

```{tip}
If you are solely interested in LaTeX projects there are other services available that offer 
collaboration features such as [overleaf](https://www.overleaf.com) but requires a paid account.
```


## What is Git?

**Git** is a `distributed version control` system that sits on top of
your file system that tracks the state of a collection of files.

Its major strength is text type data (manuscripts, code etc.) but can keep track
of other file types also.

It can help you determine exactly what has changed, why it has changed, and
who has changed it.


### Key Concepts of Git

1. Working Directory
2. Staging Area
3. Local Repository (Repo)
4. Remote Repository (Repo)

as `git` is `distributed` the local and remote
repositories have access to the same history information.

### Git Workflow

```{margin}
Image courtesy of this [tutorial](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/)
```

```{figure} img/git-basic-2.png
```

A **file** in a Working Directory can have one of the following three states

1. **Modified** changes detected
2. **Staged** changes are marked to be committed
3. **Commited** changes stored in local repository

:::{note}
You can find the status of files using:
```bash
git status
```
:::

### Setting up Git

When using Git for the first time it can be a good idea to setup
Git with the correct user information.

Open a terminal (or Git Bash (Windows)):

```bash
$ git config --global user.name "Your name here"
$ git config --global user.email "your_email@example.com"
```

:::{note}
You can check the configuration using:
```bash
git config --list
```
:::

## Setting up a Repository (GitHub)

Go to GitHub (in browser) and click on **New**

```{figure} img/github-new-repo.png
```

### New Repository

To setup a new repository

:::{margin}
```{tip}
Click on `Clone` and copy the url such as: `https://github.com/<username>/test.git`
to your clipboard to use when cloning.
```
:::

```{figure} img/github-repo.png
```

### Cloning your Repository

To get a copy of the repository on your local machine

Open a `terminal`:

```bash
cd <working-directory>
git clone https://github.com/<username>/<repo-name>.git
```

```{figure} img/terminal-git-clone.png
```


### Fetching the latest from GitHub

If you **already** have a local copy of the repository on your local computer
then you should always fetch the latest changes before starting your work.

Open a **terminal**:

```bash
git pull
```

this is particularly the case in collaborative environments.

### Adding a Change

Navigate to the repository via `terminal`

Create a file such as `first.txt` and use:

```bash
git status
```

to check on `git` state

```{figure} img/terminal-git-status.png
```

### Committing a Change (Local)

We will want to move the file `first.txt` into the staging area
in preparation for committing.

In `Terminal`:

```bash
git add first.txt
```

```{figure} img/terminal-git-add.png
```

Once we have added the files we want to commit them to history

In `Terminal`:

```bash
git commit -m "initial commit"
```

```{figure} img/terminal-git-commit.png
```

### Pushing a Change (GitHub)

To get those changes on your remote GitHub copy of the repository
we need to push them to GitHub:

In `Terminal`:

:::{margin}
```{note}
On collaborative projects you rarely push to **master**
```
:::

```bash
git push origin master
```

```{figure} img/terminal-git-push.png
```

### Viewing results on GitHub

```{figure} img/github-updated-repo.png
```

## (Optional) Git - Advanced

Git has a **lot** of features:

1. [Forking](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
2. [Branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
3. [Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
4. [Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
5. [Stashing](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
6. ...

we will run through **branching**

### Branching

A **branch** is like a parallel copy of the **master**/**main** branch.

```{figure} img/git-branch.png
```

It allows changes to occur in parallel.

The **master**/**main** branch does not get modified until the branch is merged
into the main** branch.

Using GitHub this is called a `pull request`.

**Setting up a Branch:**

Let's setup a branch

```bash
git checkout -b first-branch
```

```{figure} img/terminal-git-checkout.png
```

and then add a file `second.txt` and/or modify `first.txt`


**Adding a Change:**

We now want to follow the same **commit** workflow as before

```bash
git add second.txt
git commit -m "adding a second file"
```

```{figure} img/terminal-git-add-commit-branch.png
```

**Pushing the Change:**

Pushing this branch to GitHub's copy of the **test** repo

:::{margin}
```{note}
The `origin` is automatically configured to GitHub when you cloned the repository from GitHub
```
:::

```bash
git push origin first-branch
```

```{figure} img/terminal-git-push-branch-github.png
```

**Setup a PR on GitHub:**

Look for:

```{figure} img/github-recent-push-notification.png
```

then setup a `PR` by clicking on `Compare and pull request`

```{figure} img/github-pull-request.png
```

## Suggested Workflows

### Key GIT Commands

The vast majority of interactions with **git** is focused on these commands

1. `git status`
1. `git pull`
1. `git checkout -b <branch-name>`
1. `git add`
1. `git commit -m "message"`
1. `git push`


### A Common Terminal Workflow

1. `git pull` : retrieve new updates
2. `git status` : show status of commit
3. General work and edits
4. `git status` : show status of commit
5. `git add .` : puts **all** changed files into **staging area**
6. `git commit -m "some message"` : commit changes to local git repository with a description
7. `git push` : pushes the new version to Github



## Further Reading / Resources

## Git Resources

Understanding **Git**:

1. [Github Tutorials](https://try.github.io/)
2. [Git Book](https://git-scm.com/book/en/v2)
3. [Blog: Beginners](https://juristr.com/blog/2013/04/git-explained)
4. [Blog: Git Guide](https://itnext.io/become-a-git-pro-in-just-one-blog-a-thorough-guide-to-git-architecture-and-command-line-interface-93fbe9bdb395)
5. [Blog: Git Quickstart](https://www.freecodecamp.org/news/learn-the-basics-of-git-in-under-10-minutes-da548267cc91/)
6. [Blog: Useful Git Commands](https://towardsdatascience.com/10-git-commands-you-should-know-df54bea1595c)


## GUI Options (OS X and Windows):

Some like to start by using a GUI

1. [Git Fork](https://git-fork.com/)
1. [Git Kraken](https://www.gitkraken.com/)

I typically recommend `terminal based workflows`


## Exercise

```{exercise} Exercise 1: Clone Workshop Repository
Clone the workshop repository:
```bash
git clone https://github.com/QuantEcon/2021-workshop-rsit.git
```
```