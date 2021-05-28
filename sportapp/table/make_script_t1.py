# coding: utf-8
import os

def make_t1(context, methods):
    f = open(os.path.join(os.getcwd(), 'static', 't1.js'), "w")
    f.write('var tabledata = ' + str(context) + '\n')
    f.write('\nvar table = new Tabulator("#myTable1", {\n')
    f.write('    height: 640,\n    data: tabledata,\n    layout: "fitColumns",\n    tooltips: true,\n resizableRows: false,\n resizableColumns:false,\n')
    f.write('    columns: [{title: "N", field: "number", width: 25,},\n')
    f.write('    {title: "RATE", field: "rate",hozAlign: "left",width: 75, formatter: "textarea",},\n')
    for meth in methods:
        f.write('    {title: "'+str(meth)+'", field: "'+str(meth.id)+'", hozAlign: "center", width: 120, editor: true, formatter: "textarea",},\n')
    f.write('    {title: "TOTAL", field: "h_rate_total", sorter: "string", hozAlign: "left", width: 80,editor: false,},\n')
    f.write('    {title: "%", field: "rate_percent", sorter: "string", hozAlign: "left", width: 70, editor: false,},\n')
    f.write('    ],\n')

    f.write('cellEdited:function(cell){ \n')

    f.write('var initial_value = cell.getInitialValue();')
    f.write('var new_value = cell.getValue();')
    f.write('var initial_len = initial_value.length;')
    f.write('var new_len = new_value.length;')
    f.write('var col_id = cell.getField();')
    f.write('var row_name = cell.getRow().getCell("rate").getValue();')

    #Проверка, не изменяет ли пользователь Последние две строки:
    f.write('if ((row_name != "ИТОГО:") && (row_name != "%")) {')
    #ЗДЕСЬ ФУНКЦИЯ ПРОВЕРКИ. ЕСЛИ ПОЛЬЗОВАТЛЬ удалил что-то и длина уменьшилась,
    #то всео отменяем!!! и возвращаем initial value.
    # если нет, то оставляем как есть и добавляем данные сегодняшним днем
    f.write('    if (new_len > initial_len) {')
    f.write('        var value = new_value.slice(initial_len, new_len);')
    f.write('        document.getElementById("transfer_text_area").value = value+";"+col_id+";"+row_name;')
    f.write('        document.theForm.action = "/table/edit_table_by_user/"+value+"/"+col_id+"/"+row_name+"/"\n')
    f.write('        document.theForm.submit()\n')
    f.write('    } else {')
    f.write('        alert("Непосредственно в таблице нельзя менять уже существующие значения");')
    f.write('        cell.setValue(initial_value);')
    f.write('    }')
    f.write('} else {')
    f.write('    alert("Нельзя менять последние строки");')
    f.write('    cell.setValue(initial_value);')
    f.write('}')


    f.write('}, \n')
    f.write('});\n')
    f.close()