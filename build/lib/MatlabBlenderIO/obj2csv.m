function obj2csv(filename, obj, obj_path)
% Saves down an obj-struct with parameters position, attitude and/or mesh plus additional optinal parameters and child-sctructs to a .csv file.
    
    File = fopen(filename, 'w');
    
    path_elements = split(filename, "\");
    name = path_elements{end};
    name = split(name, ".");
    name = name{1};
    path = replace(filename, path_elements(end),"");
    
    fprintf(File, name);
    write_branches(name, obj);
    fprintf(File, ",,,,,\n");

    fclose(File);
    
        function write_branches(trace, branches)
            branch_names = fieldnames(branches);
            for branch_index = 1:numel(branch_names)
                branch_name = branch_names{branch_index};

                fprintf(File, ",,,,,\n");
                fprintf(File,trace+"."+branch_name);
                fprintf(File, ",,,,\n");

                is_meshpath = isequal(branch_name, "mesh");
                try struct(branches.(branch_name)); is_parent = true; catch; is_parent = false; end
                try double(branches.(branch_name)); is_matrix = true; catch; is_matrix = false; end
                try string(branches.(branch_name)); is_string = true; catch; is_string = false; end


                if is_meshpath
                    mesh_filename = split(branches.(branch_name), "\");
                    mesh_filename = mesh_filename{end};
                    if isequal(path, ""); path = "."; end
                    mesh_destination = path+mesh_filename;
                    mesh_origin = obj_path+branches.(branch_name);
                    if ~isequal(mesh_origin, mesh_destination); copyfile(mesh_origin, mesh_destination); end
                end
                %% Set priority-order by ordering the if-statements:
                if     is_parent;   write_branches(trace+"."+branch_name,                  branches.(branch_name) );
                elseif is_meshpath; fwrite        (File,                                   branches.(branch_name) );
                elseif is_matrix;   fprintf       (File,        matrix2csvtext(double(branches.(branch_name)),","));
                elseif is_string;   fprintf       (File,      replace(  string(branches.(branch_name)), "\", "\\"));
                else;               fprintf       (File,                                                 "MISSING");
                end
                
            end
    
    
        end
    end