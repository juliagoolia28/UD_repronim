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
