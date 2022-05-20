import os
import shutil
import time

# Pasta Raiz
folder_path = r'\\192.168.1.147\pronim\instaladores'
# Pasta PC
pc_path = rf'C:\PRONIM\instaladores'
# Senha do ADM
required_password = "!@C!sb@f!@7890"


# Mover arquivos para a pasta do Pronim
def to_move(shell, screen, folder, file):
    screen.pushButton.hide()
    try:
        shutil.copy(rf'{folder_path}\{folder}\{file}', rf'{pc_path}\{folder}')
        # Caso consiga, instalar
        print(f'{pc_path}\{folder}{file}')
        shell.Run(f"runas /user:CISBAF\Administrador {pc_path}\{folder}\{file}")
        time.sleep(1)
        shell.SendKeys(f"{required_password}\r\n", 0)

    except:
        screen.label_2.setText(f'Algum erro ao instalar, chame o suporte tecnico!')
    screen.pushButton.show()
    screen.label_2.setText(f'O arquivo de instalação foi inicializado!')
    screen.label_2.setStyleSheet('color: rgb(0, 115, 19);')
    screen.listWidget.setStyleSheet("QListView::item:selected"
                                       "{"
                                       "background : green;"
                                       "}")


# Listar todos os arquivos da pasta solicitada
def list_folder(folder):
    new_folder_path = f'{folder_path}\{folder}'
    files_all = []

    for root, dirs, files in os.walk(new_folder_path):
        for file in files:
            item = (f'{new_folder_path}\{file}')
            time_file = os.path.getmtime(item)
            convert_time = time.ctime(time_file)
            convert_time_string = time.strptime(convert_time)
            format_date = time.strftime("%d/%m/%Y", convert_time_string)

            files_all.append(f'{file}      {format_date}')
        return files_all
