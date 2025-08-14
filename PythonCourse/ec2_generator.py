from random import randint, choice
departments = ["DevOps", "HR", "Marketing"]
selected = choice(departments)
Number_of_EC2_instances = int(input('How many EC2 instances do you want names for?\n'))
Name_of_department = (input('What is the name of your Department?\n'))
def generate_ec2_names():
    Department = ["DevOps", "HR", "Marketing", "InfoSec", "FrontEnd"]
    dogs = ["Schnauzer", "Yorkie", "Greyhound", "Westie", "Labrador"]
    numbers = randint(1, 200)
    dogs = choice(dogs)
    return f"{Name_of_department}--{dogs}--instance--{numbers:03d}"
for i in range(Number_of_EC2_instances):
    print(generate_ec2_names())