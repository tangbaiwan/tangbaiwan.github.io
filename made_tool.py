import os
import subprocess

Publish_Tool_Env = os.environ['PublicMGEnv'].replace('\\', '/')
EnvPath = (Publish_Tool_Env + '/Scriptlibrary/env')
ffmpeg_path = EnvPath + '/ffmpeg/bin/ffmpeg.exe'

uag_uagad_mov_file_path=r"F:\_BaiXiaoSheng\Work\Github\BxsUEProject\tangbaiwan.github.io\mywork\test1.mov"
uag_prev_gif_path=r"F:\_BaiXiaoSheng\Work\Github\BxsUEProject\tangbaiwan.github.io\mywork\test1.gif"


ffmpeg_cut_commands = ffmpeg_path + "  -y -i  \"" + uag_uagad_mov_file_path + "\"    -vf \"fps=10,scale=200:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse\" -loop 0   " + "\"" + uag_prev_gif_path + "\"  "
subprocess.Popen(ffmpeg_cut_commands, creationflags=subprocess.SW_HIDE, shell=True)