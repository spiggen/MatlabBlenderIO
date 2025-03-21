import bpy, mathutils, numpy, os, shutil, time


def txt2obj(filepath, *args, **kwargs):

    replace = kwargs.get('replace', None)
    if replace == None: replace = True

    file               = open(filepath, 'r')
    data               = file.read()
    data               = data.split('\n')
    tracked_properties = ['position', 'attitude', 'mesh']
    is_number          = ['0','1','2','3','4','5','6','7','8','9']


    # loop through once to identify & create all the objects: _______________________________________
    for row in range(0, len(data)):
        
        is_address = not any((num in data[row]) for num in is_number )
        
        if is_address:
            address = data[row].split('.')
            
            is_body = (address[-1] in tracked_properties)

            if is_body:
                body_name    = address[-2]
                is_new_body  = not any(name == body_name for name in bpy.data.objects.keys())

                if replace and not is_new_body:
                    bpy.ops.object.select_all(action='DESELECT')
                    print(body_name)
                    bpy.data.objects[body_name].select_set(True)
                    children = bpy.data.objects[body_name].children
                    parent   = bpy.data.objects[body_name].parent
                    bpy.ops.object.delete()
                    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                    body           = bpy.data.objects['Empty']
                    body.name      = body_name
                    for child in children:
                        child.parent = body
                    bpy.data.objects[body_name].parent = parent


                if is_new_body:
                    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
                    body           = bpy.data.objects['Empty']
                    body.name      = body_name



    
    # loop through to assign all the properties: ____________________________________________________
    for row in range(0, len(data)):

        is_address = not any((num in data[row]) for num in is_number )
        
        if is_address:
            address = data[row].split('.')
            is_body = (address[-1] in tracked_properties)

            if is_body:
                is_position = (address[-1] == 'position')
                is_attitude = (address[-1] == 'attitude')
                is_mesh     = (address[-1] == 'mesh'    )
                body_name   =  address[-2]
                body        =  bpy.data.objects[body_name]


                if is_position:
                    number_of_frames = len(data[row+1].split(','))
                    positions        = numpy.zeros((3,number_of_frames))
                    
                    for dimension in range(0,3):
                        positions[dimension,:] = numpy.array(data[row+1+dimension].split(','),dtype='float')
                        
                    for keyframe in range(1,number_of_frames):
                        body.keyframe_insert('location', frame = keyframe)
                        body.location = mathutils.Vector(positions[:,keyframe-1])



                if is_attitude:
                    
                    number_of_frames = len(data[row+1].split(','))
                    
                    bpy.context.view_layer.objects.active = bpy.data.objects[body_name]
                    bpy.context.object.rotation_mode = 'QUATERNION'
                    
                    if number_of_frames > 1:
                        
                        attitudes        = numpy.zeros((9,number_of_frames))
                        
                        for dimension in range(0,9):
                            attitudes[dimension,:] = numpy.array(data[row+1+dimension].split(','),dtype='float')
                            
                        for keyframe in range(1,number_of_frames):
                            body.keyframe_insert('rotation_quaternion', frame = keyframe)
                            attitude = mathutils.Matrix(attitudes[:,keyframe-1].reshape(3,3))
                            attitude.transpose()
                            attitude = attitude.to_quaternion()

                            body.rotation_quaternion = attitude
                            
                    else:
                        attitude = numpy.zeros((3,3))
                        
                        for dimension in range(0,3): attitude[dimension,:] = numpy.array(data[row+1+dimension].split(','), dtype='float')    
                        
                        attitude = mathutils.Matrix(attitude)
                        attitude.transpose()
                        attitude = attitude.to_quaternion()
                        body.rotation_quaternion = attitude


                if is_mesh and replace:

                    mesh_name    = address[-2]

                    bpy.ops.object.select_all(action='DESELECT')
                    
                    try:
                        bpy.data.objects[mesh_name].select_set(True)
                        bpy.ops.object.delete()
                    except:
                        print("no objects replaced")
                    try:
                        bpy.data.objects[body_name].select_set(True)
                        bpy.ops.object.delete()
                    except:
                        print("no mesh replaced")

                    print("PRE____________________________")
                    print(filepath)
                    print(data[row+1])
                    print(data[row+1].split('\\'))
                    print(data[row+1].split('\\')[-1])
                    stl_filename       = data[row+1].split('\\')[-1]
                    txt_filename       = filepath   .split('\\')[-1]
                    stl_filepath       = filepath.replace(txt_filename, stl_filename)
                    print("POST___________________________")
                    print(stl_filename)
                    print(txt_filename)
                    print(stl_filepath)
                    # Testa att...
                    # Printa stl_filename och se om den är null
                    # Se vad som händer om ".stl" inte finns i stringen
                    import_name        = stl_filename.replace(".stl", "")

                    # Min gissning är att felet ligger i linen nedan
                    # Antagligen finns inte den filepathen
                    # Verkar som din filepath är "Trallgok.stl"
                    # Är detta rätt? Behövs inte typ "/mapp/gaksg/gaklsn/Trallgok.stl"?
                    bpy.ops.import_mesh.stl(filepath = stl_filepath)
                    
                    print(import_name)
                    bpy.data.objects[import_name].name = mesh_name


    ## Parent-assignment: ___________________________________________________________________________
    for row in range(0, len(data)):

        is_address = not any((num in data[row]) for num in is_number )
        
        if is_address:
            address    = data[row].split('.')
            
            is_body    = (address[-1] in tracked_properties)
            has_parent = (len(address) > 2)

            if is_body and has_parent:
                body_name   = address[-2]
                parent_name = address[-3]
                
                bpy.data.objects[body_name].parent = bpy.data.objects[parent_name]

    return data
