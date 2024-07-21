import assemblyai as aai

aai.settings.api_key = "46de903eec3e48c6858df556aa1b3518"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("video.mp4")

print(transcript.text)
subtittles = transcript.export_subtitles_srt()

f = open("subtittles.srt","a")
f.write(subtittles)
f.close