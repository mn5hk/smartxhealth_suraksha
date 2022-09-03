# smartxhealth_surakshit
This repo contains submissions of Team Surakshya for the IISc-Siemens Hackathon 2022 https://iisc.ac.in/events/smartx-health-2022-a-iisc-siemens-hackathon/ 

The following workflow has been used for the coding pipeline:
<ul>
  <li>In the command line, yolo object detection model has been run to detect people and gloves. The details on the model run can be found here: https://sway.office.com/d1TSLFNdzswF4MOb The model was not fully trained and did not perform well; further, the model was only implemented in the command line and the results have not been further continued down the coding pipeflow.</li>
  <li>The second part of the code is built in the python programming interface; Here, random instance generator is used to simulate detection of people and detection of gloves; if people are detected in the frame and gloves not detected, the model counts the instance. If the number of instances sequentially detected exceeds a threshold (threshold = 3), the code sends a notification. The code can be found in 02_smartxhealth_alert.py file. The binder launcher for the python file is: 
  </li>
  <li>The third part of the coding pipeline consists of an interactive prototype for the front-end (what the user sees); made in Figma. The link to the Figma interactive prototype is presented here: https://www.figma.com/proto/FtyR9RQhNZumGHKDpkWyjn/Team_Surakshya?node-id=6%3A26&scaling=min-zoom&page-id=6%3A25
  </li>
  </ul>
[![Binder](https://mybinder.org/badge_logo.svg)] (https://mybinder.org/v2/gh/mn5hk/smartxhealth_surakshit/HEAD) <br>



