# Voice Assistant

Small experiment with a voice-based interaction pipeline using a multimodal language model.

The application captures audio from the microphone, sends the recording to Google Gemini for processing, converts the generated response to speech, and plays the resulting audio back to the user.

## Workflow

```text
Microphone
    ↓
Audio recording
    ↓
Google Gemini
    ↓
Text response
    ↓
Edge TTS
    ↓
Audio playback
```

## Technologies

- Python
- Google Gemini
- Edge TTS
- SoundDevice
- SciPy
- Pygame

## Purpose

This project was created as a small experiment to explore multimodal interaction with LLMs, combining audio input, language model processing, and text-to-speech synthesis.
