import os

# create a function called create_key
def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes


def infotodict(seqinfo):
    # Section 1: These key definitions should be revised by the user
    ###################################################################
    # For each sequence, define a variable using the create_key function:
    # variable = create_key(output_directory_path_and_name).
    #
    # "data" creates sequential numbers which can be for naming sequences.
    # This is especially valuable if you run the same sequence multiple times at the scanner.
    data = create_key('run-{item:03d}')
    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
    tse = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_acq-tse_T2w')
    dwi = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_acq-AP_dwi')
    fmap_rev_phase =  create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_dir-PA_epi')
    fmap_mag =  create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_magnitude')
    fmap_phase = create_key('sub-{subject}/{session}/fmap/sub-{subject}_{session}_phasediff')
    func_rest = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-01_bold')
    func_rest_post = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_run-02_bold')
    asl = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_acq-asl_run-01')
    asl_post = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_acq-asl_run-02')

    # Section 1b: This data dictionary (below) should be revised by the user.
    # It uses the variables defines above as keys.
    ##########################################################################
    # Enter a key in the dictionary for each key you created above in section 1.
    info = {data: [], t1w: [], tse: [], dwi: [], fmap_rev_phase: [], fmap_mag: [], fmap_phase: [], func_rest: [], func_rest_post: [], asl: [], asl_post: []}
    last_run = len(seqinfo)

    # Section 2: These criteria should be revised by user.
    ##########################################################
    # Define test criteria to check that each dicom sequence is correct
    # seqinfo (s) refers to information in dicominfo.tsv. Consult that file for
    # available criteria.
    # Here we use two types of criteria:
    # 1) An equivalent field "==" (e.g., good for checking dimensions)
    # 2) A field that includes a string (e.g., 'mprage' in s.protocol_name)
    for idx, s in enumerate(seqinfo):
        if ('mprage' in s.protocol_name) and (s.dim3 == 176):
            info[t1w].append(s.series_id)
        if ('TSE' in s.protocol_name):
            info[tse].append(s.series_id)
        if ('DTI' in s.protocol_name) and (s.dim3 == 74) and (s.dim4 == 32):
            info[dwi].append(s.series_id)
        if ('verify_P-A' in s.protocol_name):
            info[fmap_rev_phase] = [s.series_id]
        if ('field_mapping' in s.protocol_name) and (s.dim3 == 64):
            info[fmap_mag] = [s.series_id]
        if ('field_mapping' in s.protocol_name) and (s.dim3 == 32):
            info[fmap_phase] = [s.series_id]
        if ('restingstate' == s.protocol_name):
            info[func_rest].append(s.series_id)
        if ('Post_TMS_restingstate' == s.protocol_name):
            info[func_rest_post].append(s.series_id)
        if ('ASL_3D_tra_iso' == s.protocol_name):
            info[asl].append(s.series_id)
        if ('Post_TMS_ASL_3D_tra_iso' == s.protocol_name):
            info[asl_post].append(s.series_id)
    return info

