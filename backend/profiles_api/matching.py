from tokenize import group
from profiles_api.models import Student, Mentor, UserProfile, Preference
from profiles_api.gale_shapely import StableMatch

def get_valid_students_and_mentors() -> dict:
    students = Student.objects.filter(mentor_or_mentee = None)
    mentors = Mentor.objects.filter(mentor_or_mentee = None)
    return {"students" : students, "mentors": mentors}



std_mnt = get_valid_students_and_mentors()
#For Students, {"s1" : [m2,m3], s2: [m3,m2]}
std_preferences_dict = {}
for std in std_mnt['students']:
    std_preferences = std.user.preferences.all()
    std_preference_list = [Mentor.objects.get(user = std_preference.candidate).id for std_preference in std_preferences]
    std_preferences_dict[std.id] = std_preference_list

mnt_preferences_dict = {}
for mnt in std_mnt['mentors']:
    mnt_preferences = mnt.user.preferences.all()
    mnt_preference_list = [Student.objects.get(user = mnt_preference.candidate).id for mnt_preference in mnt_preferences]
    mnt_preferences_dict[mnt.id] = mnt_preference_list



#Min of std and mnt
n = min(len(std_preferences_dict), len(mnt_preferences_dict))

#If min is std
if len(std_preferences_dict) == n:
    """
    Remove Unnecessary Mentors
    """
    for key, value in std_preferences_dict.items():
        std_preferences_dict[key] = value[:n]

#if min is mnt
if len(mnt_preferences_dict) == n:
    #Create New Student Dict
    std_list = []
    for key, value in mnt_preferences_dict.items():
        mnt_preferences_dict[key] = value[:n]
        for val in value:
            if len(set(std_list)) != n:
                std_list.append(val)
    
    std_new_pref_dict = {}
    for std in std_list:
        std_new_pref_dict[std] = std_preferences_dict[std]
    
    std_preferences_dict = std_new_pref_dict


#Get Group 1 and Preference 1
group_1 = [str(key) for key in std_preferences_dict]
pref_1 = [[str(val) for val in value] for key,value in std_preferences_dict.items()]

#Get Group 2 and Preference 2
group_2 = [str(key) for key in mnt_preferences_dict]
pref_2 = [[str(val) for val in value] for key,value in mnt_preferences_dict.items()]


stable_match = StableMatch(n)
stable_match.get_grps(group_1, group_2)
stable_match.get_preference_grp1(pref_1)
stable_match.get_preference_grp2(pref_2)
stable_match.select_proposing_group(1)
stable_match.create_unmatched_list()
stable_match.create_current_partner_matrix()
stable_match.create_proposed_matrix()
result = stable_match.calculate_stable_match()
print(pref_1)
print(pref_2)
print(result)