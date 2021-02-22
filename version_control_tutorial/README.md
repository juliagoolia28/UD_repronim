# Version Control
[Much of the following information was pulled from The Github Handbook](https://guides.github.com/introduction/git-handbook/)

[Tutorial Intro Video](https://www.youtube.com/watch?v=3RjQznt-8kE)

A version control system, or VCS, tracks the history of changes as people and teams collaborate on projects together. As the project evolves, teams can run tests, fix bugs, and contribute new code with the confidence that any version can be recovered at any time. Developers can review project history to find out:

Which changes were made?
Who made the changes?
When were the changes made?
Why were changes needed?

**Git** is commonly used for version control (more than 70% of developers use it!). Git allows developers to all collaborate in one place and see the entire timeline of their project, including changes, decisions, and the overall progression. No more "_final", "_final_1", "_final_for_real"...etc.

### There is a little bit of a learning curve, but once you learn some **basic Git commands**, you really have most of it down:

```git init``` initializes a brand new Git repository and begins tracking an existing directory. It adds a hidden subfolder within the existing directory that houses the internal data structure required for version control.

```git clone``` creates a local copy of a project that already exists remotely. The clone includes all the project’s files, history, and branches.

```git add``` stages a change. Git tracks changes to a developer’s codebase, but it’s necessary to stage and take a snapshot of the changes to include them in the project’s history. This command performs staging, the first part of that two-step process. Any changes that are staged will become a part of the next snapshot and a part of the project’s history. Staging and committing separately gives developers complete control over the history of their project without changing how they code and work.

```git commit``` saves the snapshot to the project history and completes the change-tracking process. In short, a commit functions like taking a photo. Anything that’s been staged with git add will become a part of the snapshot with git commit.

```git status``` shows the status of changes as untracked, modified, or staged.

```git branch``` shows the branches being worked on locally.

```git merge``` merges lines of development together. This command is typically used to combine changes made on two distinct branches. For example, a developer would merge when they want to combine changes from a feature branch into the main branch for deployment.

```git pull``` updates the local line of development with updates from its remote counterpart. Developers use this command if a teammate has made commits to a branch on a remote, and they would like to reflect those changes in their local environment.

```git push``` updates the remote repository with any commits made locally to a branch.

### So now that you have all of these commands, how do you USE them? 

The GitHub flow has six steps, each with distinct benefits when implemented:

**Create a branch:** Topic branches created from the canonical deployment branch (usually main) allow teams to contribute to many parallel efforts. Short-lived topic branches, in particular, keep teams focused and results in quick ships.

**Add commits:** Snapshots of development efforts within a branch create safe, revertible points in the project’s history.

**Open a pull request:** Pull requests publicize a project’s ongoing efforts and set the tone for a transparent development process.

**Discuss and review code:** Teams participate in code reviews by commenting, testing, and reviewing open pull requests. Code review is at the core of an open and participatory culture.

**Merge:** Upon clicking merge, GitHub automatically performs the equivalent of a local ‘git merge’ operation. GitHub also keeps the entire branch development history on the merged pull request.

**Deploy:** Teams can choose the best release cycles or incorporate continuous integration tools and operate with the assurance that code on the deployment branch has gone through a robust workflow.

This [interactive guide is amazing](https://guides.github.com/introduction/flow/)

## Resources:

[Examples utilized in the current tutorial](https://brainhack-princeton.github.io/handbook/content_pages/pygers_workshops/fall_2020/workshop_notes_week2.html)

[OHBM Presentation about Git and Github](https://www.youtube.com/watch?v=MNgvv5oOrDc)

[Software Carpentry Tutorial](http://swcarpentry.github.io/git-novice/)

