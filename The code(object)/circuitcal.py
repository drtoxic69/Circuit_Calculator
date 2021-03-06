import sys

class calculator:    
    # The instruction 
    print('When you have to enter multiple values you have to enter with a space.')
    print('For example you have to enter 4 and 2 then you should enter like this: 4 2')
    print()

    # The values
    def __init__(self):
        self.connected = input('What is the circuit connected in? [S]eries or [P]arallel or [M]ixed: ')        
        self.ask_which_one = input('Which is not given? [C]urrent or [V]oltage: ')

        if self.ask_which_one.lower() == 'c':
            self.voltage = float(input('Enter the voltage of the battery: '))
            self.current = 'not given'

        elif self.ask_which_one.lower() == 'v':
            self.current = float(input('Enter the current flowing to the circuit: '))
            self.voltage = 'not given'
            
        else:
            sys.exit('You had to type c or v!')
        
    
    # The number of resistors in a circuit of series and parallel
    def numOfResistors(self):
        if self.connected.lower() == 's' or self.connected.lower() == 'p':
            global num_resistor

            try:
                num_resistor = int(input('Enter the no. resistors in the circuit: '))
            except ValueError:
                sys.exit('Invalid Input! You had to type a whole number!')
                
            if num_resistor == 1:
                calculator.numOfResistors.single_value = float(input('Enter the value of the resistor: '))
                return calculator.numOfResistors.single_value

            elif num_resistor > 1: 
                calculator.numOfResistors.multiple_value = list(map(float, input('Enter the values of the resistors: ').split()))
                return calculator.numOfResistors.multiple_value

            elif num_resistor == 0:
                sys.exit('To run this command you need atleast one resistor. (Your device connected will have resistance) ')

            
    # The calculation for a series circuit
    # The outputs of the series calculation
    def seriesCalculation(self):
        if self.connected.lower() == 's':

            print('_' * 84)
            print('')
            
            if self.ask_which_one.lower() == 'c':

                if num_resistor == 1:
                    print(f'The R(eq) of the circuit: {calculator.numOfResistors.single_value} ohms')

                elif num_resistor > 1:
                    print(f'The R(eq) of the circuit: {sum(calculator.numOfResistors.multiple_value)} ohms')

                if self.current.lower() == 'not given':
                    if num_resistor == 1:
                        self.current = self.voltage/calculator.numOfResistors.single_value
                        print(f'The I(ckt): {self.current} A')

                    elif num_resistor > 1:
                        self.current = self.voltage/sum(calculator.numOfResistors.multiple_value)
                        print(f'The I(ckt): {self.current} A')
                    print(f'I(ckt) = I(r1) = I(r2) = ... = {self.current} A')

                    if num_resistor == 1:
                        print(f'The voltage of the resistor: {calculator.numOfResistors.single_value*self.current} V')

                    elif num_resistor > 1:
                        for value_resistor in calculator.numOfResistors.multiple_value:
                            print(f'The voltage of the resistor: {value_resistor*self.current} V')

            elif self.ask_which_one.lower() == 'v':
                
                if num_resistor == 1:
                    print(f'R(eq) of the circuit: {calculator.numOfResistors.single_value} ohms')

                elif num_resistor > 1:
                    print(f'R(eq) of the circuit: {sum(calculator.numOfResistors.multiple_value)} ohms')

                if self.voltage.lower() == 'not given':
                    if num_resistor == 1: 
                        self.voltage = self.current*calculator.numOfResistors.single_value
                        print(f'The V(b): {self.voltage} V')

                    elif num_resistor > 1:
                        self.voltage = self.current*sum(calculator.numOfResistors.multiple_value)
                        print(f'The V(b): {self.voltage} V')
                    print(f'V(r1) + V(r2) + ... = {self.voltage} V')

                
    # The calculations for a parallel circuit
    # The outputs of the parallel circuit
    def parallelCalculation(self):    
        if self.connected.lower() == 'p':
            print('_' * 84)
            print()

            if num_resistor == 1:
                sys.exit('Invalid input! if there is one resistor in a circuit then it is a series circuit!')
            
            elif num_resistor > 1:
                global Req
                Req = 0
                for req in calculator.numOfResistors.multiple_value:
                    Req += 1/req
                print(f'The R(eq): {1/Req} ohms')

            # The calculation of current and voltage in parallel
            if self.ask_which_one.lower() == 'c':
                if self.current.lower() == 'not given':
                    self.current = self.voltage/(1/Req)
                    print(f'The I(ckt): {self.current} A')
                    print(f'V(b) = V(1) = V(2) = ... = {self.voltage} V')

                    for current_resistor in calculator.numOfResistors.multiple_value:
                            print(f'The current of the resistor: {self.voltage/current_resistor} A')


            elif self.ask_which_one.lower() == 'v':
                self.voltage = self.current*(1/Req)
                print(f'The V(b) = {self.voltage} V')
                print(f'V(b) = V(1) = V(2) = ... = {self.voltage} V')
                print(f'The I(ckt): {self.current} A')
                
                for current_resistor in calculator.numOfResistors.multiple_value:
                    print(f'The current of the resistor: {self.voltage/current_resistor} A')
    

    # Step by step 
    def stepByStep(self):
        step_by_step = input('Do you want the answer step by step? (Y/N) ')
        
        # The step by step for series
        if self.connected.lower() == 's':
            if self.ask_which_one.lower() == 'c':
                if step_by_step.lower() == 'y':
                    if num_resistor > 1:
                        print(f'''
{'='*84}

[*note: please draw the circuit yourself]
R(eq) = R(1) + R(2) + ... + R(n)
      = {sum(calculator.numOfResistors.multiple_value)} ohms
        
I(ckt) = V(b)/R(eq) [By Ohm's law]
       = {self.current} A

I(ckt) = I(r1) = I(r2) = ... = I(n) = {self.current} A [current is same to all devices when connected in series]
''')

                        for value_resistor in calculator.numOfResistors.multiple_value:
                            print(f'''
V = IR [By Ohm's law]
  = {self.current} x {value_resistor}
  = {value_resistor*self.current} V
                        ''')

                        sys.exit('Thank you and have a nice day :) ') 
						
                    elif num_resistor == 1:
                        print(f'''
{'='*84}

[*Note: draw the circuit yourself]
R(eq) = R1 + R2 + ... + Rn
      = {calculator.numOfResistors.single_value} ohms

I(ckt) = V(b)/R(eq) [By Ohm's law]
       = {self.current} A
I(ckt) = I(r1) = I(r2) = ... =I(n) = {self.current} A

V = IR [By Ohm's law]
  = {self.current} x {calculator.numOfResistors.single_value}
  = {self.current*calculator.numOfResistors.single_value} V

                    ''')
                        sys.exit('Thank you and have a nice day :)')
                else:
                    sys.exit('Ok then, have a nice day!')

            elif self.ask_which_one.lower() == 'v':
                if step_by_step.lower() == 'y':
                    if num_resistor > 1:
                        print(f'''
{'='*84}

[*Note: PLease draw the circuit yourself]
R(eq) = R(1) + R(2) + ... + R(n)
      = {sum(calculator.numOfResistors.multiple_value)} ohms

V(b) = I(ckt) x R(eq) [by ohms law]
     = {self.current} x {sum(calculator.numOfResistors.multiple_value)}
     = {self.current*sum(calculator.numOfResistors.multiple_value)} V

I(ckt) = I(r1) = I(r2) = ... = {self.current} A
                        ''')
                        for value_resistor in calculator.numOfResistors.multiple_value:
                            print(f'''
V = IR [By Ohm's law]
  = {self.current} x {value_resistor}
  = {value_resistor*self.current} V
                        ''')
                    
                    elif num_resistor == 1:
                        print(f'''
{'='*84}

[*Note: draw the circuit yourself]
R(eq) = R1 + R2 + ... + Rn
      = {calculator.numOfResistors.single_value} ohms

V(b) = I(ckt) x R(eq) [by ohms law]
     = {self.current} x {calculator.numOfResistors.single_value}
     = {self.current*calculator.numOfResistors.single_value} V

I(ckt) = I(r1) = I(r2) = ... = {self.current} A

V = IR [By Ohm's law]
  = {self.current} x {calculator.numOfResistors.single_value}
  = {self.current*calculator.numOfResistors.single_value} V
                        ''')
                
                else:
                    sys.exit('Ok, then have a nice day.')


        # Parallel step-by-step
        elif self.connected.lower() == 'p':
            if self.ask_which_one.lower() == 'c':
                if step_by_step.lower() == 'y':
                    print(f'''
{'='*84}

[*Note : PLease draw the circuit yourself]
1/R(eq) = 1/R(1) + 1/R(2) + ... + 1/R(n)
  R(eq) = {1/Req} ohms

I(ckt) = V/R(eq) [by Ohms law]
       = {self.voltage} / {1/Req}
       = {self.current} A

V(b) = V(r1) = V(r2) = ... = {self.voltage} V
                ''')
                    for value_resistor in calculator.numOfResistors.multiple_value:
                            print(f'''
I = V/R [By Ohm's law]
  = {self.voltage} / {value_resistor}
  = {self.voltage/value_resistor} A
                        ''')
                    sys.exit('Thank you and have a nice day :)')
            
                elif step_by_step.lower() == 'n':
                    sys.exit('Ok then, have a nice day!')

            elif self.ask_which_one.lower() == 'v':
                if step_by_step.lower() == 'y':
                    print(f'''
{'='*84}

[*Note: PLease draw the circuit yourself]
1/R(eq) = 1/R(1) + 1/R(2) + ... + 1/R(n)
  R(eq) = {1/Req} ohms

V(b) = I(ckt) x R(eq) [by Ohms law]
     = {self.current} x {1/Req}
     = {self.voltage} V

V(b) = V(r1) = V(r2) = ... = {self.voltage} V
                    ''')
                    for value_resistor in calculator.numOfResistors.multiple_value:
                            print(f'''
I = V/R [By Ohm's law]
  = {self.voltage} / {value_resistor}
  = {self.voltage/value_resistor} A
                        ''')
                    sys.exit('Thank you and have a nice day :)')

                else:
                    sys.exit('Invalid Input! you had to input y or n')
        
        
        # step by step for mixed

        elif self.connected.lower() == 'm':
            if step_by_step.lower() == 'y':
                if self.ask_which_one.lower() == 'c':
                    print('''
{'='*84}
[*Note: Please draw the circuit yourself]

                            ''')
    

    # Calculations for the mixed circuit
    # The outputs of the mixed circuit

    def mixedCalculation(self):
        if self.connected.lower() == 'm':
            sets_of_resistors = int(input('Enter the number of sets in the circuit: '))
            print()
            
            values_for_step_by_step = {} 
            
            req_of_sets = {}
            values_of_resistors = {}
            for sets in range(sets_of_resistors):
                input_of_top_resistors = list(map(float, input(f'Enter the value of resistor(s) in top of set {sets+1}: ').split()))
                req_of_sets[f'top_{sets+1}'] = sum(input_of_top_resistors)
                
                input_of_bottom_resistors = list(map(float, input(f'Enter the value of resistor(s) in bottom of set {sets+1}: ').split()))
                req_of_sets[f'bottom_{sets+1}'] = sum(input_of_bottom_resistors)
                
                values_of_resistors[f'set_{sets+1}'] = {f'top_{sets+1}' : input_of_top_resistors, f'bottom_{sets+1}' : input_of_bottom_resistors}
                print()
            
            import numpy as np

            Req_mixed_sets = sum(list(np.reciprocal([float(i) for i in list(req_of_sets.values())])))
            mixed_series_resistors = list(map(float, input('Enter the value of the series resistor(s): ').split()))
            values_of_resistors['series_resistors'] = mixed_series_resistors
            values_for_step_by_step['parallel_sets'] = values_of_resistors.copy()
            values_for_step_by_step['parallel_sets'].popitem()
            values_for_step_by_step['series_sets'] = mixed_series_resistors

            print('_'*84)
            print()
            
            Req_mixed = Req_mixed_sets + sum(mixed_series_resistors)
            values_for_step_by_step['Req_mixed'] = Req_mixed
            print(f'The R(eq) of the circuit: {Req_mixed}')

            if self.ask_which_one.lower() == 'c':
                self.current = self.voltage/Req_mixed
                print(f'The I(ckt): {self.current} A')
                print(f'I(ckt) = I(r1) = I(set_1) = ... = {self.current} A')
                print()
                
            elif self.ask_which_one.lower() == 'v':
                self.voltage = self.current*Req_mixed
                print(f'The V(b) of the circuit: {self.voltage} V')
                print(f'I(ckt) = I(r1) = I(set_1) = ... = {self.current} A')
                print()
            
            values_for_step_by_step['voltage_circuit'] = self.voltage
            values_for_step_by_step['current_circuit'] = self.current
            
            for sets in range(sets_of_resistors): 
                sets_value = values_of_resistors.get(f'set_{sets+1}')
                Req_set_top = sum(sets_value.get(f'top_{sets+1}'))
                Req_set_bottom = sum(sets_value.get(f'bottom_{sets+1}'))
                Req_set = (1/Req_set_top) + (1/Req_set_bottom)
                values_for_step_by_step[f'Req_set_{sets+1}_top'] = Req_set_top
                values_for_step_by_step[f'Req_set_{sets+1}_bottom'] = Req_set_bottom
                values_for_step_by_step[f'Req_set_{sets+1}'] = Req_set 
                values_for_step_by_step[f'Voltage_set_{sets+1}'] = self.current * Req_set
                values_for_step_by_step[f'current_top_set_{sets+1}'] = (self.current * Req_set)/Req_set_top
                values_for_step_by_step[f'current_bottom_set_{sets+1}'] = (self.current * Req_set)/Req_set_bottom

                print(f"Req of the top of set_{sets+1} = {Req_set_top} ohms")
                print(f"Req of the bottom of set_{sets+1} = {Req_set_bottom} ohms")
                print(f'Req of set_{sets+1} = {Req_set} ohms')
                print(f'The voltage of set_{sets+1} = {self.current * Req_set} V')
                print(f'Current of top of set_{sets+1} = {(self.current * Req_set)/Req_set_top} A')
                print(f'Current of bottom of set_{sets+1} = {(self.current * Req_set)/Req_set_bottom} A')
                print(f'I(set_{sets+1}) = I(top_r1) = I(top_r2) = ... = {(self.current * Req_set)/Req_set_top} A \n')

                sets_resistors_top_value = sets_value.get(f'top_{sets+1}')
                sets_resistors_bottom_value = sets_value.get(f'bottom_{sets+1}')
                
                for count, resistor in enumerate(sets_resistors_top_value, start=1):
                    print(f'The voltage of resistor{count} on top of set_{sets+1} = {((self.current * Req_set)/Req_set_top) * resistor} V')
                    values_for_step_by_step[f'resistor_{count}_voltage_parallel_set_{sets+1}_top'] = ((self.current * Req_set)/Req_set_top) * resistor
                print()
                

                for count, resistor in enumerate(sets_resistors_bottom_value, start=1):
                    print(f'The voltage of resistor on bottom of set_{sets+1} = {((self.current * Req_set)/Req_set_bottom) * resistor} V')
                    values_for_step_by_step[f'resistor_{count}_voltage_parallel_set_{sets+1}_bottom'] = ((self.current * Req_set)/Req_set_bottom) * resistor
                print()
                
            for count, series_resistors in enumerate(values_of_resistors.get('series_resistors'), start=1):            
                print(f'The voltage of the series resistor = {self.current * series_resistors} V')
                print(f'The current of the series resistor = {self.current} A\n')
                values_for_step_by_step[f'voltage_of_series_resistor_{count}'] = self.current * series_resistors
                values_for_step_by_step[f'current_of_series_resistor_{count}'] = self.current
            
            print(values_for_step_by_step)



c = calculator()
c.numOfResistors()
c.seriesCalculation()
c.parallelCalculation()
c.mixedCalculation()
c.stepByStep()
