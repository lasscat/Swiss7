from mojang import MojangAPI
print('ys////////////////////////////////////sy\nyo                                    oy\nyo                                    oy\nyo             oooooooooo             oy\nyo             yyyyyyyyyy             oy\nyo             yyyyyyyyyy             oy\nyo             yyyyyyyyyy             oy\nyo   ``````````yyyyyyyyyy``````````   oy\nyo   ssssssssssyyyyyyyyyyssssssssss   oy\nyo   yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy   oy\nyo   yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy   oy\nyo   yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy   oy\nyo   ``````````yyyyyyyyyy``````````   oy\nyo             yyyyyyyyyy             oy\nyo             yyyyyyyyyy             oy\nyo             yyyyyyyyyy             oy\nyo             oooooooooo             oy\nyo                                    oy\nyo                                    oy\nys////////////////////////////////////sy\n\n\n')
print('1) Username to uuid.\n2) Uuid to username.\n3)Username/Uuid to skin url.\n4) Username/uuid to cape.')
selection = input()
if selection=='3':
    username_or_uuid = input("Type 'user' to use username to find skin, or type uuid to find skin with your uuid")
    if username_or_uuid=='user':
        username_or_uuid_username = input("Enter your username")
        uuid_get = MojangAPI.get_uuid(username_or_uuid_username)
        profile_skin = MojangAPI.get_profile(uuid_get)                   
        print('The skin url is: ', profile_skin.skin_url)
    elif username_or_uuid=='uuid':
        uuid_input = input('Enter uuid: ')
        profile_skin_uuid = MojangAPI.get_profile(uuid_input)                
        print('The skin url is: ', profile_skin_uuid.skin_url)
     
if selection=='1':
    username_input = input('Enter your current minecraft username: ')
    uuid = MojangAPI.get_uuid(username_input)
    if not uuid:
        print("uuid is invalid")
    else:
        print('There uuid is: ' + uuid)

        
if selection=='2':
    uuid_input_2 = input('Enter the uuid: ')
    username = MojangAPI.get_username(uuid_input_2)
    print('The username is ' + username)

if selection=='4':
    username_or_uuid_cape = input("Type 'user' to use username to find skin, or type uuid to find skin with your uuid")
    if username_or_uuid_cape=='user':
        username_input_cape = input("Enter your username: ")
        uuid_get_cape = MojangAPI.get_uuid(username_input_cape)
        profile_cape = MojangAPI.get_profile(uuid_get_cape)
        print('The skin url is: ', profile_cape.cape_url)
    if username_or_uuid_cape=='uuid':
        uuid_input_cape = input('Enter the uuid: ')
        profile_cape = MojangAPI.get_profile(uuid_input_cape)
        print('The skin url is: ', profile_cape.cape_url)
        
        
    
    
