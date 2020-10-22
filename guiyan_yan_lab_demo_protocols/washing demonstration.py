from opentrons import containers, instruments, robot, labware


#Deck Slot 2 - tipracks A for each step

tiprack_2a = containers.load('tiprack-200ul', '2', 'tiprack_2a')
tiprack_3a = containers.load('tiprack-200ul', '2', 'tiprack_3a', share=True)


#Deck Slot 3 - tipracks B for each step




#Deck Slot 4 - MBL_3

MBL_3 = labware.load('point', '7', 'MBL_3')



#Deck Slot 8 - Square Well Block (deep well block)

square_wells = labware.load('96-deep-well', '8', 'square_wells')

#Deck Slot 9 - Chemical waste receptacle

chem_waste = labware.load('trough-12row', '9')





eight_pipettes = instruments.P300_Multi(
    tip_racks=[
        tiprack_2a,
        tiprack_3a,
    ],
    mount="left"
)




#trough_source - labware item to source washing fluid
#quantities_to_put_in - array that should add up to total volume want to put in,
#    but broken into 300 uL increments and smaller
#distances_when_putting_in - array whose length should be the same as quantities_to_put_in.
#    This is how many mm deep to go each time
def add_fluid(trough_source, 
              quantities_to_put_in,
              distances_when_putting_in
             ):
    
    columns = ['1','2','3','4','5','6','7','8','9','10','11','12']


    for column in columns: #for each column, use new pipette tips but keep looping until total qty dispensed for column.
                            # doesn't quite make sense in terms of: we should instead use new tips every *single* dispense.
    
        eight_pipettes.pick_up_tip()
    
        for quantity, distance in zip(quantities_to_put_in, distances_when_putting_in):

            eight_pipettes.move_to(trough_source, strategy = "arc")

            eight_pipettes.aspirate(quantity, trough_source)

            eight_pipettes.move_to(square_wells.cols(column).top(distance), strategy = "arc")
    
            eight_pipettes.dispense(quantity, square_wells.cols(column).top(distance))
    
        eight_pipettes.mix(repetitions=4, volume=300, location=square_wells.cols(column).top(-35), rate=1.0)
    
        eight_pipettes.drop_tip()
    

    
#quantities_to_take_out - array that should add up to total volume want to take out,    
#    but broken into 300 uL increments and smaller for finesse
#distances_when_taking_out - array whose length should be the same as quantities_to_take_out.
#    This is how many mm deep to go each time
def remove_supernatant(quantities_to_take_out, 
                       distances_when_taking_out):
    
    columns = ['1','2','3','4','5','6','7','8','9','10','11','12']
    
    for column in columns: #for each column, use new pipette tips but keep looping same tips until total qty removed for column.
                    
        eight_pipettes.pick_up_tip()
    
        for quantity, distance in zip(quantities_to_take_out, distances_when_taking_out):

            eight_pipettes.move_to(square_wells.cols(column).top(distance), strategy = "arc")

            eight_pipettes.aspirate(quantity, square_wells.cols(column).top(distance))

            eight_pipettes.move_to(chem_waste['A1'].top(), strategy = "arc")
    
            eight_pipettes.dispense(quantity, chem_waste['A1'].top())
        
        
        eight_pipettes.drop_tip()




# add 300 uL MBL_3 @ top-31 then mix 5 times (changed mix in function)

add_fluid(trough_source = MBL_3.wells('A1').top(-47), 
          quantities_to_put_in = [300],
          distances_when_putting_in = [-31]
         )


# demonstrate box replacement

robot.comment("MESSAGE: ROBOT HAS BEEN PAUSED. PLEASE REPLACE TIP RACKS BEFORE CONTINUING")
robot.pause()


# remove 400 uL supernatant

remove_supernatant(quantities_to_take_out = [100, 300], 
                       distances_when_taking_out = [-34.5, -42])