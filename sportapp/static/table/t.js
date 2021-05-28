        var tabledata = [{'number': 12, 'rate': '>191', 'Бег': '30 11 13 14 15 16 17 18 19 20 ', 'Лыжи (своб)': '111 ', 'Лыжи (класс)': '', 'Лыжи (имит)': '', 'ОФП ОРУ': '', 'ОФП спец.': '', 'Плавание': '', 'h_rate_total': '284', 'rate_percent': '96.59%'}, {'number': 2, 'rate': '170-190', 'Бег': '', 'Лыжи (своб)': '', 'Лыжи (класс)': '', 'Лыжи (имит)': '10 ', 'ОФП ОРУ': '', 'ОФП спец.': '', 'Плавание': '', 'h_rate_total': '10', 'rate_percent': '3.401%'}]


        //var tdata1 = document.getElementById('label_ison').value
        //document.getElementById('label1').value = tabledata
        //var a = eval('({obj:[' + tdata1 + ']})');

        //alert("tdata1= " + typeof tdata1 + "; tabledata=" + typeof tabledata + "; a=" + typeof a);
        //alert("tdata1= " + typeof tdata1 + "; tabledata=" + typeof tabledata + "; a=" +  a);

        var table = new Tabulator("#myTable", {
            height: 500,
            data: tabledata,
            layout: "fitColumns",
            //pagination: "local",
            //paginationSize: 5,
            tooltips: true,
            columns: [{
                    title: "N",
                    field: "number",
                    width: 25,
                    sorter: "string",
                    //headerFilter: "input"
                }, {
                    title: "ЧСС",
                    field: "rate",
                    editor: true,
                    sorter: "string",
                    hozAlign: "left",
                    width: 75,
                },

                {% for meth in methods%}
                {
                    title: "{{meth}}",
                    field: "{{meth}}",
                    hozAlign: "center",
                    width: 100,
                    editor: true,
                },
                {%endfor%}

                {
                    title: "TOTAL",
                    field: "h_rate_total",
                    sorter: "string",
                    hozAlign: "left",
                    width: 80,
                    editor: true,
                },
                {
                    title: "percent",
                    field: "rate_percent",
                    sorter: "string",
                    hozAlign: "left",
                    width: 80,
                    editor: true,
                },
            ],


            cellEdited:function(cell){
              //alert("Значение: " + cell.getValue() + ";  столбец(параметр): " + cell.getField() +"; Строка(параметр): "+ cell.getData().playername)
              document.getElementById('textarea1').value = document.getElementById('textarea1').value +
               "\n" + cell.getField() + ";" + cell.getData().playername + ";" + cell.getValue()
              document.theForm.submit()
            },

            /*
            rowClick: function(e, row) {
                alert("Row " + row.getData().playerid + " Clicked!!!!");
            },
            */
        });
    </script>