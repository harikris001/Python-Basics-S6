import pandas as pd

topper_dict = {
    "Reg.No." : ['ABC123','ECH265','FET345','GNT734'],
    "Name" : ['Ganesh kumar','John Mathew' ,'Reena K', 'Adil M'],
    "Semester" : ['S8', 'S7', 'S6', 'S5'],
    "College" : ['ABC','ECH','FET','GMT'],
    "CGPA" : [9.8,9.9,9.7,9.75]
}

df = pd.DataFrame.from_dict(topper_dict)

pd.DataFrame.to_csv(df,"University_topper.csv")