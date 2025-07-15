% 假设您的Simulink模型名为 'your_model_name.slx'
% 确保模型已保存并在当前路径下

% 运行Simulink模型
% 'out' 是 Simulink 默认的 SimulationOutput 对象
% sim('uwb_0');

% 检查 'out' 变量是否存在且是 Simulink.SimulationOutput 类型
if exist('out', 'var') && isa(out, 'Simulink.SimulationOutput')
    % 检查 out.sim_data 是否存在并且是 timeseries 类型
    % 这里的 'sim_data' 是 To Workspace 块在模型中配置的变量名
    if isprop(out, 'sim_data') && isa(out.sim_data, 'timeseries')

        % 从 timeseries 对象中获取数据
        data_values = out.sim_data.Data; % 这是您的信号数据
        time_values = out.sim_data.Time; % 这是对应的时间戳

        % 创建索引列 (从1开始)
        index_col = (1:length(data_values))';

        % 组合数据
        % 如果您的 data_values 是复数 (double (complex) from image_552091.png),
        % 那么您可能需要决定如何保存复数。
        % 通常，复数会保存为两列：Real Part 和 Imaginary Part。
        % CSV 文件不支持直接存储复数类型。

        % 检查数据是否为复数
        if isreal(data_values)
            output_table = table(index_col, data_values, 'VariableNames', {'Index', 'Data'});
        else
            % 如果是复数，保存实部和虚部
            real_part = real(data_values);
            imag_part = imag(data_values);
            output_table = table(index_col, real_part, imag_part, 'VariableNames', {'Index', 'RealPart', 'ImagPart'});
        end

        % 定义CSV文件名
        csv_filename = '../csv/simulink_output.csv';

        % 将数据写入CSV文件
        writetable(output_table, csv_filename);

        disp(['数据已成功保存到 ', csv_filename]);
    else
        disp('Simulink 输出变量 "out.sim_data" 未找到或不是 timeseries 类型。');
        disp('请检查 To Workspace 块的变量名和保存格式。');
    end
else
    disp('Simulink 仿真输出变量 "out" 未找到或类型不正确。');
    disp('请确保您的模型运行成功，并且其输出被正确记录。');
end