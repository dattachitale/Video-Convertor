mainFrameSS = """
                background-color: rgb(15, 52, 84);
                border-radius: 10px;
                opacity: 0.8;
                """

titleLabelSS = """QLabel
                {
                    font: 700 40pt "Ubisoft Sans";
                    color:#FFF;
                    background-color: none;
                    border-radius:20px;
                    border: 1 px
                }"""

helpButtonSS = """QPushButton
                {
                    border-radius:24px;
                    background-color: white
                }
                                                             
                
                QPushButton:Hover
                {
                    background-color:rgba(255, 255, 255, 128);
                    border: 2px solid white
                }
                                                               
                QPushButton:Pressed
                {
                     border: 2px solid rgb(199, 199, 199);                     
                    
                }"""

minimizeButtonSS = """QPushButton
                    {
                        border-radius:24px;
                        background-color: white
                    }
                                                                 
                    
                    QPushButton:Hover
                    {
                        background-color:rgba(255, 255, 255, 128);
                        border: 2px solid white
                    }
                                                                   
                    QPushButton:Pressed
                    {
                         border: 2px solid rgb(199, 199, 199);                     
                        
                    }"""

closeButtonSS = """QPushButton
                    {
                        border-radius:24px;
                        background-color: white;
                    }
                                                                 
                    
                    QPushButton:Hover
                    {
                        background-color:rgba(255, 255, 255, 128);
                        border: 2px solid white;
                    }
                                                                   
                    QPushButton:Pressed
                    {
                         border: 2px solid rgb(199, 199, 199);                     
                        background-color: rgb(126, 10, 26);
                    }"""

selectVideoButtonSS = """QPushButton
                    {
                    font: 700 13pt "Ubisoft Sans";
                    
                    border-radius: 5px;
                    color:#FFF;
                    background-color: rgb(45, 146, 237);
                    padding-bottom:3px
                    }
                    
                    QPushButton:Hover
                    {
                    
                    background-color: rgb(105, 180, 234);
                    }
                                                                   
                    QPushButton:Pressed
                    {
                    background-color: #0065ba;
                    }"""

outputFolderLabelSS = """QLabel
                        {
                            font: 700 13pt "Ubisoft Sans";
                            border: 1px;
                            border-radius:none;
                            color: #FFF;
                            background-color:none;
                        }"""


outputPathLineEditSS = """QLineEdit
                        {     
                            background-color: #476994;
                            border: 1px solid rgb(199, 199, 199);
                            border-radius: 8px;
                            padding: 13px;
                            color:#FFF;
                            font:  11pt "Ubisoft Sans";
                        }"""

setOutputPathButtonSS = """QPushButton
                      {
                            
                        font: 700 18pt "Ubisoft Sans";
                        border-radius: 3px;
                        background-color: rgb(45, 146, 237);
                        color:rgb(197, 197, 197)
                      }
                    
                    QPushButton:Hover
                    {
                    
                    background-color: rgb(105, 180, 234);
                    }
                                                                   
                    QPushButton:Pressed
                    {
                    background-color: #0065ba;
                    }"""



#Video Information Data
infoFrameSS = """QFrame
                {
                    border: 2px solid rgb(199, 199, 199);
                    border-radius:8px;
                    color: #FFF;
                    background-color: none;
                }"""
videoInformationLabelSS = """QLabel
                            {
                                font: 700 17pt "Ubisoft Sans";
                                background-color:#3f8e92;
                                border-radius:5px;
                                border: 1 px
                            }"""

thumnailFrameSS = """QFrame
                {
                border: 1px solid rgb(199, 199, 199);
                border-radius: 0px;
                color: #FFF;
                background-color:#6497b1;
                }"""
infoplayVideoButtonDisableSS = """QPushButton
                                {
                                  
                                    border-radius: 25px;
                                    background-color:  rgb(100, 129, 147);                   
                                }"""
infoplayVideoButtonEnableSS = """QPushButton
                                {
                                    
                                    border-radius: 25px;
                                    background-color:   rgb(45, 146, 237);
                                }
                                QPushButton:hover
                                {       
                                  
                                    border-radius: 24px;
                                    background-color: rgb(105, 180, 234);
                                }
                                QPushButton:pressed
                                {       
                                  
                                    background-color: #0065ba;;
                                }"""
infoAllLabel1SS = """QLabel
                    {
                    font: 700 13pt "Ubisoft Sans";
                    border: 1px;
                    color: #FFF;
                    }"""

infoAllLabel1DisableSS = """QLabel
                    {
                    font: 700 13pt "Ubisoft Sans";
                    border: 1px;
                    color: rgb(168, 168, 168);
                    }"""

infoAllLabel2DisableSS = """QLabel
                            {
                            font: 700 10pt "Ubisoft Sans";
                            border: 1px;
                            color:rgb(168, 168, 168);
                            }"""
infoAllLabel2EnableSS = """QLabel
                        {
                            font: 700 10pt "Ubisoft Sans";
                            border: 1px;
                            color:rgb(218, 218, 218)
                        }"""


#Conversion Settings Data
convertFrameSS = """QFrame
                    {
                        border: 2px solid rgb(199, 199, 199);
                        color: #FFF;
                        border-radius:8px;
                        background-color: none;
                    }"""
conversionSettingsLabelSS = """QLabel
                        {
                            font: 700 17pt "Ubisoft Sans";
                            background-color:#3f8e92;
                            border-radius:5px;
                            border: 1 px
                        }"""

trimSettingFrameSS = """QFrame
                        {
                            border: 2px solid rgb(199, 199, 199);
                            color: #FFF;
                            background-color: none;
                            border-radius:1px;
                        }"""
trimSettingsLabelSS = """QLabel
                        {
                                font: 700 15pt "Ubisoft Sans";
                            background-color:#3f8e92;
                            border-radius: 5px;
                            border: 1 px
                        }"""

startEndTimeLineEditEnableSS = """QLineEdit
                                {
                                font:  11pt "Ubisoft Sans";
                                border: 1px solid rgb(199, 199, 199);
                                border-radius:5px;
                                color: #FFF;
                                padding-left:8px;
                                background-color: #476994;
                                }"""

startEndTimeLineEditDisableSS = """QLineEdit
                                {
                                font:  11pt "Ubisoft Sans";
                                border: 1px solid rgb(199, 199, 199);
                                border-radius:5px;
                                color: #FFF;
                                padding-left:8px;
                                background-color: #476994;
                                }"""

outputSettingFrameSS = """QFrame
                        {
                            border: 1px solid rgb(199, 199, 199);
                            color: #FFF;
                            border-radius:1px;
                            background-color: none;
                        }"""
outputSettingsLabelSS = """QLabel
                        {
                            font: 700 15pt "Ubisoft Sans";
                            background-color:#3f8e92;
                            border-radius: 5px;
                            border: 1 px
                        }"""

bitrateReductionFpsSpinBoxDisableSS = """QSpinBox
                                    {
                                    border: 1px solid rgb(199, 199, 199);
                                    font: 11pt "Ubisoft Sans";
                                    border-radius:5px;
                                    color: rgb(197, 197, 197);
                                    background-color:rgb(100, 129, 147)
                                    }"""

bitrateReductionFpsSpinBoxEnableSS = """QSpinBox
                                        {   
                                            font: 11pt "Ubisoft Sans";
                                            border: 1px solid rgb(199, 199, 199);
                                            border-radius:5px;
                                            color: #FFF;
                                            background-color: #476994;
                                        }"""
bitrateReductionPercentLabelSS = """QLabel
                                    {
                                        font: 700 11pt "Ubisoft Sans";
                                        border: 1px;
                                        color: #FFF;
                                    }"""
resolutionComboBoxFrameSS = """QFrame
                            {   
                                font: 11pt "Ubisoft Sans";
                                border: none;
                                border-radius:5px;
                                background-color:rgb(0, 91, 150);
                            }"""
resolutionComboBoxDisableSS = """QComboBox
                        {
                            font: 11pt "Ubisoft Sans";;
                            border: 1px solid rgb(199, 199, 199);
                            border-radius:5px;
                            color: rgb(197, 197, 197);
                            background-color:rgb(100, 129, 147);
                            padding-left:60px;
                        }"""
resolutionComboBoxEnableSS = """QComboBox
                                {
                                    font: 11pt "Ubisoft Sans";
                                    border: 1px solid rgb(199, 199, 199);
                                    border-radius:5px;
                                    color: #FFF;
                                    background-color: rgb(0, 91, 150)
                                }"""

keepAudioFrameSS ="""QFrame
                    {
                        border-radius:5px;
                    }"""
keepAudioCheckBoxDisableSS = """QCheckBox
                        {
                            background-color: none;
                            font: 700 13pt "Ubisoft Sans";
                            border-radius: 5px;
                            color:rgb(197, 197, 197);
                            padding-bottom:3px
                        }"""
keepAudioCheckBoxEnableSS = """QCheckBox
                        {
                            background-color: none;
                            font: 700 13pt "Ubisoft Sans";
                            border-radius: 5px;
                            color: #FFF;
                            padding-bottom:3px
                        }"""


targetSizeFrameSS = """QFrame
                    {
                        border-radius:5px;
                    }"""
targetSizeLabelSS = """QLabel
                    {
                        font: 700 13pt "Ubisoft Sans";
                        border: 1px;
                        color: rgb(197, 197, 197);
                    }"""
provideSizeLineEditDisableSS = """QLineEdit
                                {
                                    border: 1px solid rgb(199, 199, 199);
                                    border-radius:5px;
                                    color: rgb(197, 197, 197);
                                    background-color: rgb(100, 129, 147)
                                }"""
provideSizeLineEditEnableSS = """QLineEdit
                                {
                                    border: 1px solid rgb(199, 199, 199);
                                    border-radius:5px;
                                    color: #FFF;
                                    background-color: #476994;
                                }"""

outputFormatFrameSS = """QFrame
                        {
                            border: 2px solid rgb(199, 199, 199);
                            color: #FFF;
                            border-radius:5px;
                            background-color: none;
                            border-radius:1px;
                        }"""
outputFormatLabelSS = """QLabel
                        {
                                font: 700 15pt "Ubisoft Sans";
                            background-color:#3f8e92;
                            border-radius: 5px;
                            border: 1 px
                        }"""

outputFormatAllRadioButtonSS = """QRadioButton
                                {
                                    background-color: none;
                                    border-radius: 5px;
                                    color:#FFF;
                                    padding-bottom:3px
                                }
                                """

#All push button stylesheet
allPushButtonDisableSS = """QPushButton
                        {
                        font: 700 13pt "Ubisoft Sans";
                        
                        border-radius: 5px;
                        color:rgb(197, 197, 197);
                        background-color:rgb(100, 129, 147);
                        padding-bottom:2px
                        }"""
allPushButtonEnableSS = """QPushButton
                        {
                        font: 700 13pt "Ubisoft Sans";
                        border-radius: 5px;
                        color:#FFF;
                        background-color: rgb(45, 146, 237);
                        padding-bottom:3px
                        }
                        
                        QPushButton:Hover
                        {
                        
                        background-color: rgb(105, 180, 234);
                        }
                                                                       
                        QPushButton:Pressed
                        {
                        background-color: #0065ba;
                        }"""

'''
Stylesheet for Video Player class
'''

videoPlayerMainFrameSS = """QFrame
                            {
                                border: 2px solid rgb(199, 199, 199);
                                color: #FFF;
                                background-color: none;
                                border-radius:5px;
                            }
                            """

videoWidgetFrameSS = """QFrame
                        {
                            border: 2px solid rgb(199, 199, 199);
                            color: #FFF;
                            background-color: none;
                            border-radius:5px;
                            border-radius:1px;
                        }"""

seekSliderFrameSS = """QFrame
                        {
                            background-color: none;
                            border: 1px rgb(255, 255, 255)
                        }"""

seekSliderSS = """QSlider
                {
                    border: none;
                    background-color: none;
                }"""

videoTimeLabelSS = """QLabel
                    {
                        font: 700 12pt "Ubisoft Sans";
                        border:None;
                        color: #FFF;
                        background-color:none
                    }"""

trimControlFrameSS ="""QFrame
                    {
                        border: 2px solid rgb(199, 199, 199);
                        background-color: none;
                    }
                    """

playButtonDisableSS = """QPushButton
                    {
                        font: 700 13pt "Ubisoft Sans";
                        border-radius: 19px;
                        color:rgb(197, 197, 197);
                        background-color:rgb(100, 129, 147);
                        padding-left:4px;
                    }"""

playButtonEnableSS = """QPushButton
                    {
                        font: 700 10pt "Ubisoft Sans";
                        border-radius: 19px;
                        color:#FFF;
                        background-color:rgb(45, 146, 237);
                        padding-left:4px;
                    }
                    
                    QPushButton:Hover
                    {
                        background-color: rgb(105, 180, 234);
                    }
                                                                   
                    QPushButton:Pressed
                    {
                                           
                        background-color: #0065ba;
                    }"""

pauseButtonDisableSS = """QPushButton
                    {
                        font: 700 13pt "Ubisoft Sans";
                        border-radius: 19px;
                        color:rgb(197, 197, 197);
                        background-color:rgb(100, 129, 147);
                    }"""

pauseButtonEnableSS = """QPushButton
                    {
                        font: 700 10pt "Ubisoft Sans";
                        border-radius: 19px;
                        color:#FFF;
                        background-color:rgb(45, 146, 237);
                    }
    
                    QPushButton:Hover
                    {
                        background-color: rgb(105, 180, 234);
                    }
                                                                   
                    QPushButton:Pressed
                    {                  
                        background-color: #0065ba;
                    }"""

stopButtonDisableSS = """QPushButton
                    {
                        font: 700 13pt "Ubisoft Sans";
                        border-radius: 19px;
                        color:rgb(197, 197, 197);
                        background-color:rgb(100, 129, 147);
                    }"""

stopButtonEnableSS = """QPushButton
                    {
                        font: 700 10pt "Ubisoft Sans";
                        border-radius: 19px;
                        color:#FFF;
                        background-color:rgb(45, 146, 237);
                    }
    
                    QPushButton:Hover
                    {
                        background-color: rgb(105, 180, 234);
                    }
                                                                   
                    QPushButton:Pressed
                    {            
                        background-color: #0065ba;
                    }"""


playerControlLabelSS = """QLabel
                        {
                            font: 700 14pt "Ubisoft Sans";
                            background-color:#3f8e92;
                            border-radius: 5px;
                            border: 1 px
                        }"""

trimControlLabelSS = """QLabel
                        {
                            font: 700 14pt "Ubisoft Sans";
                            background-color:#3f8e92;
                            border-radius: 5px;
                            border: 1 px
                        }"""

startEndTrimButtonSS = """QPushButton
                    {
                        font: 700 11pt "Ubisoft Sans";
                        border-radius: 5px;
                        color:#FFF;
                        background-color:rgb(45, 146, 237);
                    }
                    
                    QPushButton:Hover
                    {
                        background-color: rgb(105, 180, 234);
                    }
                                                                   
                    QPushButton:Pressed
                    {                     
                        background-color: #0065ba;
                    }"""

startEndTrimLabelSS = """QLabel
                        {
                            font:  12pt "Ubisoft Sans";
                            border:None;
                            color: #FFF;
                            padding-left:10px;
                            background-color:none
                        }"""

allVideoPlayerPushButtonEnableSS ="""QPushButton
                                    {
                                    font: 700 13pt "Ubisoft Sans";
                                    border-radius: 5px;
                                    color:#FFF;
                                    background-color: rgb(45, 146, 237);
                                    padding-bottom:3px
                                    }
                                    
                                    QPushButton:Hover
                                    {
                                    
                                    background-color: rgb(105, 180, 234);
                                    }
                                                                                   
                                    QPushButton:Pressed
                                    {
                                    background-color: #0065ba;
                                    }"""

trimWindowLabelSS = """QLabel
                    {
                        font: 700 43pt "Ubisoft Sans";
                        color:#FFF;
                        
                        background-color: none;
                        border-radius:20px;
                        border: 1 px
                    }"""



# MessageBoxClass Stylesheet
messageBoxMainFrameSS = """
                background-color: rgb(15, 52, 84);
                border-radius: 8px;
                border:1px solid white;
                opacity: 0.8;
                """
messageBoxOkayButtonSS = """QPushButton
                        {
                        font: 700 13pt "Ubisoft Sans";
                        border-radius: 10px;
                        border:none;
                        color:#FFF;
                        background-color:rgb(45, 146, 237);
                        padding-bottom:3px
                        }
                        
                        QPushButton:Hover
                        {
                        background-color: rgb(105, 180, 234);
                        }
                                                                       
                        QPushButton:Pressed
                        {
                        border: 2px solid rgb(199, 199, 199);                     
                        background-color: #343d46;
                        }"""

messageBoxOkayButtonDisableSS = """QPushButton
                                    {
                                    font: 700 13pt "Ubisoft Sans";
                                    border-radius: 10px;
                                    color:rgb(197, 197, 197);
                                    background-color:rgb(100, 129, 147);
                                    padding-bottom:3px;
                                    width: 111px;
                                    height: 35px;
                                }
                                
                                QPushButton:Hover
                                {
                                
                                    
                                    width: 111px;
                                    height: 35px;
                                }
                                                                               
                                QPushButton:Pressed
                                {
                                    border: 2px solid rgb(199, 199, 199);                     
                                    background-color: rgb(100, 129, 147);
                                    width: 111px;
                                    height: 35px;
}"""

messageBoxTextIconSS = """QLabel
                        {
                            font: 700 12pt "Ubisoft Sans";
                            border:None;
                            background-color:none
                        }"""

messageBoxTextLabelSS = """QLabel
                        {
                            font:  14pt "Ubisoft Sans";
                            border:None;
                            color: #FFF;
                            padding-left:10px;
                            background-color:none
                        }"""

messageBoxWindowLabelSS = """QLabel
                        {
                            font: 700 20pt "Ubisoft Sans";
                            color:#FFF;
                            background-color: none;
                            border-radius:20px;
                            border: 1 px
                        }"""

messageBoxCloseButtonSS = """QPushButton
                            {
                                border-radius:20px;
                                background-color: white;
                            }
                                                                         
                            
                            QPushButton:Hover
                            {
                                background-color:rgba(255, 255, 255, 128);
                                border: 2px solid white
                            }
                                                                           
                            QPushButton:Pressed
                            {
                                 border: 2px solid rgb(199, 199, 199);                     
                                background-color: rgb(126, 10, 26);
                            }"""

signLabelSS = """QLabel
                {
                    font: 700 13pt "Ubisoft Sans";
                    border: 1px;
                    border-radius:none;
                    background-color: none;
                    color: rgb(216, 216, 216)
                }
            """
signLovelabelSS = """QLabel
                    {
                        font: 700 20pt "Ubisoft Sans";
                        border: 1px;
                        border-radius:none;
                        background-color: none;
                        color: rgb(216, 216, 216)
                    }
                    """
#Animation
animationFrameSS = """QFrame
                   {
                        background-color: none;
                        border-radius: 1px;
                        border: 1px solid rgb(199, 199, 199);
                    }"""

animationFrame_2SS = """QFrame
                    {
                    	background-color: none;
                    	border-radius: 1px;
                    	border: 1px solid rgb(199, 199, 199);
                    }"""
rectFrameSS = """QFrame
                 {
                 	background-color: rgb(78, 157, 116);
                 	border: none;
                 }"""

#output_format_msgbox stylesheet
outputformatMessageBoxMainFrameSS = """
                background-color: rgb(15, 52, 84);
                border-radius: 8px;
                border:1px solid white;
                opacity: 0.8;
                """
buttonBoxSS = """QPushButton
                {
                    font: 700 13pt "Ubisoft Sans";
                    border:none;
                    border-radius: 5px;
                    color:#FFF;
                    background-color:rgb(45, 146, 237);
                    padding-bottom:3px;
                    width: 111px;
                    height: 35px;
                }
                
                QPushButton:Hover
                {
                    background-color: rgb(105, 180, 234);
                    width: 111px;
                    height: 35px;
                }
                                                               
                QPushButton:Pressed
                {
                                        
                    background-color: #0065ba;
                    width: 111px;
                    height: 35px;
                }"""

#logo stysheet
logoLableSS = """QFrame
             {
             border: none;
             }"""