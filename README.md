# HandWriting Robot
Final Group Project for ECE387


## Project Members:
Sam Rutschilling, Brendan Moran, Deeparshan Khadka, and Michael Mattingly


# Introduction:

Our project is a handwriting robot for labels, it is designed to use a pen to write names or other text on to a label. This is to make more personable labels that have more depth and texture more similar to handwriting than labels printed by traditional printers.

The printer has a 3D printed frame with two 3D printed "carriages" for each axis (X and Y). The carriages for each axis are driven by stepper motors similar to a 3D printer. The carriages move back and forth on smooth, rigid plastic tubes desiged for use with cake decorating. Gears are printed into the design of the main body and X-Axis carriage for the stepper motors to interface with.

The Y-axis carriage, which is mounted to the X-axis carriage, contains the mount for the pen. The pen is controlled using a small 9-gram servo. The servo moves a small block vertically to determine if the pen is in contact with the surface of the paper. The pen holder is mounted to the Y-axis carriage using brass standoffs. Brass Standoffs also allow the pen holder to move freely.

As a group we used a Trello board to keep track of what tasks needed done, which were in progress, and which still needed completed.

# 3D printed parts

The body and mechanical parts of the pritner are constructed of 3D printed parts. These 3D parts were designed collaboratively using the cloud features of Autodesk Fusion 360. All of the 3D parts used in this project are located in this [Folder](https://github.com/rutschsr/ece387FinalGroupProject/tree/main/3-D%20printed%20parts). After the parts were desgined in Fusion 360 they were exported into the  stereolithography (.stl) format to be used by the slicer ([Utlimaker Cura](https://ultimaker.com/software/ultimaker-cura)). A slicer in the context of 3D printing takes a 3D model and sperates it into each of the layers that can be printed by a 3D printer. It then exports these layers in machine "g-code" that give the 3D printer specific instructions on where to move and how to place material. All of the 3D printed parts were printed using white or black PLA (polycactic acid) as shown below.

![PLA Filament](https://srutschilling.net/ECE387/ToyProject/Images/Filament.JPEG)

## Main Body

The main body of the printer is the largest piece of the project and includes several important design features. The first important design decision is the inclusion of a gap in the bottom of the frame, designed to allow the user to pass the piece of paper to be pritned through to the print area. The second important design detail is the inclusion of holes to hold the printer rods near the top. These were an important part to be 3D printed, as the 3D printing process allows keeping much more accurate dimensions than we could constructing by hand using materials such as wood. These are directly in line with each other so the rods stay parallel to each other. The final design detail that is important to note for this part, is the Gear located along the edge on one side. This was also the most difficult detail to include, as none of the members of our group are mechanical engineers and have little expierence modeling 3D parts the way it is. A Fusion 360 add on to produce rack gears helped with this process, however. 

![PLA Filament](https://github.com/rutschsr/ece387FinalGroupProject/blob/main/Pictures/IMG_4815.JPEG)

## X-Axis carriage

The X-Axis carriage is the next largest piece, 

![PLA Filament](https://github.com/rutschsr/ece387FinalGroupProject/blob/main/Pictures/IMG_4828.JPEG)

## Y-Axis carriage

## Servo Mount

## Pen Bracket

## Gears

# Electrical Parts

# Programming

# Demonstration

# Issues / Improvements

# Cost

Cost breakdown. Costs for 3D printed parts are estimated from the slicer's estimate of the filament required for printing. Based on $22 per 1kg (335m) spool of 1.75mm PLA. 3D printed parts do not consider the price of electricity used to construct.

| Part | Quantity | Cost | Note |
| --- | ----------- | --- | --- |
| Main Body | 1 | $4.67 | PLA |
| X-Axis carriage | 1 | $1.28 | PLA |
| Y-Axis carriage  | 1 | $1.67 | PLA |
| Pen Mount | 2 | $3.13 | PLA |
| Servo | 2 | $5.49 |  |
| X-Axis Stepper| 2 | $ |  |
| Y-Axis Stepper| 2 | N/A | Already Had |
| Limit Switches | 2 | $1.17 |  |
| Stepper Driver| 1 | $|  |
| Raspberry Pi | 1 | |  |
| 3D printed Gears | 1 | $0.24 | PLA |
| Brass Standoffs | N/A | $14.99 |  |
| Cake Rods | 4| $ |  |


Total: 


