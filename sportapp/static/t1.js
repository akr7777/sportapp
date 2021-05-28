var tabledata = [{'number': '1', 'rate': '>190', '18': ' 12 12 13 ', '19': ' 3 ', '20': ' 5 ', '21': ' 12 ', '22': ' ', '23': ' ', '26': ' ', 'h_rate_total': '57', 'rate_percent': '100.0%'}, {'number': '2', 'rate': '170-190', '18': ' ', '19': ' ', '20': ' ', '21': ' ', '22': ' ', '23': ' ', '26': ' ', 'h_rate_total': '0', 'rate_percent': '0.0%'}, {'number': '3', 'rate': '150-170', '18': ' ', '19': ' ', '20': ' ', '21': ' ', '22': ' ', '23': ' ', '26': ' ', 'h_rate_total': '0', 'rate_percent': '0.0%'}, {'number': '4', 'rate': '130-150', '18': ' ', '19': ' ', '20': ' ', '21': ' ', '22': ' ', '23': ' ', '26': ' ', 'h_rate_total': '0', 'rate_percent': '0.0%'}, {'number': '5', 'rate': '110-130', '18': ' ', '19': ' ', '20': ' ', '21': ' ', '22': ' ', '23': ' ', '26': ' ', 'h_rate_total': '0', 'rate_percent': '0.0%'}, {'number': ' ', 'rate': 'ИТОГО:', '18': '37', '19': '3', '20': '5', '21': '12', '22': '0', '23': '0', '26': '0', 'h_rate_total': '57', 'rate_percent': '100%'}, {'number': ' ', 'rate': '%', '18': '64.91%', '19': '5.263%', '20': '8.771%', '21': '21.05%', '22': '0.0%', '23': '0.0%', '26': '0.0%', 'h_rate_total': '100%', 'rate_percent': ' '}]

var table = new Tabulator("#myTable1", {
    height: 640,
    data: tabledata,
    layout: "fitColumns",
    tooltips: true,
 resizableRows: false,
 resizableColumns:false,
    columns: [{title: "N", field: "number", width: 25,},
    {title: "RATE", field: "rate",hozAlign: "left",width: 75, formatter: "textarea",},
    {title: "Бег", field: "18", hozAlign: "center", width: 120, editor: true, formatter: "textarea",},
    {title: "Лыжи (своб)", field: "19", hozAlign: "center", width: 120, editor: true, formatter: "textarea",},
    {title: "Лыжи (класс)", field: "20", hozAlign: "center", width: 120, editor: true, formatter: "textarea",},
    {title: "Лыжи (имит)", field: "21", hozAlign: "center", width: 120, editor: true, formatter: "textarea",},
    {title: "ОФП ОРУ", field: "22", hozAlign: "center", width: 120, editor: true, formatter: "textarea",},
    {title: "ОФП спец.", field: "23", hozAlign: "center", width: 120, editor: true, formatter: "textarea",},
    {title: "Плавание", field: "26", hozAlign: "center", width: 120, editor: true, formatter: "textarea",},
    {title: "TOTAL", field: "h_rate_total", sorter: "string", hozAlign: "left", width: 80,editor: false,},
    {title: "%", field: "rate_percent", sorter: "string", hozAlign: "left", width: 70, editor: false,},
    ],
cellEdited:function(cell){ 
var initial_value = cell.getInitialValue();var new_value = cell.getValue();var initial_len = initial_value.length;var new_len = new_value.length;var col_id = cell.getField();var row_name = cell.getRow().getCell("rate").getValue();if ((row_name != "ИТОГО:") && (row_name != "%")) {    if (new_len > initial_len) {        var value = new_value.slice(initial_len, new_len);        document.getElementById("transfer_text_area").value = value+";"+col_id+";"+row_name;        document.theForm.action = "/table/edit_table_by_user/"+value+"/"+col_id+"/"+row_name+"/"
        document.theForm.submit()
    } else {        alert("Непосредственно в таблице нельзя менять уже существующие значения");        cell.setValue(initial_value);    }} else {    alert("Нельзя менять последние строки");    cell.setValue(initial_value);}}, 
});
