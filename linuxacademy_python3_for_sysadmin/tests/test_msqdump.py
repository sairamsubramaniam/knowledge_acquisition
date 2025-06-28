
import pytest
import subprocess

from msqbackup import msqdump

url = "mysql://root:walkin@123@127.0.0.1:3306/linuxacademy"

def test_dump_calls_msqdump(mocker):
    """
    Utilizes mysqldump with the dtabase URL
    """
    mocker.patch("subprocess.Popen")
    assert msqdump.dump(url)
    subprocess.Popen.assert_called_with(["mysqldump", url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    msqdump.dump returns a reasonable error if mysqldump isn't installed
    """
    mocker.patch("subprocess.Popen", side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        msqdump.dump(url)
