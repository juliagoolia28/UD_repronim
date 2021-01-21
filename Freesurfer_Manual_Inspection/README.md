# Inspecting MRI data before running Freesurfer edits

You should always inspect the MRI data to decide whether you should edit your brain structure scan data and choose which edits to run.  The purpose of this page is to guide you through the process of decision making and documentation before and while you do the actual Freesurfer edits such as skullstripping, gray matter and white matter edits, and control point editing. 

## Which data should undergo manual inspection? 

Let's look at the Qoala-T table output that can be derived by following the steps in the first part of Lesson 4.

![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/qoala-t_table_original.png)

All your data should be visually inspected, even if Qoala-T does not recommend changes.

## Qoala-T criterion
When inspecting data, you should consider the following questions to help you decide which edits to make (if any):
1. Is the reconstructed image affected by movement?
2. Is (part of) the temporal pole missing in the reconstruction?
3. Is non-brain tissue (e.g. dura/skull) included in the reconstruction of pial surface (red line)?
4. Are parts of the cortex missing in the reconstruction (other than temporal poles)?

## Documentation of Errors and Edits
You should document any errors you see in the MRI data along with your Freesurfer edit changes using our [Qoala-T QC template spreadsheet](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Qoala-T_QC_spreadsheet.xlsx).  

For each participant, if there is an error in movement, missing or extra gray or white matter, you should put a 1 and highlight this in red in the respective column demarcating the error.  If not, then mark it with a zero so we know this was still inspected. **You should only mark errors that are seen across 3 consecutive slices of the brain.**

You should document any anomalies seen in each of the lobes of the brain, separately for the right and left hemispheres of the brain (see picture below).

![](https://upload.wikimedia.org/wikipedia/commons/2/2c/Diagram_showing_the_lobes_of_the_brain_CRUK_308.svg)

See below for an example of how you should fill out the spreadsheet.

![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/QC_spreadsheet_example.png)

### Watch Freeview Tutorial video
[![](http://img.youtube.com/vi/Mv-ECowxq2o/0.jpg)](http://www.youtube.com/watch?v=Mv-ECowxq2o "Freeview_tutorial")

### Open Freeview GUI 
Freeview is a Freesurfer-based visualization toolkit. You can open this by simply typing Freeview into your command line once you have Freesurfer installed.  For more details about this software, please see [here](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeviewGuide/FreeviewGeneralUsage/FreeviewQuickStart). You should load the following files:

1. First load the following Volumes: wm, brainmask, and T1.  Make sure the brainmask is selected for viewing.
2. Then load your Surfaces: rh.pial, rh.white, lh.pial, and lh.white.  Make sure one of the pial surfaces is selected for viewing.

### Check for movement
If it looks like there are “rings” around the brain, there is likely a significant amount of movement.  Check to see if this is seen across 3 consecutive slices of the brain or more.  Below is a picture of a participant with significant movement.  Therefore, we would write a 1 in the "excessive movement" column of the Qoala-T QC template spreadsheet.

![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/check_movement.png)

### Check the Temporal lobe
One of the most common errors we will see in sMRI data is that there will be sections of the temporal pole missing. You should mark the spreadsheet if there is a whole section of the temporal lobe not included in the red outline in 3 consecutive slices. 

In the image below, you would mark 1 only for the left hemisphere which is missing significant portions of the temporal lobe.

![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/check_temporal_pole_error.png)


### Check Dura
The brain is covered by 3 meninges, the thickest and most outer covering is called the dura mater. Sometimes, Freesurfer will accidentally include the dura mater as part of the brain, which is not accurate.  Therefore, we need to mark whether or not this occurred. 

Dura usually appears as as bright white layer right next to the skull. In the picture below, you would mark 1 only for the left hemisphere which includes dura and the skull as part of the brain.

![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/check_dura.png)


### Check other lobes of the brain

Just like you did for the temporal lobe, you now should go through the rest of the brain and mark whether there are missing parts to the frontal, parietal, and occipital lobes.

Below we can see there are significant missing parts to the frontal lobe on both sides of the brain, so we would mark 1 for both hemispheres of the brain.

![](https://github.com/jlegault/Materials_for_Inspection_of_sMRI_data/blob/master/Images_for_wiki_page/check_frontal_lobe.png)


You are now ready to start making the Freesurfer edits!
