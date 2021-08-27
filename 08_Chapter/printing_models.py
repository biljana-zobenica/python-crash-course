#import printing_functions as pf --> uvozi ceo printing_functions.py 
#(koji ne sme sadržati poziv funkcija u tom slučaju) 

from printing_functions import print_models, show_completed_models # uvoz samo funkcija iz fajla printing_funcitons.py

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models (unprinted_designs, completed_models)
show_completed_models (completed_models)