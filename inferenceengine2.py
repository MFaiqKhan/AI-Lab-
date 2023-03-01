import cv2

def validate_security_features(image_path):
    # Load image and convert to grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Define feature rules and corresponding feature extractors
    feature_rules = [
        {"rule": "Watermark of Quaid-e-Azam visible when held against light", "extractor": watermark_extractor},
        {"rule": "Electrotype Watermark of '20' visible when held against light", "extractor": electrotype_extractor},
        {"rule": "Micro-Text Security Thread with 'State Bank of Pakistan' and '20' visible in embedded thread", "extractor": anti_scan_extractor},
        {"rule": "Portrait of Quaid-e-Azam in Sherwani visible on the right side of the note", "extractor": portrait_extractor},
        {"rule": "Value numeral '20' printed in Urdu appearing partly on obverse left top and partly on reverse right top", "extractor": value_numeral_extractor},
        {"rule": "Anti-scan and anti-copy line patterns appearing at the note to prevent scanning and photo copying", "extractor": anti_scan_extractor},
        {"rule": "Hidden image of denomination numeral appears while tilting the note at right side of the portrait of Quaid-e-Azam", "extractor": hidden_image_extractor},
        {"rule": "Raised line for visually impaired people appears on left side of the note", "extractor": raised_line_extractor},
        {"rule": "Intaglio Lines appear at extreme right and left sides of the note", "extractor": intaglio_extractor}
    ]

    # Loop through each feature rule and extract the corresponding feature
    for rule in feature_rules:
        result = cv2.matchTemplate(gray, rule["extractor"], cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val < 0.8:
            rule["value"] = False
        else:
            rule["value"] = True

    # Return the validation results
    return feature_rules
