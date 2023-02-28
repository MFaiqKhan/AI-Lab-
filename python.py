import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras # keras is a high level API for tensorflow, it makes it easier to build neural networks

# Define the feature rules as a list of dictionaries, where each dictionary has two keys: rule and value
# The rule key contains the feature rule and the value key contains the value of the feature rule
# rule key in each dictionary contains the feature rule that needs to be checked , 
# while the value key contains the value of the feature rule
# which is set to True by default, true means the feature rule is satisfied, 
# false means the feature rule is not satisfied

feature_rules = [
    {"rule": "Watermark of Quaid-e-Azam visible when held against light", "value": True},
    {"rule": "Electrotype Watermark of '20' visible when held against light", "value": True},
    {"rule": "Micro-Text Security Thread with 'State Bank of Pakistan' and '20' visible in embedded thread", "value": True},
    {"rule": "Portrait of Quaid-e-Azam in Sherwani visible on the right side of the note", "value": True},
    {"rule": "Value numeral '20' printed in Urdu appearing partly on obverse left top and partly on reverse right top", "value": True},
    {"rule": "Anti-scan and anti-copy line patterns appearing at the note to prevent scanning and photo copying", "value": True},
    {"rule": "Hidden image of denomination numeral appears while tilting the note at right side of the portrait of Quaid-e-Azam", "value": True},
    {"rule": "Raised line for visually impaired people appears on left side of the note", "value": True},
    {"rule": "Intaglio Lines appear at extreme right and left sides of the note", "value": True},
    {"rule": "Denomination appears in Urdu and English on the note", "value": True},
    {"rule": "Serial number with Prefix and magnetic ink visible on the note", "value": True},
    {"rule": "Signature of the Governor, State Bank of Pakistan visible in main color of the note", "value": True},
    {"rule": "Vignette of MOHEN-JO-DARO, LARKANA along with the name appear on the note", "value": True},
    {"rule": "Seal of the State Bank of Pakistan visible on the note", "value": True}
]

# Define a function to extract the features from an input image
def extract_features(img):
     # Load the image and convert to grayscale
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # inout image converted to greyscale before extracting the features because
    # it have only one channel (intensity) 
    # color images have three channels, red, green and blue, # what is a channel? 
    # channels are basically the color components of an image, # what is a color component?
    # color components are basically the intensity of the color, # what is intensity?
    # intensity is basically the amount of light reflected from the object. 
    # By reducing the image to a single channel, 
    # we simplify the computation required to extract features 
    # and reduce the amount of memory needed to store the image.




    # Resize the image to 200x200 pixels , # why do we need to resize the image? #  
    # to make it easier to extract the features and computationally less expensive
    img = cv2.resize(gray, (200, 200))

    # define the feature extractor from the feature rules list of dictionaries
    # using opencv to extract the features from the input different images of  20 rupee note

    watermark_extractor = cv2.imread("quaid_watermark.png") # load the image
    watermark_extractor = cv2.cvtColor(watermark_extractor, cv2.COLOR_BGR2GRAY) # convert to grayscale
    electrotype_extractor = cv2.imread("20_watermark.png")
    electrotype_extractor = cv2.cvtColor(electrotype_extractor, cv2.COLOR_BGR2GRAY)
    security_thread_extractor = cv2.imread("security_thread.png")
    security_thread_extractor = cv2.cvtColor(security_thread_extractor, cv2.COLOR_BGR2GRAY)
    portrait_extractor = cv2.imread("quaid_portrait.png")
    portrait_extractor = cv2.cvtColor(portrait_extractor, cv2.COLOR_BGR2GRAY)
    value_numeral_extractor = cv2.imread("value_numeral.png")
    value_numeral_extractor = cv2.cvtColor(value_numeral_extractor, cv2.COLOR_BGR2GRAY)
    anti_scan_extractor = cv2.imread("anti_scan.png")
    anti_scan_extractor = cv2.cvtColor(anti_scan_extractor, cv2.COLOR_BGR2GRAY)
    hidden_image_extractor = cv2.imread("hidden_image.png")
    hidden_image_extractor = cv2.cvtColor(hidden_image_extractor, cv2.COLOR_BGR2GRAY)
    raised_line_extractor = cv2.imread("raised_line.png")
    raised_line_extractor = cv2.cvtColor(raised_line_extractor, cv2.COLOR_BGR2GRAY)
    intaglio_extractor = cv2.imread("intaglio.png")
    intaglio_extractor = cv2.cvtColor(intaglio_extractor, cv2.COLOR_BGR2GRAY)
    denomination_extractor = cv2.imread("denomination.png")
    denomination_extractor = cv2.cvtColor(denomination_extractor, cv2.COLOR_BGR2GRAY)
    serial_num_extractor = cv2.imread("serial_num.png")
    serial_num_extractor = cv2.cvtColor(serial_num_extractor, cv2.COLOR_BGR2GRAY)
    signature_extractor = cv2.imread("signature.png")
    signature_extractor = cv2.cvtColor(signature_extractor, cv2.COLOR_BGR2GRAY)
    vignette_extractor = cv2.imread("vignette.png")
    vignette_extractor = cv2.cvtColor(vignette_extractor, cv2.COLOR_BGR2GRAY)
    seal_extractor = cv2.imread("seal.png")
    seal_extractor = cv2.cvtColor(seal_extractor, cv2.COLOR_BGR2GRAY)

    # Extract the features from the input image using opencv matchTemplate function
    # matchTemplate function is used to find the location of the template image in the input image
    # here gray is the input image and watermark_extractor is the template image
    # returns a 2D array of matching scores, where each score corresponds to a particular location in the input image
    # the higher the score, the more similar the template is to the region of the input image

    # TM_CCOEFF_NORMED is the method used to find the location of the template image in the input image
    # normalize the correlation coefficient by the number of pixels in the template image
    # resulting in a value between -1 and 1, where -1 indicates perfect negative correlation,
    # 0 indicates no correlation, and 1 indicates perfect positive correlation
    # the best matches are those with a score close to 1


    # This code uses the OpenCV function cv2.matchTemplate() to find the location of the watermark of the banknote image.
    watermark = cv2.matchTemplate(gray, watermark_extractor, cv2.TM_CCOEFF_NORMED)
    electrotype = cv2.matchTemplate(gray, electrotype_extractor, cv2.TM_CCOEFF_NORMED)
    security_thread = cv2.matchTemplate(gray, anti_scan_extractor, cv2.TM_CCOEFF_NORMED)
    portrait = cv2.matchTemplate(gray, portrait_extractor, cv2.TM_CCOEFF_NORMED)
    value_numeral = cv2.matchTemplate(gray, value_numeral_extractor, cv2.TM_CCOEFF_NORMED)
    anti_scan = cv2.matchTemplate(gray, anti_scan_extractor, cv2.TM_CCOEFF_NORMED)
    hidden_image = cv2.matchTemplate(gray, hidden_image_extractor, cv2.TM_CCOEFF_NORMED)
    raised_line = cv2.matchTemplate(gray, raised_line_extractor, cv2.TM_CCOEFF_NORMED)
    intaglio = cv2.matchTemplate(gray, intaglio_extractor, cv2.TM_CCOEFF_NORMED)
    denomination = cv2.matchTemplate(gray, value_numeral_extractor, cv2.TM_CCOEFF_NORMED)
    serial_num = cv2.matchTemplate(gray, serial_num_extractor, cv2.TM_CCOEFF_NORMED)
    signature = cv2.matchTemplate(gray, signature_extractor, cv2.TM_CCOEFF_NORMED)
    vignette = cv2.matchTemplate(gray, vignette_extractor, cv2.TM_CCOEFF_NORMED)
    seal = cv2.matchTemplate(gray, seal_extractor, cv2.TM_CCOEFF_NORMED)



    # normalizing it again to 0 or 1 (binary value) based on a threshold, which is 0.8 in this case.
    # any feature value greater than 0.8 or equal is considered to be present in the image
    # any feature value less than 0.8 is considered to be absent in the image
    # max function is used to find the maximum value in the 2D array returned by the matchTemplate function


    # Normalize the feature values to 0 or 1 based on a threshold
    threshold = 0.8
    features = [1 if feature >= threshold else 0 for feature in [watermark.max(), electrotype.max(), 
                security_thread.max(), portrait.max(), value_numeral.max(), anti_scan.max(), 
                hidden_image.max(), raised_line.max(), intaglio.max(), denomination.max(), 
                serial_num.max(), signature.max(), vignette.max(), seal.max()]]

    # Return the feature vector as a numpy array
    return np.array(features)

# Loop through each feature rule and extract the corresponding feature
for rule in feature_rules:
    if rule["rule"] == "Watermark of Quaid-e-Azam visible when held against light":
        result = cv2.matchTemplate(gray, watermark_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Electrotype Watermark of '20' visible when held against light":
        result = cv2.matchTemplate(gray, electrotype_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Micro-Text Security Thread with 'State Bank of Pakistan' and '20' visible in embedded thread":
        result = cv2.matchTemplate(gray, anti_scan_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Portrait of Quaid-e-Azam in Sherwani visible on the right side of the note":
        result = cv2.matchTemplate(gray, portrait_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Value numeral '20' printed in Urdu appearing partly on obverse left top and partly on reverse right top":
        result = cv2.matchTemplate(gray, value_numeral_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Anti-scan and anti-copy line patterns appearing at the note to prevent scanning and photo copying":
        result = cv2.matchTemplate(gray, anti_scan_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Hidden image of denomination numeral appears while tilting the note at right side of the portrait of Quaid-e-Azam":
        result = cv2.matchTemplate(gray, hidden_image_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Raised line for visually impaired people appears on left side of the note":
        result = cv2.matchTemplate(gray, raised_line_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Intaglio Lines appear at extreme right and left sides of the note":
        result = cv2.matchTemplate(gray, intaglio_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False
    
    elif rule["rule"] == "Denomination numeral '20' printed in Urdu appears on the left side of the note":
        result = cv2.matchTemplate(gray, denomination_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result) # max_val is the value of the best match
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Serial number appears on the right side of the note":
        result = cv2.matchTemplate(gray, serial_num_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False
    
    elif rule["rule"] == "Signature of Governor State Bank of Pakistan appears on the right side of the note":
        result = cv2.matchTemplate(gray, signature_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "Vignette of Quaid-e-Azam appears on the left side of the note":
        result = cv2.matchTemplate(gray, vignette_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False

    elif rule["rule"] == "seal of State Bank of Pakistan appears on the left side of the note":
        result = cv2.matchTemplate(gray, seal_extractor, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False
    













# Define a function to classify the input image
def classify(img):
    # Extract the features from the input image
    features = extract_features(img)
    # Load the model
    model = keras.models.load_model('model.h5')
    # Predict the class of the input image
    prediction = model.predict([features])
    # Return the predicted class
    return prediction

# Define a function to display the results
def display_results(img, prediction):
    # Display the input image
    cv2.imshow('Input Image', img)
    # Display the results
    if prediction == 0:
        print("The input image is a fake note")
    else:
        print("The input image is a real note")
    # Wait for a key press
    cv2.waitKey(0)
    # Destroy all the windows
    cv2.destroyAllWindows()

# Define a function to test the model
def test_model():
    # Load the input image
    img = cv2.imread('test.jpg')
    # Classify the input image
    prediction = classify(img)
    # Display the results
    display_results(img, prediction)