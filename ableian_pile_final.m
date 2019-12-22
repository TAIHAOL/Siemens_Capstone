%rows = 50;
%cols = 50;

%fill_points = [[20,20]];
%draw_points = [[30,30]];

%res = abelian_pile(fill_points, draw_points, [rows, cols], 4);

function res_out = abelian_pile(fill, draw, size_in, repose)
    rows = size_in(1);
    cols = size_in(2);
    
    fill_points = fill;
    draw_points = draw;
    fill_points_size = size(fill_points);
    draw_points_size = size(draw_points);  
    
    grid = zeros(rows, cols);
    
    for i=1:2000
       for fill_index=1:fill_points_size(1)
            %grid(fill_points(fill_index,1), fill_points(fill_index,2)) = grid(fill_points(fill_index,1), fill_points(fill_index,2)) + 1;
            x = -1;
            y = -1;

            while( x<1 || y<1 || x>cols || y>rows)
                rho = normrnd(0,1);
                phi = rand * 2 * pi;

                x = fill_points(fill_index,2) + rho*cos(phi);
                y = fill_points(fill_index,1) + rho*sin(phi);

                x = int8(x);
                y = int8(y);
            end

            grid(y, x) = grid(y,x) + 1;
       end
       for fill_index=1:draw_points_size(1)
            %grid(fill_points(fill_index,1), fill_points(fill_index,2)) = grid(fill_points(fill_index,1), fill_points(fill_index,2)) + 1;
            x = -1;
            y = -1;

            while( x<1 || y<1 || x>cols || y>rows)
                rho = normrnd(0,1);
                phi = rand * 2 * pi;

                x = draw_points(fill_index,2) + rho*cos(phi);
                y = draw_points(fill_index,1) + rho*sin(phi);

                x = int8(x);
                y = int8(y);
            end

            grid(y, x) = grid(y,x) - 1;
       end
       [grid, is_done] = process_pile(grid, repose);

    end

    p_grid = zeros(rows, cols);
    n_grid = zeros(rows, cols);

    for r=1:rows
        for c=1:cols
            if(grid(r,c) > 0)
                p_grid(r,c) = grid(r,c);
            elseif(grid(r,c) < 0)
                n_grid(r,c) = grid(r,c);
            end
        end
    end

    res_p = true_anti_derv(p_grid);
    res_n = -1*true_anti_derv(-1* n_grid);

    min_v_p = 999999;
    min_v_n = 999999;
    for r=1:rows
        for c=1:cols
            if(res_p(r,c) > 0 && abs(res_p(r,c)) < abs(min_v_p))
                min_v_p = abs(res_p(r,c));
            elseif(res_n(r,c) < 0 && abs(res_n(r,c)) < abs(min_v_n))
                min_v_n = abs(res_n(r,c));
            end
        end
    end

    for r=1:rows
        for c=1:cols
            if(res_p(r,c) > 0)
                res_p(r,c) = res_p(r,c) - min_v_p;
            elseif( res_n(r,c) < 0)
                res_n(r,c) = res_n(r,c) + min_v_n;
            end
        end
    end

    res = res_p + res_n;
    
    

    [X,Y] = meshgrid(1:cols, 1:rows);
    %surf(X,Y, res);
    
    res_out.x = X;
    res_out.y = Y;
    res_out.z = res;
end

function [new_grid, is_done] = process_pile(grid, max_slope)
    
    grid_size = size(grid);
    
    made_change = 1;
    while made_change == 1
        made_change = 0;
        for r=1:grid_size(1)
           for c=1:grid_size(2)
               if(grid(r,c) > max_slope)
                    made_change = 1;
                    grid(r,c) = grid(r,c)-4;
                    grid(r+1,c) = grid(r+1,c) + 1;
                    grid(r-1,c) = grid(r-1,c) + 1;
                    grid(r,c+1) = grid(r,c+1) + 1;
                    grid(r,c-1) = grid(r,c-1) + 1;
               elseif(grid(r,c) < -max_slope)
                    made_change = 1;
                    grid(r,c) = grid(r,c)+4;
                    grid(r+1,c) = grid(r+1,c) - 1;
                    grid(r-1,c) = grid(r-1,c) - 1;
                    grid(r,c+1) = grid(r,c+1) - 1;
                    grid(r,c-1) = grid(r,c-1) - 1;
               end
               
           end
        end
    end


    new_grid = grid;
    is_done = 0;
end



function res = anti_derv(data)
    
    data1 = [-ones(1,size(data,2)) ;flipud(data)];
    df = find([-1 ;diff((data1(:))>=0)] == 1)-1;
    data1(data1<0) =0;
    c1 = cumsum(data1(:));
    data1(df) = data1(df) - [0 ;diff(c1(df))];
    c2 = cumsum(data1(:));
    c2(data1==0)=0;

    c2=reshape(c2,size(data1));
    res = flipud(c2(2:end,:));
end

function res = true_anti_derv(grid)
    res90 = rot90((anti_derv(rot90(grid))),-1);
    res180 = rot90((anti_derv(rot90(grid, 2))),-2);
    res270 = rot90((anti_derv(rot90(grid,3))),-3);
    res = anti_derv(grid);
    
    res = res + res90 + res180 + res270;
    res = res/4;
end


