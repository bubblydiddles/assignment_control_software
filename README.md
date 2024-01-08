# Assignment Control Software

As part our application process, we'd like to see what you can produce by giving you an assignment to develop an application which processes sample data.

## Requirements
Your application must adhere to the following requirments
- Function as specified under Functionality
- Be hierarchical in nature. All major functions should be performed in subVIs 
- Use a state machine that either uses a type-defined enumerated control, queue, or Event structure for state management
- Be easily scalable to add more states/features without manually updating the hierarchy
- Minimize the use of excessive structures, variables (locals/globals) and property nodes
- Respond to front panel controls (within 100 ms) without utilizing 100 % of CPU time
- Close all opened references and handles where used
- Templates, examples, or code developed outside the bounds of this assignment are not acceptable for use in the application
- Git is a must, please make sure you commit your work throughout the process.

## Aplication setup
A lasertrain is controlled by GPS and 2 safety systems cosisting of 16 boolean sensors.
In the lps_interview project are 2 VI's. The mock server VI will generate mock data for you to process. 

Build your application in the template.vi 

The data from the gps is send over TCP on port 8081 with roughly 1 message per second.

The format of the message is: "*timestamp, lattitude, longitude*" and a carriage return marks the end of a message.

The data from the safety systems is send over TCP on port 8082 with roughly 10 messages per second. 
The values of these sensors are packed in a 32-bit unsigned int. The first 16 bits belong to safety system 1, the other 16 bits belong to safety system 2. End of message is marked by a carriage return.

## Functionality

On application start disable the start button and have the user fill in a speed threshold in km/h. This value must be greater then 1. When the user has filled in a correct value enable the start button.

Once the start button is pressed receive both the data from the GPS system and the safety system.

From the gps coordinates calculate the speed in km/h. Display the current coordinates and speed in the GPS cluster

If the speed is greater then the threshold arm the system.

Display the boolean values of the safety system sensors 

If the first 14 bits of its corresponding safety system are TRUE and bits 15 and 16 are FALSE and the system is armed by the GPS, set the laser to TRUE (laser1 and safety_system1, laser2 and safetysystem2). If one of these conditions is not met set the laser back to FALSE

If the sending server has stopped or no new messages are received for 2 seconds set both lasers to FALSE and disarm the system and wait for the server to start sending new messages.

## Delivery
To complete your work, please add `TimBerrier` as a contributer to your github repo when you're done, send an email to let us know. We will send you an invite to present your app.