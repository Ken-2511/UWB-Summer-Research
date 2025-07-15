% First, run your Simulink model.
% Replace 'uwb_0_8psk' with the actual name of your Simulink model file.
disp('正在运行 Simulink 模型: uwb_0_8psk...');
sim('uwb_0_8psk'); % Make sure your model is saved and in the current path.
disp('Simulink 模型运行完成。');

% --- Check for the 'out' variable from Simulink simulation ---
if exist('out', 'var')
    % --- Process decoded_data (assumed to be real) ---
    if isfield(out.decoded_data, 'signals') && isfield(out.decoded_data.signals, 'values')
        decoded_data_values = out.decoded_data.signals.values;

        % Ensure decoded_data_values is a column vector if it's a row vector
        if isrow(decoded_data_values)
            decoded_data_values = decoded_data_values';
        end

        % Create an index column (starts from 1)
        index_col_decoded = (1:size(decoded_data_values, 1))';

        % Create table for decoded data
        output_table_decoded = table(index_col_decoded, decoded_data_values, ...
                                     'VariableNames', {'Index', 'DecodedData'});

        % Define the CSV filename for decoded data
        csv_filename_decoded = '../csv/decoded_data.csv';

        % Create the directory if it doesn't exist
        [filepath_decoded, ~, ~] = fileparts(csv_filename_decoded);
        if ~isempty(filepath_decoded) && ~exist(filepath_decoded, 'dir')
            mkdir(filepath_decoded);
        end

        % Write the decoded data to the CSV file
        writetable(output_table_decoded, csv_filename_decoded);
        disp(['解码数据已成功保存到 ', csv_filename_decoded]);
    else
        disp('错误: Simulink 输出变量 "out.decoded_data.signals.values" 未找到或结构不正确。');
    end

    % --- Process demodulated_data (assumed to be complex) ---
    if isfield(out.demodulated_data, 'signals') && isfield(out.demodulated_data.signals, 'values')
        demodulated_data_values = out.demodulated_data.signals.values;

        % Ensure demodulated_data_values is a column vector if it's a row vector
        % This is important for consistency in table creation
        if isrow(demodulated_data_values)
            demodulated_data_values = demodulated_data_values';
        end

        % Create an index column (starts from 1)
        index_col_demodulated = (1:size(demodulated_data_values, 1))';

        % Extract real and imaginary parts
        real_part_demod = real(demodulated_data_values);
        imag_part_demod = imag(demodulated_data_values);

        % Create table for demodulated data
        output_table_demodulated = table(index_col_demodulated, real_part_demod, imag_part_demod, ...
                                         'VariableNames', {'Index', 'RealPart', 'ImagPart'});

        % Define the CSV filename for demodulated data
        csv_filename_demodulated = '../csv/demodulated_data.csv';

        % Create the directory if it doesn't exist (re-checking is safe, though it might exist from previous check)
        [filepath_demodulated, ~, ~] = fileparts(csv_filename_demodulated);
        if ~isempty(filepath_demodulated) && ~exist(filepath_demodulated, 'dir')
            mkdir(filepath_demodulated);
        end

        % Write the demodulated data to the CSV file
        writetable(output_table_demodulated, csv_filename_demodulated);
        disp(['解调数据已成功保存到 ', csv_filename_demodulated]);
    else
        disp('错误: Simulink 输出变量 "out.demodulated_data.signals.values" 未找到或结构不正确。');
    end

else
    disp('错误: Simulink 模型运行未能生成 "out" 结构体。');
    disp('请检查您的 Simulink 模型名称是否正确，以及是否配置了正确的 "To Workspace" 块以输出数据。');
end