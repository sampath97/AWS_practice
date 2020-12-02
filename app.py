#python code that can be used for running FLASK+OpenCV

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import cv2
import os
import imutils
from img_algo import convert_to_grayscale

print(cv2.__version__)

UPLOAD_FOLDER='static/uploads/'
app = Flask('stock_pricer',template_folder='templates')
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route('/')
def show_predict_stock_form():
    return render_template('predictform.html',img_path='#',img_visibility='display: none')
@app.route('/', methods=['POST'])
def result():
    uploaded_file = request.files['file']
    if uploaded_file !='':
        uploaded_file_name=secure_filename(uploaded_file.filename)
        print(uploaded_file.filename)
        uploaded_file.save(os.path.join(UPLOAD_FOLDER, uploaded_file_name))
        img_loc=os.path.join(UPLOAD_FOLDER, uploaded_file_name)
        print(img_loc)

        #show the processed file
        gray_img=convert_to_grayscale(img_loc)
        gray_img_path=os.path.join(UPLOAD_FOLDER,'filtimage.JPG')
        cv2.imwrite(gray_img_path,gray_img)
        '''
        #read the filtered image
        filt_img=cv2.imread(gray_img_path)
        cv2.imshow('Filtered Image',filt_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''
        print(gray_img_path)
        return render_template('predictform.html',img_path=gray_img_path,img_visibility='display: block')
    
    #form = request.form
    #if request.method == 'POST':


app.run("localhost", "9999", debug=True)