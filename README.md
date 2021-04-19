# cornerSpotter

### In a nutshell:
Internet of thing warning system for vechicles when travelling around tight corners.

## My initial plan:
The project vision is that a beacon situated on a tight corner will be able to warn a driver or a self driving vechicle about an oncoming obstacle if one exists.
The beacon will be equipped with its vision system and will be able to communicate with a oncoming vechicle that is in a way subscribed to an application.

The application inside the vechicle is assumed to have internet connection most of the time therefore all the data the car recieves from the beakon will be transmitted into the cloud where more analysis and decisions can be made.

The beacons and the application recievers inside the car must be scalable that it could pick up messages from each other without any major configurations

## The technology that (I think) must be used.
* Two raspberry pis for communication.
* Pi camere used for the vision system.
* RF 433 modules for communication.
* Tensor flow or open cv for object recognition.
* IFTT or things speak or a simmilar cloud platform to connect the devices.

## Project Graphics
![graphic](./images/ProjectGraphics.jpg)
#### Flow chart
![flowchart](./images/flow.jpg)