# Opentrons-Protocols
Programming the Opentrons OT-2 robot (opentrons.com) to run protocols (procedures) in biology labs.

# Genomic DNA from 200uL Blood Isolation.ipynb
## Introduction

This script was produced by Russell Tran for the [Guiyan Yan Lab](https://www.faculty.uci.edu/profile.cfm?faculty_id=5307) at UC Irvine. The Yan lab [studies](https://news.uci.edu/2017/04/27/9-6-million-grant-fuels-uci-malaria-control-research-in-africa/) the relationship between human-made environmental modifications (dams, irrigation, etc.) and malaria, and focuses on Kenya and Ethiopia.

The script uses the [Opentrons](http://opentrons.com/) OT-2 robotics platform to automate Machery-Nagel's ["Genomic DNA from Blood"](https://www.mn-net.com/Portals/8/attachments/Redakteure_Bio/Protocols/Genomic%20DNA/UM_gDNABlood_NMag200.pdf) protocol (procedure), published Dec 2015. In brief, the protocol uses various buffers and Machery-Nagel's NucleoMag magnetic beads to isolate DNA from a 200uL blood sample. Should the Yan lab decide to invest in an OT-2 robot, this script would help the lab cut down on the 4-5 hours of manual labor they report it takes them to complete the protocol once (for each 96 samples).

## Measurements / Notes for refining the robot's technique

(The protocol has been made to work with Qiagen troughs, though other troughs work too)

- The Qiagen 170 mL troughs have depth of about 52.5 mm, so going to 47 mm deep is a good idea
- The Qiagen 170 mL trough: 7mm height = 30 mL (RECTANGULAR PRISM VOLUME, not that of the trough indent on the bottom)
- Square_wells total depth from the top is 44 mm
- Square_wells meniscus 18 mm from bottom = 800 uL of volume (ratio is 0.0225 mm/uL)
- MBL_3 trough: 12 mm down is sufficient for first "drink" at 170 mL
- 80% Ethanol trough: 30 mm down down is sufficient for first "drink" at 80 mL

## Before starting the protocol:

- Check if Proteinase K was prepared according to section 3.
