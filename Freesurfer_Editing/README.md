# Overview
Being able to be confident in your data and being able to deciden when to and how to make freesurfer edits is not something that can be learned in an hour or two.  There is no single tutorial video that could cover all of this without being extremely long.  Therefore, I am providing you all with the very best resources that I have personally used that have helped me with making Freesurfer edits to my own data.  

# Freeview Tutorial
Before you made any actual edits to FS data, you should understand how to navigate Freeview.  If you have not watched this video (also listed in the manual inspection tutorial), please do so now since it overviews how to use Freeview, one of Freesurfer's main visualization and editing tools.  To follow along, you can also access the Freeview instructions [here.](https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/OutputData_freeview) 

[![](http://img.youtube.com/vi/Mv-ECowxq2o/0.jpg)](http://www.youtube.com/watch?v=Mv-ECowxq2o "")

# Knowing when and how to make edits
In order to decide when to make edits, along with how to make these edits, you should follow the directions in the Freesurfer Course video below.  I highly recommend you all watch this video since it goes over the thought process and decision making process in an expert manner, and this is usually the toughest part of editing your data.  To follow along with some of the troubleshooting elements of this tutorial, please visit [here.](https://surfer.nmr.mgh.harvard.edu/fswiki/FsTutorial/TroubleshootingData)

[![](http://img.youtube.com/vi/AR83_Bt04VQ/0.jpg)](http://www.youtube.com/watch?v=AR83_Bt04VQ "")

## Important points from this video
1. First things first.  If you are going to make any edits to your data, then you should rename and save the original files (e.g. wm.mgz and brainmask.mgz can be changed to wm_orig.mgz and brainmask_orig.mgz, respectively). 
2. If you are uncertain about whether you need to make a change, remember that Freesurfer includes a sample subject "Bert".  You can look at this person's brain and reconstruction as a comparison.  
3. Changes to gray matter (like when the pial surface includes too many voxels that should not count as gray matter) will apply to the brainmask.mgz file.  Changes to white matter (like when not enough voxels are included in the pial surface or when there's too much or too little white matter included) will apply to the wm.mgz file or you will need to add control points.
4. When using Recon Edits, to erase voxels, click Shift + Left click.  To add voxels, just left click.  To undo an action, press command or ctrl + Z.  The instructions are always at the bottom of the recon edits box if you forget. 

# Brief summary videos
Andrew Jahn is an awesome neuroscientist who provides a lot of valuable and short tutorials.  To overview some of the key steps on the video provided above, I suggest you view these short summary videos.  I am also linking his corresponding brain book.

## Types of Freesurfer errors
Here is an overview of types of hard and soft errors Freesurfer can make.  For the purposes of this tutorial, I'd recommend you focus on the soft errors, which will be overviewed next.  For the corresponding brain book page, please see [here.](https://andysbrainbook.readthedocs.io/en/latest/FreeSurfer/FS_ShortCourse/FS_12_FailureModes.html)

[![](http://img.youtube.com/vi/8n5_XE-OH0E/0.jpg)](http://www.youtube.com/watch?v=8n5_XE-OH0E "")

## Gray Matter Edits: Skull stripping and pial surface edits
The section overviewing skull stripping is especially useful since the Freesurfer Course video in the "Knowing when and how to make edits" portion of this document did not have time to overview this process.    For the corresponding brain book page, please see [here.](https://andysbrainbook.readthedocs.io/en/latest/FreeSurfer/FS_ShortCourse/FS_13_PialSurface.html)

[![](http://img.youtube.com/vi/WaPtktm2EX4/0.jpg)](http://www.youtube.com/watch?v=WaPtktm2EX4 "")

In order to understand proper rationale for the pial surface edits, I highly recommend you skip to the portion in the Freesurfer Course video that goes over this (around the 2:45 minute mark) if you have not watched it already. 

## White Matter Edits: Control points and white matter normalization
This video goes over how to make control point edits and white matter normalization.  For the corresponding brain book page, please see [here.](https://andysbrainbook.readthedocs.io/en/latest/FreeSurfer/FS_ShortCourse/FS_14_ControlPoints.html)

[![](http://img.youtube.com/vi/TY2G8cHHzRE/0.jpg)](http://www.youtube.com/watch?v=TY2G8cHHzRE "")

Again, in order to understand the proper rationale for when to make edits to the wm.mgz file (edits to segmentation) which are more forgiving edits versus control points (intensity normalization) which lead to much more substantial editing and should not be over-used, you should definitely watch the Freesurfer Course video above (around the 25-27 minute mark) if you have not watched it already.  

# Save your data and re-run the Freesurfer reconstruction
In order to save edits you've made in freesurfer to the wm.mgz or the brainmask.mgz file, make sure you select which of these volumes you want to save and then go to the main Freeview menu and click on the "Save Volume" option.  Importantly, you must save these files as their original names otherwise when you run the reconstruction again, it will not grab these files.  In order to save control point edits, you should go to the main Freeview menu and click on the "Save Set Points" option.
![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/FS_save_volume.png)

You do not need to re-run the freesurfer reconstruction after every single change.  Instead, make and save all the changes to the files that are necessary (if applicable), and then run the recon-all steps starting at the earliest point at which you made an edit.  For example, if you edited the brainmask.mgz by running a skull strip or gcuts, then you would run the following command: ```recon-all autorecon2```

![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/FS_preprocessing_stream_overview.png)

# Implementing proper documentation
This can be quite an involved process, and the last thing you want to do is edit a lot of files and then six months later have zero recollection of which files you edited, and how you edited them.  An important part of conducting responsible and reproducible science is documenting your work.  Therefore, I recommend that you use the spreadsheet provided in the Freesurfer_manual_inspection_of_sMRI_data portion of this tutorial and add in any edits you've made.  I would also recommend that you include the pre-edits qoala-t scores and then re-run the quoala-t scores after your reconstruction and document this on the spreadsheet to see changes in your score before and after your edits. 

# Key takeaways

1. In order to help you decide whether or not to edit a slice, make sure you view the same problem in three consecutive slices
2. When in doubt, do not make edits. Either ask for help from a more seasoned professional, or err on the side of caution and do not make edits if they are very minor.  This will prevent you from making too many changes to the reconstruction and will also save you time.
3. Save. Your. Data. Often.  This cannot be stressed enough since sometimes Freeview will crash and you do not want all your hard work to go down the drain.
4. Make sure you re-run the reconstruction if you want your changes to be implemented.

