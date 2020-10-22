from opentrons import containers, instruments, robot, labware


#Deck Slot 2 - tipracks A for each step

tiprack_2a = containers.load('tiprack-200ul', '2', 'tiprack_2a')



#Deck Slot 4 - MBL_3

MBL_3 = labware.load('point', '7', 'MBL_3')


#Deck Slot 8 - Square Well Block (deep well block)

square_wells = labware.load('96-deep-well', '8', 'square_wells')

#Deck Slot 9 - Chemical waste receptacle

chem_waste = labware.load('point', '9', 'chem_waste')




eight_pipettes = instruments.P300_Multi(
    tip_racks=[
        tiprack_2a,
    ],
    mount="left"
)





columns = ['1','2','3','4','5','6','7','8','9','10','11','12']


eight_pipettes.pick_up_tip()

for column in columns:
    eight_pipettes.transfer(200, MBL_3.wells('A1').top(-47), square_wells.cols(column).top(-35), new_tip='never')

eight_pipettes.drop_tip()




