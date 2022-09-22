from .models import UserProfile, Student, Mentor, Preference


def create_preference_for_student_user(student_user):
    student_user_m = UserProfile.objects.get(id = student_user.id)
    print(type(student_user_m))
    student = Student.objects.get(user=student_user_m)
    print(student)
    #create valid Preferences for a user of type student
    mentors = Mentor.objects.all()
    print(mentors)
    #structure [[mentor_id, score]]
    mentor_and_score = []
    for mentor in mentors:
        if mentor.mentor_or_mentee != None:
            continue
        if mentor.faculty != student.faculty:
            continue
        #Initiliaze Score
        score = 0
        if mentor.gender == student.gender:
            score += 10
        if mentor.ethnicity == student.ethnicity:
            score += 5
        mentor_and_score.append([mentor.id, score])
    
    #Delete Existing Preference Records
    preferences = Preference.objects.filter(user=student_user_m).delete()

    print(mentor_and_score)
    #Create New Preference Records
    mentor_and_score.sort(reverse=True, key=lambda x: x[1])


    rank = 0
    for sorted_mentor_and_score in mentor_and_score:
        candidate = Mentor.objects.get(id=sorted_mentor_and_score[0])
        Preference.objects.create(user=student_user_m, candidate = candidate.user, rank=rank)
        rank += 1


def create_preference_for_mentor_user(mentor_user):
    mentor_user_m = UserProfile.objects.get(id = mentor_user.id)
    mentor = Mentor.objects.get(user=mentor_user_m)
    #get students
    students = Student.objects.all()
    student_and_score = []
    for student in students:
        if student.mentor_or_mentee != None:
            continue
        if student.faculty != mentor.faculty:
            continue

        #Initiliaze Score
        score = 0
        if mentor.gender == student.gender:
            score += 10
        if mentor.ethnicity == student.ethnicity:
            score += 5
        student_and_score.append([student.id, score])
    
    #Delete Existing Preference Records
    preferences = Preference.objects.filter(user=mentor_user_m).delete()

    print(student_and_score)
    #Create New Preference Records
    student_and_score.sort(reverse=True, key=lambda x: x[1])

    rank = 0
    for sorted_mentor_and_score in student_and_score:
        candidate = Student.objects.get(id=sorted_mentor_and_score[0])
        Preference.objects.create(user=mentor_user_m, candidate = candidate.user, rank=rank)
        rank += 1