data = evalin('base', 'out.phase_noise_data_1.data');
time = evalin('base', 'out.phase_noise_data_1.time'); % Assuming time data is available
header = {'Time', 'Data'};
csvwrite_with_headers('phase_noise_data_1.csv', [time, data], header);

function csvwrite_with_headers(filename, data, header)
    % Write header
    fid = fopen(filename, 'w');
    fprintf(fid, '%s,%s\n', header{1}, header{2});
    fclose(fid);
    
    % Append data
    dlmwrite(filename, data, '-append');
end