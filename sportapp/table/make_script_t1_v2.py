# coding: utf-8
import os

def make_t1_2(context, methods):

    f = open(os.path.join(os.getcwd(), 'static', 't1_2.js'), "w")
    f.write('alert("trtrtrtr")\n')
    f.write("var tableObj = document.createElement('table');\n")
    f.write("tableObj.border = '1'\n")
    f.write("tableObj.style.width = '80%';\n")
    tableHTML = '<tr><td style="width: 50%; padding-bottom: 20px;">555</td><td style="padding-bottom: 20px;">666</td></tr>'
    f.write("var tableHTML = '" + tableHTML +"';\n")

    # TOP table
    tableHTML = "<tr>"
    tableHTML += '<td>N</td><td>ЧСС</td>'
    for meth in methods:
        tableHTML += "<td>"+str(meth.method_name)+"</td>"

    tableHTML += '<td>ИТОГО:</td><td>%</td>'
    tableHTML += "</tr>"

    f.write("tableHTML += '" + tableHTML + "';\n")


    f.write("for (var i = 1; i <= 10; i++){\n")
    tableHTML = '<tr><td>' + str(123) + '</td><td align="center">' + str(3342) + '</td></tr>'
    f.write("   tableHTML += '" + tableHTML + "';\n")
    f.write("}\n")

    f.write("tableObj.innerHTML = tableHTML;\n")
    f.write("document.body.appendChild(tableObj);\n")
    f.close()