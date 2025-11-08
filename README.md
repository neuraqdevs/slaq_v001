# voice_agent features implementation

## Setup and Running

1. Clone the repository and navigate to the project woeking directory (`/features`). 
working files `audio_processor.py` or create your own. <br />
NOTE : current changes are done under `analyzer` branch, use 
```d
git switch main
````

2. Create and activate a Python virtual environment:

```shell
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

````
3. Install dependencies:

```shell
pip install django numpy SpeechRecognition pydub
````
<!-- 4. Apply database migrations: -->
<!-- currently we dont use db -->

<!-- ```shell
python manage.py migrate
```` -->
4. Run the development server: before this ensure you installed FFmpeg ( The package we use now )

```shell
python manage.py runserver
````
---

## Notes ( For contribution )

- ### install FFmpeg <br />
<i>Install Chocolatey first (run as Administrator in PowerShell)</i>
```shell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
````

<i>Then install ffmpeg (run as Administrator in PowerShell)</i>

```shell
choco install ffmpeg
````

---

Developed by neuraq devs.
