'''
функція формування csv_файла власного CV
'''


def CV_csv(name: str, education: str, skills: list, **kwargs) -> None:

    '''

    :param name: Name
    :param education: Education
    :param skills: Skills
    :param kwargs: Contact Information
    :return:
    '''

    file_result = 'CV_csv.csv'

    result = "Name: \n" + name + '\n' + "Education: \n" + str(education) + '\n' + "Skills: \n" + str(skills) + '\n' + "Contact Information: \n" + str(kwargs)

    try:
        with open(file_result, 'w', encoding = "UTF-8") as f:
            f.write(result)

    except Exception as error:
        print(f"It looks like something has happened. This is {error}")



CV_csv(name = 'Stetsenko Anna', education = 'University', skills = ['Python', 'SQL'], adress = 'Kyiv', email = 'asdf@sdf')
