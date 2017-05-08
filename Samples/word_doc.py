from docx import Document
from docxtpl import DocxTemplate
from docx.shared import Inches

import cx_Oracle
import os
#os.environ["NLS_LANG"] = "JAPANESE_JAPAN.JA16SJISTILDE"
os.environ["NLS_LANG"] = "Japanese_Japan.AL32UTF8"

agents = []

def make_word():
    document = DocxTemplate('tmpl/docx_tpl.docx')
    context = {'title' : "表領域使用量",
           'set_val' : "1000",
           'setidx_val' : "1200",
           'sethist_val' : "1300",
           }
    document.render(context)

    document.add_picture('images/taji.png', width=Inches(1.0))

    document.add_page_break()
    table = document.add_table(rows=1, cols=3, style=None)
    #table.style = 'Table Normal'
    hd_cells = table.rows[0].cells
    hd_cells[0].text = 'ID'
    hd_cells[1].text = '担当者コード'
    hd_cells[2].text = '担当者名'
    for agent in agents:
        row_cells = table.add_row().cells
        row_cells[0].text = str(agent[0])
        row_cells[1].text = str(agent[1])
        row_cells[2].text = str(agent[2])


    document.save('docx.docx')

def connect_oracle():
    tns = cx_Oracle.makedsn("10.6.2.197",1521,"SETORA")
    connection = cx_Oracle.connect("dynpt19","dynpt",tns)
    #connection = cx_Oracle.connect("dynpt19","dynpt","(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=10.6.2.197) (PORT=1521))(CONNECT_DATA=(SID=SETORA)))")
    cursor = connection.cursor()
    #agent_cd = '7'
    sql = """
        select user_id, agent_cd, agent_name
          from sys_user
        """
    cursor.execute(sql)
    #for agent in cursor:
    #    agents.append(agent)
    #    print(str(agent))

    rows = cursor.fetchall()
    for agent in rows:
        agents.append(agent)

if __name__ == '__main__':
    connect_oracle()
    make_word()
