# Setup MathForge on Windows
Set-Location -Path "..\backend"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

Set-Location -Path "..\frontend"
npm install
