## CHANGE LOG

### v0.1 : b8d49df

* Initial Commit

### v0.2 : cddbab6

* Added Changes Main Window GUI.
* Added Backend for trimming Feature.
* Added Settings-Profile feature.
* Added video player feature for trimming purposes.

### v0.3 : c1017a9

* Fixed Issue with TargetSize - Now, user will get proper notification about behavior.
* Fixed multiple blockers for video player feature.
* Added message box feature for custom prompts.
* Connected video player and backend of trimming feature.
* Added multiple UI fixes.

### v0.4 : 61b7634

* Added multiple miscellaneous polishing changes to code logic.
* Fixed issue of trimming interval overwrite when user loads settings - trimming interval will remain unaffected by setting any Config Save/Load operation during any flow.
* Made Video Player Frameless and Movable.
* Added Icon to all window objects.

### v0.5 : fe80575

* Added Time Seek Label to Seek Bar in video trimming window.
* Added user option to select custom output folder.
* Fixed trimming logic in video player to allow user to select either START or END - logic will automatically learn respective START and END.
* Modified Window titles to all possible window objects, provided icons as well.
* Updated .spec file to create full-fledged bundled exe.

### v0.6 : 8a6bd31

* Added Threading Functionality to isolate main video conversion process from GUI.
* Improved MessageBox Spawning.

### v0.7 : 5fd32bb

* Improved Threading Logic To Isolate Main Conversion Process
* Added In-ProgressUI Disable Feature
* Polished LoadConfig Logic

### v0.8 : af1fb41

* Fixed bug where multiple video player instances spawn
* Fixed bug where user was not able to 'Save' config after 'Load' config
* To avoid invalid trim intervals we have removed editing from interval fields
* Fixed bug to rectify disable/enable relation of Bitrate and framerate\
* Added drag option to entire plane of video player
* Added signature at the bottom of main UI

### v.09 : 675d2b0

* Added functionality to update the minimum target size placeholderText according to updated duration post- -trimming.
* Added functionality to automate the font installation flow.

### v.1.0 : c69e1b9

* Added Animation to message box of in-progress conversion.
* Handled force close event - terminated background ffmpeg process.
* Improved logic to avoid unnecessary triggers to elastic search data push during force close event.
* Any messageboxes on screen will be removed if main window is closed.
* Suppressed Slider Click warning issue.
* Added logic to ensure only one messagebox to present at any given time.
* Added disable button stylesheet during conversion process.
* Added Thumbnail Creation.

### v.1.1 : 35543d2

* Converted all message boxes from modal-less to modal design - all messageboxes will wait for user input.
* Added prompt to alert user about conversion format.
* Added logic to check source file existence on all possible operations - Convert, Trim, Play.
* Added opacity to all message boxes.
* Fixed a bug where Trimming Interval was omitted after using 'Load Config' feature.
* Fixed a bug where Outpath path derived from loaded config caused problem.
* Removed Delay before removing the csv file for elastic search.

### v.1.2 : ef0521b

* Fixed a bug where 'Minimum Suggested Size' was not updated properly after resetting the trim interval.
* Fixed a bug where output video was mistakenly deleted when tool window is closed.
* Improved this logic using by replacing thread running flag with isRunning method.
* Added Ubisoft Pune Logo.
* Improved trimming interval 'Reset' logic.
* Improved minimum trimming interval logic and added warning messagebox.
* Added stylesheets for 'Cavolini' font on Output Settings Fields.
* Added logic to automatically use extensions - need to modify one list only.
* Fixed a bug where Unset values were not handled properly in 'Load Config' feature.

### v.1.3 : 73d11f4

* Added logic to get Counts for Trim, Save/Load Config & Tool Trigger(Launch).
* Recreated the Kibana dashboard to encapsulate above changes.
* Fixed a complex issue where trimming interval behaved wrong after using reset settings.
* Added feature to hide console window of the tool without hampering the main execution.

### v.1.4 : 062ebf5f1c9faf2e240f0d05da360977f41b3761

* Added authentication using MFA dll.
* Added elastic ROI data push using autoserverconnector dll.
