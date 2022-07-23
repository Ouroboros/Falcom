from Falcom.Common import IntEnum2

L_ARM_POINT     = 'L_arm_point'
R_ARM_POINT     = 'R_arm_point'

L_HAND_POINT    = 'L_hand_point'
R_HAND_POINT    = 'R_hand_point'

NODE_L_HAND     = 'NODE_L_HAND'
NODE_R_HAND     = 'NODE_R_HAND'

MAX_REG_ID      = 0x20

DummyCharBaseId             = 0xB5E
TempCharBaseId              = 0xB68

class PseudoChrId(IntEnum2):
    Party1                  = 0x00F6
    Party2                  = 0x00F7
    Party3                  = 0x00F8
    Party4                  = 0x00F9
    Self                    = 0x00FE

class ChrPhysicsFlags(IntEnum2):
    Gravity                 = 0x0001
    Hidden                  = 0x0080
