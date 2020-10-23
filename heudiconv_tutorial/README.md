# Heudiconv Tutorial

## Resources:
[The main documentation for the Heudiconv Tutorial](https://neuroimaging-core-docs.readthedocs.io/en/latest/pages/heudiconv.html)

[James Kent created a fantstic step-by-step video that the current tutorial was adapted from](https://www.youtube.com/watch?v=O1kZAuR7E00)

[Why use BIDS/What is BIDS? An inspiring talk by Sam Nastase](https://docs.google.com/presentation/d/11MeS72TRLTiEwX4EbjWj84IFCTAmMJIawZF3VCLWLjA/edit#slide=id.g89c2127f6e_0_478)

## Creating a Heuristic File
A little background: Your MRI scan produces study specific information that you need to create a "cheat sheet" for. We call this "cheat sheet" a heuristics file. Basically, you will run a dry pass heudiconv on one subject to get this information. Then, you pull numbers from them to create your heuristic of the number of sessions, runs, localizers, T1s, etc. that your subject has. 

Ensure Docker is installed prior to beginning heudiconv.
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
