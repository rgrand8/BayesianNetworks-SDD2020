beliefs_exo = BN.predict_proba({'jewelry' : 'Yes', 'gas' : 'No', 'sex' : 'Female', 'age' : '>50'})
print('Fraud probability for a woman > 50 yo given Jewelry buyings :', beliefs_exo[0].items())