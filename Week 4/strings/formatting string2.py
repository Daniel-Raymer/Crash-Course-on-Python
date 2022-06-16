price = 7.5
with_tax = price * 1.09

print (price, with_tax) #printing variables

print ("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

#{:.2f} is a formatting expression
#expressions are needed when we want to tell python to tell our values that
#are different from the default