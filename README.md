# UD_repronim

"[ReproNim's](https://www.repronim.org/) goal is to improve the reproducibility of neuroimaging science and extend the value of our national investment in neuroimaging research, while making the process easier and more efficient for investigators."

Towards this goal, the [ReproNim Fellowship Program](https://www.repronim.org/fellowship.html) supports individual syllabus development and implementation of reproducibility training at appointed fellows' home institutions. 

The current workshop series, UD ReproNim, is a product of this ReproNim Fellowship Program, and as such, draws heavily from existing open-source materials in the neuroimaging community to foster growth and knowledge of existing, reproducible computational technologies, pipelines/workflows, data wrangling approaches and statistical toolboxes. 

The Fellows who organized this workshop, Drs. Jennifer Legault and [Julie Schneider](https://sites.udel.edu/jmschneider/), thank those who have come before them to establish and share the resources included in the current repo. 

## Resources
[The missing semester](https://missing.csail.mit.edu/)

[ReproNim Training Modules](https://www.repronim.org/teach.html)

## Requirements

This workshop will rely heavily on the use of Terminal -- therefore, working knowledge of how to use a Shell is necessary. You don't need to be a professional, but being able to cd in and out of directories with confidence will benefit you greatly! To help you get started, we have provided some resources for [Bash/Shell scripting](https://github.com/juliagoolia28/UD_repronim/tree/master/bash_unix_resources).

You will also need to have some things installed prior to our first workshop:
- [pip](https://pip.pypa.io/en/stable/reference/pip_install/)

If you are using lab data, working on a lab server, or setting up these pipelines for your lab computers:
- Be able to [VPN](https://udeploy.udel.edu/software/anyconnect-vpn/) onto the UD network
- Need to have setup [Google Authentication](https://services.udel.edu/TDClient/32/Portal/KB/ArticleDet?ID=4) to VPN/Remotely connect to lab computers

## Course Description

Creating reproducible science is an essential part of being a scientist.  In this workshop, we will introduce the importance and implementation of reproducibility, version control, and teach about using reproducible methods such as automated pipelines and data organization structures.  Specifically, we will overview functional MRI, demonstrating how labs can make data BIDS compatible and the benefits of pre-processing data using fMRIprep. We will then go over structural MRI data selection/examination and editing using Qoala-T and Freesurfer editing for child data.  MRI data selection and editing is important especially in children since 1) children tend to move a lot (more scanner artifacts) and 2) children’s brains are more difficult to model due to high variation between children

## Tentative Schedule

This schedule and its contents are subject to change.

| Week     | Content                                                               |
| -------- | --------------------------------------------------------------------- |
| Feb 8    | The Fear Factor: Why Reproducibility Matters & Reproducibility basics |
| Feb 15   | Docker / Containers                                                   |
| Feb 22   | Version control                                                       |
| March 1  | Heudiconv + BIDS Formatting                                           |
| March 8  | BIDS Formatting/Intro fMRIprep                                        |
| March 15 | fMRIprep continued                                                    |
| March 22 | Freesurfer Introduction to sMRI outputs and using Qoala-T             |
| March 29 | Spring Break                                                          |
| April 5  | Freesurfer : Check and edit your sMRI data                            |
| April 12 | Higher-Level Options                                                  |
| April 19 | fMRIprep pre-processing + versatility                                 |


