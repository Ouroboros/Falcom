from Falcom.ED83.Parser.scena_writer import *
from Falcom.ED83.Parser.scena_writer_gen import *

ChrTable = GlobalConfig.ChrTable

def ReturnToTitle():
    Call(0x0A, 'FC_EventEndMapChange', (0xDD, 'title'), (0xDD, ''))

def SaveClearData():
    OP_90('current', 0x00000019)
    OP_93(0x00, 0x02)
    OP_93(0x01)

def ChangeSkin(chrId: int, model: str):
    # SetScenaFlags(ScenaFlag(0x00A7, 0, 0x538))
    AddChrAnimeClip(0x0A, chrId, model, '')

def CameraRotate(vertical: float, horizontal: float, rotation: float, durationInMs: int = 0):
    '''
        上下
        左右
        翻转
    '''
    OP_36(0x04, 0x03, vertical, horizontal, rotation, durationInMs, 0x01)
    return

def CameraPos(x: float, y: float, z: float):
    CameraCtrl(0x02, 0x03, x, y, z, 0)

def CameraHeight(height: float, durationInMs: int = 0):
    CameraCtrl(0x05, 0x03, height, durationInMs)
