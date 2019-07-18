def rev (x):
    rev =0
    while x:
        rev *= 10
        rev += x % 10
        x //= 10

a= rev(123)

######################################################################
#while x:
#In boolean, none zero value means 'true' and 0 means 'false'.
# The code reaches the argument while(0) or while(false) and terminate the body
######################################################################