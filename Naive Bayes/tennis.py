

# # Sunny,cool,high,strong

# #Outlook= sunny,temp:cool,humidity:high,wind:strong

# #P(Yes) = 9/14
# #P(No) = 5/14

# #Outlook
# ...........
#         P(Yes)          P(No)

# Sunny   2/9               3/5              


# Overcast  4/9              


# Rain     3/9                2/9


# #Temperature
# ...........
#             P(Yes)          P(No)

# Hot           2/9              2/5


# Mild          4/9             2/5


# Cool          3/9               1/5

# #Humidity
# ...........
#             P(Yes)          P(No)

# High           3/9           4/5


# Normal         6/9           1/5

# #Wind
# ...........
#             P(Yes)          P(No)

# Weak           6/9           2/5


# Strong         3/9           3/5

# ///////////////////////////////////////////////////

# #x=Outlook= sunny,temp:cool,humidity:high,wind:strong

# #P(Yes/x) = P(X/yes)*P(Yes)
#             # ...............
#             #     p(x)


#         # = P(outlook=sunny/yes)*P(temp=cool/Yes)*p(humidity=high/yes)*p(wind=strong/yes)*p(Yes)

#         # = 2/9*3/9*3/9*3/9*9/14= 0.005

# #P(No/x) = P(X/No)*P(No)
#             # ...............
#             #     p(x)


#         # = P(outlook=sunny/No)*P(temp=cool/No)*p(humidity=high/No)*p(wind=strong/No)*p(No)

#         # = 3/5*1/5*4/5*3/5*5/14= 0.020        

# #Yes = 0.005
# #NO = 0.20
