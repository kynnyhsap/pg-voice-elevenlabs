import subprocess


samples = {
    'Interview': [
        ("00:04:18", "00:04:34"),
        ("00:06:03", "00:06:31"),
        ("00:11:17", "00:11:35"),
        ("00:20:14", "00:20:29"),
        # ("00:10:32", "00:10:56"),
    ],
    'Keynote': [
        # ("00:06:16", "00:06:36"),
        # ("00:07:02", "00:07:39"),
    ],
    'Lecture': [
        ("00:02:31", "00:03:00"),
        ("00:18:20", "00:18:50"),
        # ("00:08:50", "00:09:25"),
    ],
}

def command(sample_name, start, end):
    return ["ffmpeg", "-i", f"./samples/long/{sample_name}.mp3", "-ss", start, "-to", end, "-c", "copy", f"./samples/short/{sample_name}_{start}_{end}.mp3"]

for sample_name in samples:
    for start, end in samples[sample_name]:
        subprocess.run(command(sample_name, start, end))
