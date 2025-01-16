PI =  3.14159; 
R = float(input("Enter radius ")); 
H = float(input("Enter heigh ")); 

print("Volume of cylinder" + str(PI*R*R*H));
print("Surface area of cylinder with open top bottom elements %f " %(2*PI*R*H));
print("Surface area of cylinder with open top bottom elements %f " %(PI*R*R*(R+H)));

