from setuptools import find_packages, setup

setup(
    
    name = "multilingual assistant",
    version=0.0.1,
    author = "vsanth",
    author_email="kanva001@gmail",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition","pinwin","Pyaudio","gTTS","google-generativeai","python-dotenv","streamlit"
    ]
    
)