from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication, QLineEdit,QPushButton, QVBoxLayout, QHBoxLayout)
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



#Define Options for Parameters For Custom Configuration
Configuration = {"Configuration? ( If Default Config, Only Need To Select From This DropDown):": True,
                 "CUSTOM_CONFIGURATION": "CUSTOM_CONFIGURATION", "KENWORTH_DEFAULT": "KENWORTH_DEFAULT",
                 "PETERBUILT_DEFAULT": "PETERBUILT_DEFAULT", "DAF_DEFAULT": "DAF_DEFAULT",
                 "NMD_KW_DEFAULT": "NMD_KW_DEFAULT", "NMD_PB_DEFAULT": "NMD_PB_DEFAULT"}

Config_2 = {"Configuration?:(Choose Again)": True, "CUSTOM_CONFIGURATION": "CUSTOM_CONFIGURATION"}

Disp_Var = {"Display_Variant?:": True, "KW_15": 0, "PB_15": 1, "DAF_12.3": 2, "KW_7": 3, "PB_7": 4}

Transmission = {"Transmission?:": True, "Automatic": 0, "Automated Manual": 1, "Manual": 2, "Traxon": 3}

Engine = {"Engine Type?:": True, "Cummins": 0, "MX": 1}

RHS = {"RHS Installed?:": True, "Uninstalled": 0, "Installed": 1}

Logger = {"Logger Enabled?:": True, "Disabled": 0, "Enabled": 1}

Demo = {"Demo Enabled?:": True, "Disabled": 0, "Enabled": 1}

show_fps = {"Show_FPS?:": True, "No": 0, "Yes": 1}


#Manual Entry Parameters
Man_Entry_Param = ["Enter Sweet Spot High Value Below:", "Enter Sweet Spot Low Value Below:",]



#Default Configuration Parameters; includes manual entry parameters

KW_Default = {"cust_config": "KENWORTH_DEFAULT", "Cust_Config": "KENWORTH_DEFAULT", "Display_Var": 0,
          "Trans": 0, "Engine": 0, "RHS_Inst": 0, "Logger": 0, "Sweet_Spot_High": 100, "Sweet_Spot_Low": 200, "Demo": 0,
                  "show_fps": 0}

PB_Default = {"cust_config": "PETERBUILT_DEFAULT", "Cust_Config": "PETERBUILT_DEFAULT", "Display_Var": 0,
          "Trans": 0, "Engine": 0, "RHS_Inst": 0, "Logger": 0, "Sweet_Spot_High": 100, "Sweet_Spot_Low": 200, "Demo": 0,
                  "show_fps": 0}

DAF_Default = {"cust_config": "DAF_DEFAULT", "Cust_Config": "DAF_DEFAULT", "Display_Var": 0,
          "Trans": 0, "Engine": 0, "RHS_Inst": 0, "Logger": 0, "Sweet_Spot_High": 100, "Sweet_Spot_Low": 200, "Demo": 0,
                  "show_fps": 0}

NMD_KW_Default = {"cust_config": "NMD_KW_DEFAULT", "Cust_Config": "NMD_KW_DEFAULT", "Display_Var": 0,
          "Trans": 0, "Engine": 0, "RHS_Inst": 0, "Logger": 0, "Sweet_Spot_High": 100, "Sweet_Spot_Low": 200, "Demo": 0,
                  "show_fps": 0}

NMD_PB_Default = {"cust_config": "NMD_PB_DEFAULT", "Cust_Config": "NMD_PB_DEFAULT", "Display_Var": 0,
          "Trans": 0, "Engine": 0, "RHS_Inst": 0, "Logger": 0, "Sweet_Spot_High": 100, "Sweet_Spot_Low": 200, "Demo": 0,
                  "show_fps": 0}



#Create Dictionary containing all the parameters that are not entered manually

config_dict = {"cust_config": Configuration.keys(), "custom_config":Config_2.keys(), "disp_var": Disp_Var.keys(),
               "transmission": Transmission.keys(), "engine": Engine.keys(), "RHS": RHS.keys(), "Logger": Logger.keys(),
               "Demo": Demo.keys(), "show_fps": show_fps.keys()}


#ls is custom configuration selected list

ls = ["CONFIGURATION = %s\n", "\n$%s=", "\n-DISPLAY_VARIANT=%s", "\n-TRANSMISSION_MODEL=%s",
      "\n-ENGINE_MODEL=%s", "\n-RHS_INSTALLED=%s", "\n-LOGGER_ENABLED=%s", "\n-DEMO_ENABLED=%s", "\n-SHOW_FPS=%s"]

#ls_Default is default selected; includes manual entry

ls_Default = ["CONFIGURATION = %s\n", "\n$%s=", "\n-DISPLAY_VARIANT=%s", "\n-TRANSMISSION_MODEL=%s",
              "\n-ENGINE_MODEL=%s", "\n-RHS_INSTALLED=%s", "\n-LOGGER_ENABLED=%s", "\n-SWEET_SPOT_HIGH_VALUE=%s",
              "\n-SWEET_SPOT_LOW_VALUE=%s", "\n-DEMO_ENABLED=%s", "\n-SHOW_FPS=%s"]




class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #Create Button for Function Execution
        run_button = QPushButton("Press After Selecting/Entering Information, then close window", self)

        run_button.clicked.connect(self.onActivated)


        #Create Formating
        #vbox = QHBoxLayout()
        #vbox.addStretch(1)

        hbox = QVBoxLayout()
        hbox.addLayout(hbox)
        hbox.addWidget(run_button)

        self.setLayout(hbox)


        #Defines Dimensions of Window and Window Title

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Text File Creation')


        #define and create combobox's for every parameter that is not manual entry
        count = 0;
        self.combo_dict= {}
        for key, options in config_dict.items():
            count +=1
            combo = QComboBox(self)
            combo.addItems(options)
            self.combo_dict[key] = combo
            hbox.addWidget(combo)

        #self.manual_Entry creates is list of manual inputs for every manual input that needs to happen

        self.emp = []
        for i, manual in enumerate(Man_Entry_Param):
            text_box = QLineEdit(self)
            self.emp.append(text_box)
            self.lbl = QLabel(Man_Entry_Param[i])
            hbox.addWidget((self.lbl))
            hbox.addWidget(text_box)


        #Displays ComboBox Window
        self.show()




    #Function defines what happens in Python with what happens with ComboBox/manual entry selection
    def onActivated(self):

        #get dictionary objects
        self.selections = {}
        for key, combo_box in self.combo_dict.items():
            self.selections[key] = combo_box.currentText()

        #gets values from dictionary
        empt = []
        for i, final_values in self.selections.items():
            empt.append(final_values)


        #Define Text file to be used/written to
        text_file = open("digitalDisplayParameters.dcf", "w")



        if empt[0] == "CUSTOM_CONFIGURATION":

        ####get digits from GUI
            digits = []
            for key1 in empt:

                if key1 in Configuration.keys():
                    digits.append(Configuration[key1])
                elif key1 in Config_2.keys():
                    digits.append(Config_2[key1])
                elif key1 in Disp_Var.keys():
                    digits.append(Disp_Var[key1])
                elif key1 in Transmission.keys():
                    digits.append(Transmission[key1])
                elif key1 in Engine.keys():
                    digits.append(Engine[key1])
                elif key1 in RHS.keys():
                    digits.append(RHS[key1])
                elif key1 in Logger.keys():
                    digits.append(Logger[key1])
                elif key1 in Demo.keys():
                    digits.append(Demo[key1])
                elif key1 in show_fps.keys():
                    digits.append(show_fps[key1])
                #New Param Added; format like two lines below
                # elif key1 in NEW_PARAMETER.keys()
                    #digits.append(NEW_PARAMETER[key1])


        #Below writes combobox choices stored in "digits" list to txt file for Custom Config

            for i, k in enumerate(ls):
                text_file.write(k % digits[i])

        #Below writes Manual Entry fields to text file if Custom Configuration Selected

            Manual_Entry_Blank = []

            manual_entry = ["\n-SWEET_SPOT_HIGH_VALUE=%s", "\n-SWEET_SPOT_LOW_VALUE=%s"]



            for item in self.emp:
                Manual_Entry_Blank.append(item.text())

            for n,m in enumerate(manual_entry):
                text_file.write(m % Manual_Entry_Blank[n])


        #Writes Default Conditions to Text file

        elif empt[0] == "KENWORTH_DEFAULT":

            for i, k in enumerate(ls_Default):
                values = list(KW_Default.values())
                text_file.write(k % values[i])

        elif empt[0] == "PETERBUILT_DEFAULT":
            for i, k in enumerate(ls_Default):
                values = list(PB_Default.values())
                text_file.write(k % values[i])

        elif empt[0] == "DAF_DEFAULT":
            for i, k in enumerate(ls_Default):
                values = list(DAF_Default.values())
                text_file.write(k % values[i])
        elif empt[0] == "NMD_KW_DEFAULT":
            for i, k in enumerate(ls_Default):
                values = list(NMD_KW_Default.values())
                text_file.write(k % values[i])
        elif empt[0] == "NMD_PB_DEFAULT":
            for i, k in enumerate(ls_Default):
                values = list(NMD_PB_Default.values())
                text_file.write(k % values[i])



        # Write specifc string for cfg file for parsing

        text_file.write("\n%END_CONFIGURATION")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())