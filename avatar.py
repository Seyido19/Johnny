def get_attribute(query,default):
    answer = input(query)
    if answer == "":
        answer = default
    print('You chose',answer)
    return answer


hair_color = get_attribute("What is the color of your hair?: ","Black")
hair_length = get_attribute("What is your hair length?[long or short]: ","Short")
eye_color = get_attribute("What is the color of your eyes?: ","Brown")
gender = get_attribute("Are you a male or female?: ","Male")
location = get_attribute("Where are you located?: ","Lagos, Nigeria")

print(f"You are a {eye_color} eyed {gender} with lovely {hair_length} {hair_color} hair. Living in {location}..")

