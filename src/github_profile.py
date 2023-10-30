def generate_profile(theme , **kwargs):
    with open (f'src/themes/{theme}/profile.txt')as f :
        profile = f.read()
        for key, value in kwargs.items():
            with open (f'src/themes/{theme}/{key}.txt') as f:
                profile_item= f.read()

            profile_item = profile_item.replace(f'{{{{{key}}}}}',value)
            profile = profile.replace(f"{{{key}}}",value)
        return profile


if __name__ == '__main__':
    name ='sadaf rad'
    email = "sadafismaeili@gmail.com"
    phone = "+316"
    location = "netherlands"

    github = " sadaf_rad"
    linkedin = " sadaf"
    instagram = "sadafrad"
    youtube="sadaf rad"
    facebook = "sadaf rad"
    theme = 'default'
    profile = generate_profile(theme ,name=name , email=email , linkedin = linkedin )
    print(profile)
    

