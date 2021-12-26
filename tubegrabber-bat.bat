SETLOCAL
set app_path="C:\Users\GoonerLagoon\Projects\Tube Grabber"
set env_path=%app_path%\venv
set activate=%env_path%\Scripts\activate.bat
set req=%env_path%\requirements.txt
set app=%app_path%\tubeGrabber.py

%activate% && python -m pip install --upgrade pip && pip install -r %req% && python %app% & pause
ENDLOCAL
