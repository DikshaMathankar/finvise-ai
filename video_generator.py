import os
import re
import textwrap
from pathlib import Path
from gtts import gTTS
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import numpy as np

TMP = Path("/tmp/finvise")
TMP.mkdir(exist_ok=True)
W, H = 1280, 720

def make_frame(title, body, idx):
    img = Image.new("RGB", (W, H), (10, 14, 26))
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0,0),(W,6)], fill=(0,255,135))
    try:
        font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_med = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        font_sm  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font_big = font_med = font_sm = ImageFont.load_default()
    draw.text((60, 40), f"[{idx}] {title}", font=font_big, fill=(0,255,135))
    draw.line([(60,90),(W-60,90)], fill=(31,41,55), width=1)
    lines = textwrap.wrap(body, width=60)
    for i, line in enumerate(lines[:10]):
        draw.text((60, 110 + i*46), line, font=font_med, fill=(249,250,251))
    draw.rectangle([(0,H-50),(W,H)], fill=(17,24,39))
    draw.text((60, H-35), "FinVise AI - Indian Stock Intelligence", font=font_sm, fill=(107,114,128))
    return np.array(img)

def parse_sections(script):
    parts = [s.strip() for s in re.split(r'\n\n+', script) if s.strip()]
    if not parts:
        parts = [script]
    return parts

def create_video(script, ticker="STOCK"):
    try:
        audio_path = str(TMP / "voice.mp3")
        gTTS(text=script, lang="en", tld="co.in").save(audio_path)
        audio = AudioFileClip(audio_path)
        total = audio.duration
        parts = parse_sections(script)
        dur_each = total / len(parts)
        labels = ["HOOK","SNAPSHOT","HAPPENING","TAKEAWAY","CTA"]
        clips = []
        for i, part in enumerate(parts):
            label = labels[i] if i < len(labels) else f"PART {i+1}"
            frame = make_frame(label, part[:300], i+1)
            clips.append(ImageClip(frame).set_duration(dur_each))
        video = concatenate_videoclips(clips, method="compose")
        video = video.set_audio(audio)
        out = str(TMP / f"{ticker}.mp4")
        video.write_videofile(out, fps=24, codec="libx264", audio_codec="aac", logger=None)
        audio.close()
        video.close()
        return out
    except Exception as e:
        print("Video error:", e)
        return None
