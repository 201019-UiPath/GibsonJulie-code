import os
import shutil
import sys
import time



def startPreprocessing(cwd, datadir):

    input_datadir = datadir + 'train_img'
    output_datadir = datadir + 'pre_img'

    os.chdir(cwd + '/FaceRecognition/')
    if not hasattr(sys, 'argv'):
        sys.argv  = ['']
    sys.path.append('.')

    if os.path.isdir(datadir + 'pre_img/'):
        shutil.rmtree(datadir + 'pre_img/')
        time.sleep(.3) # making sure the folder is completely deleted before trying to create it again
        os.mkdir(datadir+ 'pre_img/')

    from preprocess import preprocesses

    obj = preprocesses(input_datadir,output_datadir)

    nrof_images_total, nrof_successfully_aligned = obj.collect_data()
    return '{} {}'.format( obj.input_datadir, obj.output_datadir)
    #return 'Total number of images: {}. Number of successfully aligned images: {}'.format(nrof_images_total, nrof_successfully_aligned)
