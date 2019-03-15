from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)
import sys

"""
Things to be edited/created when new parameters are created:

if parameter has options to chose from:
-create dict of parameter options:digit values in "Define Options for Parameters For Custom Configuration" Section Below 
-add newly created dict.keys to end of dictionary "config_dict" 
-add elif statement replicating format in "get digits from GUI" section of function "onActivated"

-add new parameter/default condition of new parameter to end of dictionaries in "Default Configuration Parameters"
-add/replicate format for new parameter in "ls", "ls_Default" of what output format is desired to txt file created
-- 

if parameter is manual entry text:
-add/format correctly to end of "Man_Entry_Param" and "manual_entry(found in onActivated function)" lists in script
-add new parameter/default condition of new parameter to end of dictionaries in "Default Configuration Parameters"
-add/replicate format for new parameter in "ls_Default" of what output format is desired to txt file created
"""

# Define Options for Parameters For Custom Configuration

Configuration = {"Configuration?": True,
                 "CUSTOM_CONFIGURATION": "CUSTOM_CONFIGURATION"}

Demo = {"Demo Enabled?:": True, "Disabled": 0, "Enabled": 1}

Config_2 = {"Configuration?:(Choose Again)": True, "CUSTOM_CONFIGURATION": "CUSTOM_CONFIGURATION"}

# Manual Entry Parameters
Man_Entry_Param = ["Enter Sweet Spot High Value Below:", "Enter Sweet Spot Low Value Below:", ]

# Default Configuration Parameters; includes manual entry parameters

KW_Default = {"Sweet_Spot_High": 100, "Sweet_Spot_Low": 200}



# Create Dictionary containing all the parameters that are not entered manually

config_dict = {
    "Demo": Demo.keys()}

# ls is custom configuration selected list

ls = ["\n-DEMO_ENABLED=%s"]

# ls_Default is default selected; includes manual entry

ls_Default = ["\n-SWEET_SPOT_HIGH_VALUE=%s",
              "\n-SWEET_SPOT_LOW_VALUE=%s", "\n-DEMO_ENABLED=%s"]


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Create Button for Function Execution
        run_button = QPushButton("Press After Selecting/Entering Information, then close window", self)

        run_button.clicked.connect(self.onActivated)

        # Create Formating
        # vbox = QHBoxLayout()
        # vbox.addStretch(1)

        hbox = QVBoxLayout()
        hbox.addLayout(hbox)
        hbox.addWidget(run_button)

        self.setLayout(hbox)

        # Defines Dimensions of Window and Window Title

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Text File Creation')

        # define and create combobox's for every parameter that is not manual entry
        count = 0;
        self.combo_dict = {}
        for key, options in config_dict.items():
            count += 1
            combo = QComboBox(self)
            combo.addItems(options)
            self.combo_dict[key] = combo
            hbox.addWidget(combo)

        # self.manual_Entry creates is list of manual inputs for every manual input that needs to happen

        self.emp = []
        for i, manual in enumerate(Man_Entry_Param):
            text_box = QLineEdit(self)
            self.emp.append(text_box)
            self.lbl = QLabel(Man_Entry_Param[i])
            hbox.addWidget((self.lbl))
            hbox.addWidget(text_box)

        # Displays ComboBox Window
        self.show()

    # Function defines what happens in Python with what happens with ComboBox/manual entry selection
    def onActivated(self):

        # get dictionary objects
        self.selections = {}
        for key, combo_box in self.combo_dict.items():
            self.selections[key] = combo_box.currentText()

        # gets values from dictionary
        empt = []
        for i, final_values in self.selections.items():
            empt.append(final_values)

        # Define Text file to be used/written to
        text_file = open("digitalDisplayParameters.dcf", "w")

        if empt[0] == "CUSTOM_CONFIGURATION":

            ####get digits from GUI
            digits = []
            for key1 in empt:

                if key1 in Configuration.keys():
                    digits.append(Configuration[key1])
                elif key1 in Config_2.keys():
                    digits.append(Config_2[key1])
                # New Param Added; format like two lines below
                # elif key1 in NEW_PARAMETER.keys()
                # digits.append(NEW_PARAMETER[key1])

            # Below writes combobox choices stored in "digits" list to txt file for Custom Config

            for i, k in enumerate(ls):
                text_file.write(k % digits[i])

            # Below writes Manual Entry fields to text file if Custom Configuration Selected

            Manual_Entry_Blank = []

            manual_entry = ["\n-SWEET_SPOT_HIGH_VALUE=%s", "\n-SWEET_SPOT_LOW_VALUE=%s"]

            for item in self.emp:
                Manual_Entry_Blank.append(item.text())

            for n, m in enumerate(manual_entry):
                text_file.write(m % Manual_Entry_Blank[n])


        # Writes Default Conditions to Text file

        elif empt[0] == "KENWORTH_DEFAULT":

            for i, k in enumerate(ls_Default):
                values = list(KW_Default.values())
                text_file.write(k % values[i])



        # Write specifc string for cfg file for parsing

        text_file.write("\n%END_CONFIGURATION")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())