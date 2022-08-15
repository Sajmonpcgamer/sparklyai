Invoke-WebRequest -Uri https://codeload.github.com/Sajmonpcgamer/sparklyai/zip/refs/heads/main -OutFile .\sparklyai.zip
Expand-Achive -Path sparklyai.zip -DestinationPath .\sparklyai
cd sparklyai\client
py -m pip install -r .\requirements.txt
py .
