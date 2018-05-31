from django.db import models
from django.utils import timezone

class SectionLab(models.Model):
    """
    Model representing a section and lab
    """
    course_num = models.IntegerField(default=0, blank=True)
    class_id = models.CharField(max_length=999, blank=True)
    time = models.CharField(max_length=999, blank=True)
    instructor = models.CharField(max_length=999, blank=True)
    location = models.CharField(max_length=999, blank=True)
    enrollment = models.CharField(max_length=999, blank=True)
    wait = models.CharField(max_length=999, blank=True)
    status = models.CharField(max_length=999, blank=True)

    def __str__(self):
        return "Section for " + self.class_id 


class Course(models.Model):
    """
    Model representing a course.
    """

    title = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=999, blank=True)
    class_notes = models.CharField(max_length=999, blank=True)

    available_seats = models.IntegerField(default=0)
    career = models.CharField(max_length=99, blank=True)
    class_num = models.IntegerField(default=0, blank=True)
    credits = models.CharField(max_length=99, blank=True)
    enrolled = models.IntegerField(default=0)
    enrollment_capacity = models.IntegerField(default=0)
    general_education = models.CharField(max_length=99, blank=True)
    grading = models.CharField(max_length=99, blank=True)
    status = models.CharField(max_length=99, blank=True)
    type = models.CharField(max_length=99, blank=True)
    waitlist_capacity = models.IntegerField(default=0)
    waitlist_total = models.IntegerField(default=0)

    days_and_times = models.CharField(max_length=99, blank=True)
    instructor = models.CharField(max_length=99, blank=True)
    meeting_dates = models.CharField(max_length=99, blank=True)
    room = models.CharField(max_length=99, blank=True)

    section_and_labs = models.ForeignKey(SectionLab, on_delete=models.SET_NULL, null=True) 

    def __str__(self):
        return self.title

class Review(models.Model):
    """
    Model representing a Review
    """

    subject = models.CharField(max_length=300, blank=True)
    term = models.CharField(max_length=300, blank=True)
    course_title = models.CharField(max_length=300, blank=True)
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=300, blank=True)

    author = models.CharField(max_length=300, blank=True)

    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True)

    def __str__(self):
        return self.course_title + " review by " + self.author
    
    def save(self, *args, **kwargs):
        self.created = timezone.now()
        self.modified = timezone.now()
        return super(Review, self).save(*args, **kwargs)


