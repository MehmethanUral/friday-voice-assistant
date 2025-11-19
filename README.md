\# Friday - Python Voice Assistant 🎙️



Friday is a personalized voice assistant built with Python. It helps users manage tasks, control music, and search the web using voice commands. It uses the Serper API for real-time information and acts as a handy desktop companion.



\## 🚀 Features



\* \*\*Voice Interaction:\*\* Listens to commands and responds with voice (Text-to-Speech).

\* \*\*Task Management:\*\* Add, read, and clear tasks easily.

\* \*\*Web Search:\*\* Uses Google Serper API to answer questions like "Who is...", "What is...".

\* \*\*App \& Site Control:\*\* Opens Google, YouTube, X (Twitter), Instagram, and more.

\* \*\*Music Control:\*\* Plays welcoming music and specific tracks.

\* \*\*Special Modes:\*\* Includes a "Chess Mode" for focusing.



\## 🛠️ Installation



1\.  \*\*Clone the repository:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/yourusername/friday-voice-assistant.git](https://github.com/yourusername/friday-voice-assistant.git)

&nbsp;   cd friday-voice-assistant

&nbsp;   ```



2\.  \*\*Install dependencies:\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



3\.  \*\*Setup API Keys:\*\*

&nbsp;   \* Create a `.env` file in the root directory.

&nbsp;   \* Add your Serper API key:

&nbsp;       ```env

&nbsp;       SERPER\_API\_KEY=your\_api\_key\_here

&nbsp;       ```



\## 💻 Usage



Run the main script to start Friday:



```bash

python main.py




Example Commands:

"Wake up Friday"



"Google aç" (Open Google)



"Görev ekle" (Add task) -> Then say your task.



"Satranç modu" (Chess mode)



"Hava durumu nedir?" (What is the weather?)



"Kapat" (Exit)



📦 Technologies Used

Python 3.x



SpeechRecognition (for converting speech to text)



gTTS (Google Text-to-Speech)



Pygame (for audio playback)



Serper API (for Google search results)





