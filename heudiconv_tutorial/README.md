# Heudiconv Tutorial

## Resources:
[The main documentation for the Heudiconv Tutorial](https://neuroimaging-core-docs.readthedocs.io/en/latest/pages/heudiconv.html)

## Resources and Recording from Workshop
[Recording from Workshop: Part 1](https://drive.google.com/drive/folders/1zz4GXVpY8OgJxFDIf6QxUmOJNgNsY2l1?usp=sharing)

[James Kent created a fantastic step-by-step video that the current tutorial was adapted from](https://www.youtube.com/watch?v=O1kZAuR7E00)

[Why use BIDS/What is BIDS? An inspiring talk by Sam Nastase](https://docs.google.com/presentation/d/11MeS72TRLTiEwX4EbjWj84IFCTAmMJIawZF3VCLWLjA/edit#slide=id.g89c2127f6e_0_478)

## Requirements:
[Docker](https://www.docker.com/)

## Creating a Heuristic File
### You will repeat the below steps once. This will allow you to create a heuristics file that you will use for all participants moving forward.
**A little background:** Your MRI scan produces study specific information that you need to create a "cheat sheet" for. We call this "cheat sheet" a heuristics file. Basically, you will run a dry pass heudiconv on one subject to get this information. Then, you pull numbers from them to create your heuristic of the number of sessions, runs, localizers, T1s, etc. that your subject has. 

1. ```docker pull nipy/heudiconv```
3. Now we are going to run a dry pass on our dicoms to create a heuristic file:
    - Edit create_heuristic.sh file ```nano create_heuristic.sh```
    - Line 2: change path where DICOM data is located
    - Line 3: change path where BIDS data will be output
    - Lines 5-7: define a single subject, and subsequent folder organization (ses = session)
4. Execute create_heuristic.sh script ```sh create_heuristic.sh``` (sometimes this gives me trouble -- the best thing to do is just copy and paste the docker command)
5. Check output within BIDS folder ```ls -a```
    - Make sure you are within your BIDS directory
    - You should see a .heudiconv file
    - Continue to cd through this directory into the "info" directory
    - for example: /UD_repronim/heudiconv_tutorial/BIDS/.heudiconv/sub_01/info
6. Open the dicominfo.tsv file from this folder 
7. Move the heuristic.py script (stored in this folder) out to your main BIDS directory
8. Edit your heuristic.py script using this dicominfo.tsv file as a guide.

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
