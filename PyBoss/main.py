import os
import csv

#define function to retrieve state abbreviation

def stateShort(x):

    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }
    return us_state_abbrev.get(x)


inputPath = os.path.join('Resources', 'employee_data.csv')          #csv file to read
outputPath = os.path.join('Resources', 'employee_out.csv')          #csv file to write

#double loop on output file and input file
with open(outputPath, 'w', newline='') as csvNew:       
    with open(inputPath, mode='r') as csvOld:
        
        reader = csv.reader(csvOld)                                 #cursor for input file
        writer = csv.writer(csvNew,delimiter=',')                   #cursor for output file
        header = next(reader)                                       #skip header
        writer.writerow(["Empl_ID","First_Name","Last Name","DOB","SSN","State"])   #write header for output file

        for rows in reader:
            #do transformations for all fields
            empl_id = rows[0]
            full_name = rows[1].split()
            first_name = full_name[0]
            last_name = full_name[1]
            dob = rows[2][5:7] + '/' + rows[2][8:10] + '/' + rows[2][0:4]
            ssn = '***-**-' + rows[3][7:]
            state = stateShort(rows[4])
            writer.writerow([empl_id, first_name, last_name, dob, ssn, state])

csvNew.close()  #closing output file
