import subprocess


samples = {
    'From the Archives Y Combinator Founders Paul Graham and Jessica Livingston on Studio 1.0 2014': [
        ("00:10:32", "00:10:56"),
        ("00:04:17", "00:04:35"),
        ("00:06:04", "00:06:32"),
        ("00:11:17", "00:11:37"),
        ("00:20:14", "00:20:30"),
    ],
    'Paul Graham Keynote Speech At OPT412': [
        ("00:06:16", "00:06:36"),
        ("00:07:02", "00:07:39"),
    ],
    'Lecture 3 - Before the Startup (Paul Graham)': [
        ("00:02:31", "00:03:00"),
        ("00:08:50", "00:09:25"),
        ("00:18:20", "00:18:50"),
    ],
}

def command(sample_name, start, end):
    return ["ffmpeg", "-i", f"./samples/long/{sample_name}.mp3", "-ss", start, "-to", end, "-c", "copy", f"./samples/short/{sample_name}_{start}_{end}.mp3"]

for sample_name in samples:
    for start, end in samples[sample_name]:
        subprocess.run(command(sample_name, start, end))
