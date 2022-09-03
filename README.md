# smartxhealth_surakshit
This repo contains submissions of Team Surakshya for the IISc-Siemens Hackathon 2022 https://iisc.ac.in/events/smartx-health-2022-a-iisc-siemens-hackathon/ 

The following workflow has been used for the coding pipeline:
<ul>
  <li>In the command line, yolo object detection model has been run to detect people and gloves. The details on the model run can be found here: https://sway.office.com/d1TSLFNdzswF4MOb The model was not fully trained and did not perform well; further, the model was only implemented in the command line and the results have not been further continued down the coding pipeflow.</li>
  <li>The second part of the code is built in the python programming interface; Here, random instance generator is used to simulate detection of people and detection of gloves; if people are detected in the frame and gloves not detected, the model counts the instance. If the number of instances sequentially detected exceeds a threshold (threshold = 3), the code sends a notification. The code can be found in 02_smartxhealth_alert.py file. The binder launcher for the python file is: 
  </li>
  <li>The third part of the coding pipeline consists of an interactive prototype for the front-end (what the user sees); made in Figma. The link to the Figma interactive prototype is presented here: https://www.figma.com/proto/FCbdNjxBBKfy01QomLLaUz/Untitled?node-id=2%3A2&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=2%3A2
  </li>
  </ul>
  Project concept note can be found here: https://sway.office.com/aOTJhgcQWI4V5eJp?ref=Link <br>
  Project problem statement can be found here: https://sway.office.com/uQQ7MZBjEOOTyryn?ref=Link <br>
  Product canvas: https://github.com/mn5hk/smartxhealth_suraksha/blob/main/02%20pictures/03_canvas/01_product_canvas.jpeg <br>
  Progress indicator: https://github.com/mn5hk/smartxhealth_suraksha/blob/main/02%20pictures/03_canvas/02_progress_indicator.jpeg <br>
  Final presentation is available here: https://github.com/mn5hk/smartxhealth_suraksha/blob/main/Surakshya.pptx <br>



