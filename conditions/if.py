import sys

type = sys.argv[1]

if type == "t2.medium":
    print("you can create the ec2 instance charge 2 dollars")
elif type == "t2.large":
    print("you can create the ec2 instance charge 4 dollars")
elif type == "t2.xlarge":
    print("you can create the ec2 instance charge 8 dollars")
else:
    print("Please check the instance type")