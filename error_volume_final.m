
function grid = create_grid(data)
    data_size = size(data);
    rows = data_size(1);
    cols = data_size(2);
    
    grid.F = zeros(rows, cols);
    for r=1:rows
        for c=1:cols
            grid.F(r,c) = data(r,c);
        end
    end
    grid.r = rows;
    grid.c = cols;
    
    grid.x = linspace(1, cols, cols);
    grid.y = linspace(1, rows, rows);
    
    [grid.X, grid.Y] = meshgrid(grid.x, grid.y);
    grid.padded = 0;
end

function grid = unpad_zeros(in_grid)
    if(in_grid.padded == 1)
        F = in_grid.F;
        grid.F = zeros(in_grid.r, in_grid.c);
        for r=2:in_grid.r+1
            for c=2:in_grid.c+1
                grid.F(r-1, c-1) = F(r,c);
            end
        end
        grid.x = linspace(1, in_grid.c, in_grid.c);
        grid.y = linspace(1, in_grid.r, in_grid.r);
        
        [grid.X, grid.Y] = meshgrid(grid.x, grid.y);
        grid.r = in_grid.r;
        grid.c = in_grid.c;
        grid.padded = 0;
    else
       grid = -1; 
    end
end

function grid = pad_zeros(in_grid)
    if(in_grid.padded == 0)
        F = in_grid.F;
        grid.F = zeros(in_grid.r+2, in_grid.c+2);
        for r=1:in_grid.r
            for c=1:in_grid.c
                grid.F(r+1, c+1) = F(r,c);
            end
        end
        grid.x = linspace(1, in_grid.c+2, in_grid.c+2);
        grid.y = linspace(1, in_grid.r+2, in_grid.r+2);
        
        [grid.X, grid.Y] = meshgrid(grid.x, grid.y);
        grid.r = in_grid.r;
        grid.c = in_grid.c;
        grid.padded = 1;
    else
       grid = -1; 
    end
end

function res = interploate(x1, x2, x3, x4)
    res = (x1+x2+x3+x4)/4;
end

function [volume, error_list, error, start, map, data] = error_calc(p_grid)
    valid = [];
    error_list = [];
    map = ones(p_grid.r, p_grid.c);
    map = create_grid(map);
    map = pad_zeros(map);
    
    for r=2:1+p_grid.r
        for c=2:1+p_grid.c
            valid = [valid; [r,c]];
        end
    end
    
    valid_size = size(valid);
    valid_size = valid_size(1);
    
    currVol = trapz(p_grid.y,trapz(p_grid.x,p_grid.F,2));
    while(valid_size > 5)
        rand_list = [];
        for i=1:10
           rand_i = randi(valid_size);
           rand_list = [rand_list, rand_i];
        end
        
        min_error = 9999999;
        min_index = -1;
        
        for i=1:10
           newF = p_grid.F(1:p_grid.r+2, 1:p_grid.c+2);
           x_pos = valid(rand_list(i),1);
           y_pos = valid(rand_list(i),2);
           
           interp_value = interploate(p_grid.F(x_pos+1, y_pos), ...
                                      p_grid.F(x_pos-1, y_pos), ...
                                      p_grid.F(x_pos, y_pos+1), ...
                                      p_grid.F(x_pos, y_pos-1));
           
           newF(x_pos,y_pos) = interp_value;
           newVol = trapz(p_grid.y,trapz(p_grid.x, newF,2));
           error = abs(newVol-currVol)/newVol;
           if( error < min_error)
              min_error = error;
              min_index = i;
           end
        end
        
        if(min_index ~= -1)
            x_pos = valid(rand_list(min_index),1);
            y_pos = valid(rand_list(min_index),2);
            
            map.F(x_pos, y_pos) = 0;
            
            
           interp_value = interploate(p_grid.F(x_pos+1, y_pos), ...
                                      p_grid.F(x_pos-1, y_pos), ...
                                      p_grid.F(x_pos, y_pos+1), ...
                                      p_grid.F(x_pos, y_pos-1));
                                  
           
           p_grid.F(x_pos, y_pos) = interp_value;
           finalVol = trapz(p_grid.y,trapz(p_grid.x,p_grid.F,2));
           error = abs(finalVol-currVol)/finalVol;
           error_list = [error_list, error];
           
           valid(rand_list(min_index), :) = [];
           valid_size = valid_size-1;
        end
        
        
    end
        
        
    volume = finalVol;
    start = valid_size;
    map = unpad_zeros(map);
    map = map.F;
    data = unpad_zeros(p_grid);
    data = data.F;
   
end

function res = error_volume_main(x,y,z)
    grid = create_grid(z);
    p_grid = pad_zeros(grid);
    [vol, errList, err, start, map, data] = error_calc(p_grid);
    
    res.error = err;
    res.volume = vol;
    res.data = data;
    res.map = map;
    res.error_list = errList;
    res.start_count = start;
end
