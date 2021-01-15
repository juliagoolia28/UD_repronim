# Heudiconv Tutorial

## Resources:
[The main documentation for the Heudiconv Tutorial](https://neuroimaging-core-docs.readthedocs.io/en/latest/pages/heudiconv.html)

[James Kent created a fantastic step-by-step video that the current tutorial was adapted from](https://www.youtube.com/watch?v=O1kZAuR7E00)

[Why use BIDS/What is BIDS? An inspiring talk by Sam Nastase](https://docs.google.com/presentation/d/11MeS72TRLTiEwX4EbjWj84IFCTAmMJIawZF3VCLWLjA/edit#slide=id.g89c2127f6e_0_478)

## Requirements:
[Docker](https://www.docker.com/)

## Creating a Heuristic File
### You will repeat the below steps once. This will allow you to create a heuristics file that you will use for all participants moving forward.
**A little background:** Your MRI scan produces study specific information that you need to create a "cheat sheet" for. We call this "cheat sheet" a heuristics file. Basically, you will run a dry pass heudiconv on one subject to get this information. Then, you pull numbers from them to create your heuristic of the number of sessions, runs, localizers, T1s, etc. that your subject has. 

1. ```docker pull nipy/heudiconv```
2. Edit create_heuristic.sh file
    - Line 2: change path where DICOM data is located
    - Line 3: change path where BIDS data will be output
   - Lines 5-7: define a single subject, and subsequent folder organization (ses = session)
3. Execute create_heuristic.sh script (works best by copying and pasting command)
4. Check output within BIDS folder ```ls -a```
    - Make sure you are within your BIDS directory
    - You should see a .heudiconv file
5. Create a subdirectory under the output directory and call it code: ```mkdir code```
6. Add the convertall.py script (stored in this folder) to this folder
7. CD into .heudiconv/{subject}/info and open the dicominfo.tsv file.
8. Edit your convertall.py script using this dicominfo.tsv file as a guide.

## Now you are ready to convert dicoms to BIDS formatted nifti files
### You will repeat the below steps for every new participant

-  In terminal complete the following steps:
```
cd /PATH/TO/DICOM/SUBJECT/FOLDERS/
docker run --rm -it --entrypoint=bash -v $(pwd):/data nipy/heudiconv:latest
cd /data/
```
-  You should now be within the container and can run the conversion. 
**SUBJECTID in all caps should be edited. Additionally, the folder structure might differ across study designs. **
```
heudiconv -d /data/dicoms/{subject}/*/*/*.IMA -s SUBJECTID -f /data/HEURISTICS_FILENAME.py -c dcm2niix -b -o /data/bids
```
