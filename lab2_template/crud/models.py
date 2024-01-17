from django.db import models
from django.utils.timezone import now

# Define your models from here:

# User model
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)

    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " +  self.last_name
    
# Instructor model
class Instructor(User):
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self):
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "Is full time: " + str(self.full_time) + ", " + \
               "Total Learners: " + str(self.total_learners)
    
#Learner model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data scientist'
    DATABASE_ADMIN = 'dba'
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    # Occupation Char field with defined enumeration choices
    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    ) 
    social_link = models.URLField(max_length=200)

    #Create a __str__ method returning a string presentation
    #Create a toString method for object string representation

    def __str__(self):
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "Date of Birth: " + str(self.dob) + ", " + \
               "Ocupation: " + self.occupation + ", " + \
               "Social Link: " + self.social_link
    
# Course Model
class Course(models.Model):
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    # many to many relationships with instructor
    Instructors = models.ManyToManyField(Instructor)

    # many to many relationships with Learner via Enrollment relationship
    Learner = models.ManyToManyField(Learner, through = 'Enrollment' )

    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description " + self.description
    
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description

 
#lesson 
class Lesson(models.Model):
    title = models.CharField(max_length=200, default= "title")
    Course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

# Enrollment model as a lookup table with additional enrollment info 
class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]

    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)
