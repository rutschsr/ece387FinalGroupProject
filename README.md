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

![Main Body](https://github.com/rutschsr/ece387FinalGroupProject/blob/main/Pictures/IMG_4815.JPEG)

## X-Axis Carriage

The X-Axis carriage is the next largest piece. The X-Axis carriage spans and slides on the cake rods supported by the main body. The X-Axis carriage also contains a mounting bracket for the stepper motor, and holes for more rods that the Y-Axis carriage mount to, as well as the gear for movement of the Y-Axis carriage.

![X-Axis Carriage](https://github.com/rutschsr/ece387FinalGroupProject/blob/main/Pictures/IMG_4828.JPEG)

## Y-Axis Carriage

The Y-Axis Carriage is much more simple and smaller than the other pieces. It just contains holes for the rods supported by the X-Axis carriage and a mount for a stepper motor. The Servo mount attatchs to the bottom of the carriage using brass standoffs.


## Servo Mount

The Servo mount attatchs to the bottom of the Y-Axis carriage and contains a mounting bracket for the small 9g servo, as well as mounting holes for the brass standoffs that the pen bracket moves vertically along. This piece proved problamatic as in the first version of the part the mounting brackets for the servo were undersized and snapped off whenever attatching the servo motor was attempted. Simply increasing the size of the mounting brackets remedied this situation.

## Pen Bracket

The pen bracket is a very simple piece, it is just a block that contains properly spaced holes to slide on the brass standoffs attatched to the bottom of the Servo mount as well as a hole for the pen or marker to be attatched to. Additionally, it has a cutout on one side for the servo arm to interact with and move.

![X-Axis Carriage](https://github.com/rutschsr/ece387FinalGroupProject/blob/main/Pictures/IMG_4900.JPEG)

The image above shows a print with the X-Axis carriage, Y-Axis Carriage, and servo mount. These pieces had to be reprinted to correct issues with them.

## Gears

The gears were the most difficult 3D printed component to design, as no one in the group was quite sure how to start with them. Another Fusion 360 plugin helped to create the gears, and some trial and error was used to determine the best size to use.

# Electrical Parts

# Programming

# Demonstration

[![Img alt text](https://img.youtube.com/vi/LLpY4BQX6XM/0.jpg)](https://www.youtube.com/watch?v=LLpY4BQX6XM)

# Issues / Improvements

One of the issues was with the hole sizing for the X and Y axis carriages. These parts were designed with holes where the diameter matched exactly the diameter of the rods. This meant that the fit was tight and there was no room for the parts to move back and forth. This was fixed by increasing the diameter of the holes in the 3D model and reprinting the affected parts.

# Cost

Cost breakdown. Costs for 3D printed parts are estimated from the slicer's estimate of the filament required for printing. Based on $22 per 1kg (335m) spool of 1.75mm PLA. 3D printed parts do not consider the price of electricity used to construct.

| Part | Quantity | Cost | Note |
| --- | ----------- | --- | --- |
| Main Body | 1 | $4.67 | PLA |
| X-Axis carriage | 1 | $1.28 | PLA |
| Y-Axis carriage  | 1 | $1.67 | PLA |
| Pen Mount | 2 | $3.13 | PLA |
| Servo | 2 | $5.49 |  |
| X-Axis Stepper| 2 | $13.99 |  |
| Y-Axis Stepper| 2 | N/A | Already Had |
| Limit Switches | 2 | $1.17 |  |
| Stepper Driver| 1 | $28.99|  |
| Raspberry Pi | 1 | |  |
| 3D printed Gears | 1 | $0.24 | PLA |
| Brass Standoffs | N/A | $14.99 |  |
| Cake Rods | 4 | $9.49 | Pack of 24 |


Total: 


