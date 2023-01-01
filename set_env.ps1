#�J�����g�f�B���N�g��
$CurrentDir  = Split-Path $MyInvocation.MyCommand.path
$ffmpeg_zip_path = Join-Path $CurrentDir "tools\ffmpeg-win64.zip"
$ffmpeg_unzip = Join-Path $CurrentDir "tools\ffmpeg-master-latest-win64-gpl-shared"
$ffmpeg_dest = Join-Path $CurrentDir "tools\ffmpegmaster"
$ffmpeg_path_value = Join-Path $CurrentDir "tools\ffmpegmaster\bin"
$py_dest = Join-Path $CurrentDir "Python39"

$env_dest = Join-Path $CurrentDir "env"

# 1. �t�H���_�쐬
# 1.1. ffmpegmaster
if(!(Test-Path $ffmpeg_dest)) {
    Expand-Archive -Path $ffmpeg_zip_path -DestinationPath .\tools
    if(Test-Path $ffmpeg_unzip){
        Rename-Item $ffmpeg_unzip $ffmpeg_dest
    }
} else {
    echo ���Ƀt�H���_$ffmpeg_zip_path�����݂���
}

# 2. PATH��ʂ�
# 2.1 Python(Python39 / Python39\scripts)
$currenPath = [System.Environment]::GetEnvironmentVariable("Path", "User")

if($currenPath.Contains("Python3")) {
    echo Python3�Ƀp�X���ʂ��Ă�
}

if(!($currenPath.Contains("Python3"))) {
    $py_scripts_dest = Join-Path $CurrentDir "Python39\\Scripts"
    $currenPath += (";" + $py_dest)
    [System.Environment]::SetEnvironmentVariable("Path", $currenPath, "User")
    Start-Sleep -s 1
    $currenPath += (";" + $py_scripts_dest)
    [System.Environment]::SetEnvironmentVariable("Path", $currenPath, "User")
    Start-Sleep -s 1
}

# 2.2 ffmpegmaster
if($currenPath.Contains("ffmpegmaster")) {
    echo ffmpegmaster�Ƀp�X���ʂ��Ă�
}

if(!($currenPath.Contains("ffmpegmaster"))) {
    # C:\generate-minus-one\src\ffmpegmaster\bin
    $currenPath += (";" + $ffmpeg_path_value)
    [System.Environment]::SetEnvironmentVariable("Path", $currenPath, "User")
    Start-Sleep -s 1
}

#py -3 test.py
if(!(Test-Path $env_dest)) {
    echo env���Ȃ�
    py -3 -m venv env

}

#py -3 -m pip install --upgrade pip
#env\Scripts\Activate.ps1

#if(!(Test-Path $env_dest)) {
#    echo env���Ȃ�
#    pip install -r src\requirements.txt
#}

#py -3 src\main.py