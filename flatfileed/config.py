from pathlib import Path

#Name of used file
CSV_NAME = "test.csv"

#Path to folder
local_path = Path.cwd()

#Path to used locally CSV FILE
CSV_PATH = local_path / CSV_NAME

#test
SECRET_KEY = 'DEVEVE'

#Backup directory
BACKUP_DIR = local_path / "backup"

#Scp connection parameters
SCP_HOST, SCP_PORT = '192.168.1.26',22
SCP_LOGIN, SCP_PASSWORD = 'pi','szaman1'

#Scp remote direcotry with flat file
SCP_DIR = '/home/pi/flatfile_ed'

#Scp remote file name
SCP_CSV_NAME = 'scp_test.csv'