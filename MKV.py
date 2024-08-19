import os #Here you're able to interact with the operating system
import subprocess #Used to start new applications or processes. It allows you to run other programs or scripts from within your Python script, interact with them, and capture their output or errors.

if not os.path.exists("assets"):
    raise Exception("Please create and put all videos in the assets folder!")

mkv_list = os.listdir("assets")

if not os.path.exists("results"):
    os.mkdir("results")

for mkv in mkv_list:
    name, ext = os.path.splitext(mkv)
    if ext != ".mkv":
        raise Exception("Please add MKV files only!")

    output_name = name + ".mp4"
    try:
        subprocess.run(
            ['ffmpeg', '-i', f"assets/{mkv}", "-codec", "copy", f"results/{output_name}"], check=True
        )
    except:
        raise Exception(
            "Please Download, Install and Add the path of FFMPEG to Environment Variable!"
        )
print(f"{len(mkv_list)} video(s) converted to mp4")
os.startfile("results")

