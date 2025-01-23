Start
CUBIC_INCHES_IN_CUBIC_FOOT = 1728
PROMPT user for refrigerator model name
GET model_name
PROMPT user for height in inches
GET height
PROMPT user for width in inches
GET width
PROMPT user for depth in inches
GET depth
capacity_in_cubic_inches = height * width * depth
cubic_feet = capacity_in_cubic_inches / CUBIC_INCHES_IN_CUBIC_FOOT
DISPLAY "Refrigerator Model: " + model_name
DISPLAY "Capacity: " + cubic_feet + " cubic feet"
Stop
