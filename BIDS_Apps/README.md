# BIDS Applications

In 2016, a seminal article written by [Eklund, Nichols and Knutsson](https://www.pnas.org/content/pnas/113/28/7900.full.pdf) brought to light the reproducibility crisis in functional MRI studies and pointed out some important oversights, inaccuracies, and areas of improvement for many neuroimaging softwares.  While the paper originally inflated the number of studies affected, which was later corrected, it still emphasized the importance of having a consistent and rigorous preprocessing structure. As a beginner overview of some of the problems that can be seen in fMRI research, including findings from the Eklund et al. (2016) article (though not by name), see the video below.
[![](http://img.youtube.com/vi/8thDuVfqCCM/0.jpg)](http://www.youtube.com/watch?v=8thDuVfqCCM "")

As you all learned in the [heudiconv and BIDS tutorial](https://github.com/juliagoolia28/UD_repronim/blob/master/heudiconv_tutorial/README.md), Brain Imaging Data Structure (BIDS) specifies a reproducible and consistent directory structure for all your neuroimaging data.  This allows scientists from all over the world to have a uniform data structure for all their data, enabling greater reproducibility and availability of user-friendly data sharing.  For an introduction to this formatting, you should visit their [website](http://bids-apps.neuroimaging.io/). For a comprehensive overview on what BIDS formatting is and how it can be used, please see the video below.
[![](http://img.youtube.com/vi/K9hVAr5fvJg/0.jpg)](http://www.youtube.com/watch?v=K9hVAr5fvJg "")

Given the importance and usefulness of this data structure, many scientists collaborated together to create applications to preprocess, analyze, and/or visualize data that uses BIDS formatting. These applications are referred to as BIDS apps. For a comprehensive view of these BIDS apps, I would highly recommend you read the [Gorgolewski et al. (2017)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005209#abstract1) article on the creation of these applications.  This article introduces a data framework allowing for the creation and use of applications built towards analyzing various neuroimaging data that are in BIDS format.  You can also view their current list of [available BIDS apps](http://bids-apps.neuroimaging.io/apps/) and visit their [github page](https://github.com/BIDS-Apps).   

# FmriPrep

## What is FmriPrep?
Arguably one of the most frequently used BIDS apps is FmriPrep, which is an automated pipeline you can use to preprocess your data in a responsible, transparent, and reproducible fashion.  Personally, I cannot say enough good things about this incredibly useful resource.  Basically, it combines all the best functions from neuroimaging softwares such as Freesurfer, FSL, Afni and ANTS to provide you with the most scientifically rigorous and consistent manner to preprocess your data.  Plus, it allows you to select (or deselect) any specific functions in order to tailor this pipeline to your data, if need be.  It also provides a quality report including beautiful visualizations of each of the steps taken to preprocess your data so you can easily inspect your data.  This includes a before and after view of your data before preprocessing and after any corrections/preprocessing steps have been taken.  Finally, easily adapts to the use of longitudinal data, which can sometimes be complicated if using certain software packages alone.  To gain a comprehensive understanding of this program, I would recommend that you read their [article on FmriPrep](https://www.nature.com/articles/s41592-018-0235-4) and follow instructions in their [handbook](https://fmriprep.org/en/stable/) which includes everything you need to know about the pipeline.  Then, I would recomend you follow the steps outlined below. 

## How do I use FmriPrep?
Andrew Jahn (creator of [Andy's Brain Blog](https://www.andysbrainblog.com/about) and [Andy's Brain Book](https://andysbrainbook.readthedocs.io/en/latest/index.html)) has already created an incredibly useful tutorial for using fMRIPrep, from installation all the way to analyses.  Please see below for links and descriptions of these videos.  

### 1. Downloading Tutorial Data and Installing fMRIPrep
It's often best to learn by doing, therefore you can actually download a set of tutorial data and follow along with Andy's instructions.  This video introduces what fMRIPrep is, overviews how to obtain a [Freesurfer license](https://surfer.nmr.mgh.harvard.edu/registration.html) and install docker (overviewed in our [container tutorial](https://github.com/juliagoolia28/UD_repronim/tree/master/container_tutorial)) and fMRIPrep, and finally guides you to download a [Flanker task dataset](https://openneuro.org/datasets/ds000102/versions/00001).  You can view the corresponding tutorial from Andy's Brain Book [here](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_1_Download.html) and here (https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_2_RunningAnalysis.html).  If instead of using Docker you would prefer to use Singularity, please follow the instructions in either the [fMRIPrep handbook](https://fmriprep.org/en/stable/singularity.html) or [Andy's Brain Book](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep.html#fmriprep).
[![](http://img.youtube.com/vi/J0npRWV2zTY/0.jpg)](http://www.youtube.com/watch?v=J0npRWV2zTY "")

### 2. Running fMRIPrep
To facilitate the process of running fMRIPrep, Andy made a handy [script](https://github.com/andrewjahn/OpenScience_Scripts/blob/master/fmriprep_singleSubj.sh) you can edit and use on your own. The video below overviews what this script contains and how to run it. You can view the corresponding tutorial from Andy's Brain Book [here](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_2_RunningAnalysis.html). 
[![](http://img.youtube.com/vi/qCX4YlrdTAw/0.jpg)](http://www.youtube.com/watch?v=qCX4YlrdTAw "")

#### A few things to keep in mind about this tutorial
1. MRI data are huge, therefore running this script, even on a single subject, can take a while (depending on your HPC system, possibly anywhere from 1-2 hours).  
2. Since these data have been uploaded to open neuro and are already in BIDS format, you may notice that Andy uses the --skip-bids-validation flag.  If you are using your own data for the first time, you will need to make sure your data are in BIDS format.  There are many ways to do so.  For example, we have our [Heudiconv tutorial](https://github.com/juliagoolia28/UD_repronim/blob/master/heudiconv_tutorial/README.md), which shows you a concise way to convert your data to BIDS format. For a detailed tutorial on how to convert files without using Heudiconv, you can see [here](https://reproducibility.stanford.edu/bids-tutorial-series-part-1b/#auto4).  Through both methods, you should double-check that your data are properly formatted.  One way is to use the [BIDS validator](https://bids-standard.github.io/bids-validator/)), which checks your data to make sure they are in proper BIDS format.  Another way is to just run FMRIPrep without the --skip-bids-validation argument. 
3. You may also notice that another flag (--fs-no-reconall) has been used in order to skip a very lengthy process, Freesurfer's surface reconstruction.  If you do not use this flag, then Freesurfer will do a full reconstruction, which can make the whole process take anywhere from 6-24 hours to complete. 
4. If you are interested in gray matter measures, you will not want to use the --fs-no-reconall flag. 
5. If you are using longitudinal data, make sure you use the --longitudinal flag.  
6. You can always visit the fmriprep handbook to learn more about the [command-line arguments](https://fmriprep.org/en/stable/usage.html) and [pipeline details](https://fmriprep.org/en/stable/workflows.html).

### 3. Quality Assurance Checks
An important aspect of responsible science is checking your data.  FMRIPrep makes this process easy by providing quality checks for all your preprocessing steps.  This video overviews the output structure of fMRIPrep and how to view the HTML quality check file. You can view the corresponding brain book [here](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_3_ExaminingPreprocData.html).  For detailed instructions on how to manually inspect your structural MRI data, please see the following [tutorial](https://github.com/juliagoolia28/UD_repronim/tree/master/Freesurfer_Manual_Inspection) in our series.  
[![](http://img.youtube.com/vi/fQHEKSzFKDc/0.jpg)](http://www.youtube.com/watch?v=fQHEKSzFKDc "")

### 4. Optional Additional Preprocessing: Smoothing and Scaling
While some researchers are used to smoothing and scaling their data, FMRIPrep does not automatically run these steps, since they are more of an individual / judgement call.  If you would like to run these additional steps, you can watch the video below.  The corresponding brain book chapter is [here](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_4_AdditionalPreproc.html).   
https://www.youtube.com/watch?v=lA9ZUefF3Po&list=PLIQIswOrUH6_szyxn9Fy-2cxd3vjlklde&index=4

### 5. 1st-Level Analysis
This video overviews how to do a general linear model analysis on a single participant and visualize these results using AFNI viewer.  This step must be completed before you run the group analysis.  The corresponding brain book chapter can be found [here](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_5_1stLevelAnalysis.html).
[![](http://img.youtube.com/vi/OESt1--zuq4/0.jpg)](http://www.youtube.com/watch?v=OESt1--zuq4 "")

### 6. Group Analysis
This video overviews how to automate the 1st-level analysis across all your participants using a for loop (this is a long process -- can take days) and how to run a group analysis.  The corresponding brain book chapter is [here](https://andysbrainbook.readthedocs.io/en/latest/OpenScience/OS/fMRIPrep_Demo_6_GroupAnalysis.html).
[![](http://img.youtube.com/vi/JBf7HFQZ6gw/0.jpg)](http://www.youtube.com/watch?v=JBf7HFQZ6gw "")

There you go! You have successfully learned all the steps to use fMRIPrep to preprocess data and do some first- and second- level analyses!






