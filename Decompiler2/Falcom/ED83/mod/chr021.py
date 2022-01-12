import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED83.Parser.scena_writer_helper import *

scena = createScenaWriter('chr021.dat')

# id: 0x0000 offset: 0x1D54
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'LADDER_START',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'LADDER_UP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'LADDER_END',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'IDLE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'DISARM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_WAIT_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'FATTACK1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'FATTACK2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_TURN_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            model      = 'C_CHR021_DF1',
            animeClip  = 'BTL_TURN_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_ARIA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_ARTS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_ARTSa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_ARTSb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_WIN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_WINa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_ITEM',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_LEVELUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_POWERUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_CRAFT00_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            model      = 'C_CHR021_BT1',
            animeClip  = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_06a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_10',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_10a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_11',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_12',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_13',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_14',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            model      = 'C_CHR021_SC1',
            animeClip  = 'BTL_S_CRAFT00_14a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GOUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_MEGANE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_MEGANE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_MEGANE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'BTL_DEAD1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_DF1',
            animeClip  = 'SIT_WAIT-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_DF1',
            animeClip  = 'SIT_WAIT-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_DF1',
            animeClip  = 'SIT_WAIT+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_DF1',
            animeClip  = 'SIT_WAIT+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'BTL_CRUCIFIXION',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'BTL_FLOAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_AKIRE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_AKIREa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_AKIREb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_AKUBI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_AKUBI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ASENUGUI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ASENUGUIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ASENUGUIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ATAMAKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ATAMAKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_BYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_BYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_BYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_BYEBYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_BYEBYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_BYEBYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_BYE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK+3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_DESK_AGO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_DESK_PEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_DESK_PEN_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_DESK_PEN_MOVEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK_PEN_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_DESK_PEN_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_DESK_RYOTE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_DESK_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_GAKKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_GAKKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_GAKKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_GAKKARI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_GAKKARI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_GAKKARI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GOUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HAKUSHU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HAKUSHUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HAKUSHUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HAKUSHUc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_HAKUSHU_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_HAKUSHU_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_HAKUSHU_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_HAKUSHU_2c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HANASIKAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HANASIKAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HANASIKAKEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HITEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HITEI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_GLASS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_GLASS_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_GLASSc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_GLASSc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_GLASS_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_CUP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_CUPc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_JOKKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_JOKKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_JOKKI_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOLD_JOKKIc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOOKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_HOOKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_INORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_INORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KABEMOTARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAIWA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAMIHARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KANGEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KANGEIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KANGEIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KANGEI2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KANGEI2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KANGEI2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KAZETUYO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KEIREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KEIREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KEIREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KEYBOARD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KEYBOARD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KEYBOARD_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_KUZUSISUWARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_MEGANE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_MEGANEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_MEGANEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_MOKUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_MOKUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_MOKUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ODOROKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_ODOROKI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_OJIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_OJIGI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_OJIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_OJIGIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_OJIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_OJIGIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_HOLD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_HOLDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_HOLD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_HOLD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_LOOK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_LOOKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_LOOK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_LOOK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_MISERU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_MISERUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_SOUSA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_SOUSAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_SOUSA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_SOUSA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_TALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_TALKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_TALK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_PHONE_TALK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_REI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_REI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_REIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_REIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_REIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_REIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_ATAMA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_ATAMAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_ATAMAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_ATAMA_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_AWASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_AWASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_AWASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_RYOTE_KOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_MAE_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_SIRIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_RYOTE_SIRI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SEKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SEKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIAN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIAN_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIAN_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SIANF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SIANFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SIANFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SIT_JIMEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SIT_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SLEEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SLEEPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SLEEP_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SLEEP_GAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SLEEP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TAORE_1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TAORE_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TAORE_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TAORE_4',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TEMUNE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TEMUNEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TEMUNE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TEMUNE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TEMUNE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEUKASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEUKASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEUKASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TORIDASI_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TORIDASI_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TORIDASI_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_TORIDASI_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMI_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIF_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIF_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIF_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIF_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIF_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_UKETORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_UKETORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_UKETORIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASU_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASU_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASU_KAMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASU_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASU_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_WATASU_KAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YAA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YAAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YAAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_YAREYARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YARUKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YARUKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YARUKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YASUME',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YASUME_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YASUMEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YASUMEa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YORIKAKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_LEFTa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_LEFTb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_SITA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_SITAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_SITAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_UE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_UEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_UEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_MIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_MIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHRX01_EV',
            animeClip  = 'EV_YUBISASI_MIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV02025',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev02045',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev02045a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV05500',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV05500a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV05500b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV05500c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV05503',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV05505',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV05510',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV05510a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev30000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev30005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev30005a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev30185',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev30185a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev30185b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev33000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev33000a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev33005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev34085',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'ev45000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_UDEGUMIF_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR021_EV',
            animeClip  = 'EV_TEKOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            model      = 'C_CHR010_EV',
            animeClip  = 'EV79000',
        ),
    )

# id: 0x0001 offset: 0x8BDC
@scena.FieldMonsterData('FieldMonsterData')
def FieldMonsterData():
    return ScenaFieldMonsterData(
        type       = 0x00000000,
        word04     = 0x0064,
        word06     = 0x0168,
        floats08   = [1.0, 2.0, 8.0, 8.0, 1.0],
    )

# id: 0x0002 offset: 0x8BFC
@scena.FieldFollowData('FieldFollowData')
def FieldFollowData():
    return ScenaFieldFollowData(
        1.0, 180.0, 2.0, 2.0, 9.0,
    )

# id: 0x0003 offset: 0x8C14
@scena.Code('Init')
def Init():
    Call(ScriptId.Current, 'Ani_EV_Load')
    If(
        (
            (Expr.Eval, "OP_54(0x3F)"),
            Expr.Return,
        ),
        'loc_8C1E',
    )

    Return()

    def _loc_8C1E(): pass

    label('loc_8C1E')

    LoadEffect(0xFFFE, 0x85, 'battle/win021_0.eff')

    If(
        (
            (Expr.GetChrWork, 0xFFFE, 0x8),
            (Expr.PushLong, 0x10),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8C50',
    )

    OP_54(0x0B, 0xFFFE)

    Jump('loc_8C67')

    def _loc_8C50(): pass

    label('loc_8C50')

    Call(ScriptId.Current, 'AniAttachMainWeapon')

    def _loc_8C67(): pass

    label('loc_8C67')

    If(
        (
            (Expr.Eval, "OP_54(0x27)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8D09',
    )

    LoadEffect(0xFFFE, 0x82, 'battle/atk021_0.eff')
    LoadEffect(0xFFFE, 0x83, 'battle/atk021_1.eff')
    LoadEffect(0xFFFE, 0x84, 'battle/atk021_2.eff')
    LoadEffect(0xFFFE, 0x85, 'battle/atk021_3.eff')
    LoadEffect(0xFFFE, 0x86, 'battle/atk021_a0.eff')
    LoadEffect(0xFFFE, 0x87, 'battle/atk021_a1.eff')

    def _loc_8D09(): pass

    label('loc_8D09')

    Call(ScriptId.Current, 'AniReset')
    Call(ScriptId.Current, 'OnChangeSkin')

    Return()

# id: 0x0004 offset: 0x8D28
@scena.Code('ReInit')
def ReInit():
    OP_54(0x0B, 0xFFFE)
    Call(ScriptId.Current, 'AniReset')

    Return()

# id: 0x0005 offset: 0x8D3C
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000002)

    Return()

# id: 0x0006 offset: 0x8D48
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000100)

    Return()

# id: 0x0007 offset: 0x8D54
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000010)

    Return()

# id: 0x0008 offset: 0x8D60
@scena.Code('Ani_MG_Load')
def Ani_MG_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000020)

    Return()

# id: 0x0009 offset: 0x8D6C
@scena.Code('Ani_HS_Load')
def Ani_HS_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000004)

    Return()

# id: 0x000A offset: 0x8D78
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000002)

    Return()

# id: 0x000B offset: 0x8D84
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000C offset: 0x8D98
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000D offset: 0x8DAC
@scena.Code('Ani_MG_Release')
def Ani_MG_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000020)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000E offset: 0x8DC0
@scena.Code('Ani_HS_Release')
def Ani_HS_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000004)

    Return()

# id: 0x000F offset: 0x8DCC
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    LoadAsset('C_EQU076')
    AttachEquip(0xFFFE, 'C_EQU076', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)

    Return()

# id: 0x0010 offset: 0x8E28
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    ReleaseAsset('C_EQU076')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x0011 offset: 0x8E6C
@scena.Code('AniBtlLoad')
def AniBtlLoad():
    If(
        (
            (Expr.Eval, "BattleCtrl(0x62, 0xFFFE, 0x12)"),
            Expr.Return,
        ),
        'loc_8E93',
    )

    AnimeClipCtrl(0x00, 0xFFFE, 'C_CHR021_DF1', 'WAIT')

    Jump('loc_8E9B')

    def _loc_8E93(): pass

    label('loc_8E93')

    AnimeClipLoadByCatalog(0xFFFE, 0x00000100)

    def _loc_8E9B(): pass

    label('loc_8E9B')

    Return()

# id: 0x0012 offset: 0x8E9C
@scena.Code('AniReset')
def AniReset():
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'EraseEquip')

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_54(0x27)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F1C',
    )

    If(
        (
            (Expr.PushLong, 0x0),
            Expr.Return,
        ),
        'loc_8F1C',
    )

    Call(ScriptId.Current, 'AniStartRainMode')

    def _loc_8F1C(): pass

    label('loc_8F1C')

    Return()

# id: 0x0013 offset: 0x8F20
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0014 offset: 0x8F2C
@scena.Code('AniResetWorkRun')
def AniResetWorkRun():
    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0015 offset: 0x8F38
@scena.Code('DefaultFace')
def DefaultFace():
    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0016 offset: 0x8F60
@scena.Code('OnChangeSkin')
def OnChangeSkin():
    If(
        (
            (Expr.Eval, "OP_54(0x27)"),
            Expr.Return,
        ),
        'loc_8F6E',
    )

    Jump('loc_8F94')

    def _loc_8F6E(): pass

    label('loc_8F6E')

    Call(ScriptId.Current, 'AniNPCWaitMotionLoad')
    Call(ScriptId.Current, 'AniBtlLoad')

    def _loc_8F94(): pass

    label('loc_8F94')

    Return()

# id: 0x0017 offset: 0x8F98
@scena.Code('OnCampIn')
def OnCampIn():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    OP_38(0xFFFE, 0x01, 0x00, '')
    SetChrFace(0x03, 0xFFFE, '0', '[autoM0]', '0', '#b', '0')
    OP_38(0xFFFE, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0018 offset: 0x8FEC
@scena.Code('OnCostumeIn1')
def OnCostumeIn1():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_38(0xFFFE, 0x01, 0x00, '')
    SetChrAniFunction(0xFFFE, 0x00, 'AniEvWait', 0.4, 1.0, 0x00000000)

    Return()

# id: 0x0019 offset: 0x9048
@scena.Code('OnCostumeIn2')
def OnCostumeIn2():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EraseEquip')
    OP_38(0xFFFE, 0x01, 0x00, '')
    OP_38(0xFFFE, 0x00, 0x00, 'AniIdle')

    Return()

# id: 0x001A offset: 0x9088
@scena.Code('OnCostumeIn3')
def OnCostumeIn3():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    AnimeClipLoadMultiple(0xFFFE, 0x00, 'OnCostumeIn3_2', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    OP_38(0xFFFE, 0x01, 0x00, '')
    OP_38(0xFFFE, 0x00, 0x00, 'OnCostumeIn3_2')

    Return()

# id: 0x001B offset: 0x9100
@scena.Code('OnCostumeIn3_2')
def OnCostumeIn3_2():
    PlayChrAnimeClip(0xFFFE, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, 'E', '4', '', '#b', '0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_9190',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, (0xFF, 0x1742, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_9199')

    def _loc_9190(): pass

    label('loc_9190')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9199(): pass

    label('loc_9199')

    Sleep(500)
    SetChrFace(0x03, 0xFFFE, '4', 'A[autoMA]', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)
    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '', '#b', '0')

    Return()

# id: 0x001C offset: 0x9204
@scena.Code('AniFieldChange')
def AniFieldChange():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x170C, 0x0), (0xFF, 0x170D, 0x0), (0xFF, 0x170E, 0x0), (0xFF, 0x0, 0x0))

    Return()

# id: 0x001D offset: 0x9234
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)

    Return()

# id: 0x001E offset: 0x9248
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x00)

    Return()

# id: 0x001F offset: 0x925C
@scena.Code('AniEvAttachEquip')
def AniEvAttachEquip():
    Call(ScriptId.Current, 'ShowEquip')

    Return()

# id: 0x0020 offset: 0x926C
@scena.Code('AniEvDetachEquip')
def AniEvDetachEquip():
    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x0021 offset: 0x927C
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'Left_ring', 0.2)
    OP_8A(0xFE, 0xFFFE, 'Right_ring', 0.2)
    OP_8A(0xFE, 0xFFFE, 'M_himo01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'M_himo02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BH1', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BM03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BM04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftChest', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightChest', 0.2)

    Return()

# id: 0x0022 offset: 0x93F0
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'Left_ring', 0.2)
    OP_8A(0xFF, 0xFFFE, 'Right_ring', 0.2)
    OP_8A(0xFF, 0xFFFE, 'M_himo01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'M_himo02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BH1', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BM03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BM04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftChest', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightChest', 0.2)

    Return()

# id: 0x0023 offset: 0x9564
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x0024 offset: 0x9568
@scena.Code('AniStartRainMode')
def AniStartRainMode():
    Return()

# id: 0x0025 offset: 0x956C
@scena.Code('AniEndRainMode')
def AniEndRainMode():
    Return()

# id: 0x0026 offset: 0x9570
@scena.Code('AniNPCWaitMotionLoad')
def AniNPCWaitMotionLoad():
    Return()

# id: 0x0027 offset: 0x9574
@scena.Code('AniWait')
def AniWait():
    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9600',
    )

    If(
        (
            (Expr.Eval, "OP_70(0x07, 0xFFFE, 0x00)"),
            (Expr.PushLong, 0x270F),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_95DB',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')

    Jump('loc_95FB')

    def _loc_95DB(): pass

    label('loc_95DB')

    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_95FB(): pass

    label('loc_95FB')

    Jump('loc_9918')

    def _loc_9600(): pass

    label('loc_9600')

    If(
        (
            (Expr.Eval, "ChrPhysicsCtrl(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_975B',
    )

    Call(ScriptId.Current, 'ShowEquip')

    If(
        (
            (Expr.Eval, "OP_A8(0x40000000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9641',
    )

    Call(ScriptId.Current, 'BtlDefaultFace')

    def _loc_9641(): pass

    label('loc_9641')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_96B4',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(0xFFFE, 'BTL_STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_9756')

    def _loc_96B4(): pass

    label('loc_96B4')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_972E',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_AD(0x02, 0.1)
    OP_80(0.1)
    PlayChrAnimeClip(0xFFFE, 'BTL_STOP_DASH', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_9756')

    def _loc_972E(): pass

    label('loc_972E')

    OP_80(0.35)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_9756(): pass

    label('loc_9756')

    Jump('loc_9918')

    def _loc_975B(): pass

    label('loc_975B')

    If(
        (
            (Expr.Eval, "ChrPhysicsCtrl(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_97A3',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_9918')

    def _loc_97A3(): pass

    label('loc_97A3')

    Call(ScriptId.Current, 'EraseEquip')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_981C',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.15)
    PlayChrAnimeClip(0xFFFE, 'STOP_RUN', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_9918')

    def _loc_981C(): pass

    label('loc_981C')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_988E',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.1)
    OP_AD(0x02, 0.1)
    PlayChrAnimeClip(0xFFFE, 'STOP_DASH', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_9918')

    def _loc_988E(): pass

    label('loc_988E')

    If(
        (
            (Expr.PushReg, 0x6),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_98F4',
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(0xFFFE, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_9918')

    def _loc_98F4(): pass

    label('loc_98F4')

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_9918(): pass

    label('loc_9918')

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0028 offset: 0x9934
@scena.Code('AniWalk')
def AniWalk():
    OP_80(0.3)

    If(
        (
            (Expr.Eval, "ChrPhysicsCtrl(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_99CE',
    )

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_99A6',
    )

    If(
        (
            (Expr.Eval, "OP_7A(0x02, 0xFFFE, 'BTL_WAIT')"),
            Expr.Return,
        ),
        'loc_99A6',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    OP_80(0.1)

    def _loc_99A6(): pass

    label('loc_99A6')

    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_9A2D')

    def _loc_99CE(): pass

    label('loc_99CE')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9A0E',
    )

    PlayChrAnimeClip(0xFFFE, 'WAIT_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    OP_80(0.1)

    def _loc_9A0E(): pass

    label('loc_9A0E')

    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    def _loc_9A2D(): pass

    label('loc_9A2D')

    Sleep(166)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0029 offset: 0x9A4C
@scena.Code('AniRun')
def AniRun():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "ChrPhysicsCtrl(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_9AEA',
    )

    If(
        (
            (Expr.Eval, "OP_7A(0x02, 0xFFFE, 'BTL_WAIT')"),
            (Expr.Eval, "OP_7A(0x02, 0xFFFE, 'BTL_WAIT_WALK')"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_9AC2',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT_MOVE', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_9AC2(): pass

    label('loc_9AC2')

    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_9B08')

    def _loc_9AEA(): pass

    label('loc_9AEA')

    PlayChrAnimeClip(0xFFFE, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    def _loc_9B08(): pass

    label('loc_9B08')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9B1F',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9B1F(): pass

    label('loc_9B1F')

    OP_6C(0xFFFE, 1.2)
    Sleep(666)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002A offset: 0x9B3C
@scena.Code('AniDash')
def AniDash():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "ChrPhysicsCtrl(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_9B82',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_9BA1')

    def _loc_9B82(): pass

    label('loc_9B82')

    PlayChrAnimeClip(0xFFFE, 'DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_9BA1(): pass

    label('loc_9BA1')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9BB8',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_9BB8(): pass

    label('loc_9BB8')

    Sleep(666)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002B offset: 0x9BD0
@scena.Code('AniBack')
def AniBack():
    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    Sleep(166)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002C offset: 0x9C14
@scena.Code('AniDamage')
def AniDamage():
    SetChrFace(0x03, 0xFFFE, 'B', '3', '', '#b', '0')
    OP_3B(0x32, (0xFF, 0x1726, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    If(
        (
            (Expr.Eval, "BattleCtrl(0xAF, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9CA4',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_9CC9')

    def _loc_9CA4(): pass

    label('loc_9CA4')

    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_9CC9(): pass

    label('loc_9CC9')

    Sleep(500)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002D offset: 0x9CE8
@scena.Code('AniTurn')
def AniTurn():
    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.2)

    If(
        (
            (Expr.Eval, "ChrPhysicsCtrl(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_9D83',
    )

    If(
        (
            (Expr.Eval, "OP_54(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9D47',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_9D7E')

    def _loc_9D47(): pass

    label('loc_9D47')

    If(
        (
            (Expr.Eval, "OP_54(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9D7E',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_9D7E(): pass

    label('loc_9D7E')

    Jump('loc_9DF5')

    def _loc_9D83(): pass

    label('loc_9D83')

    If(
        (
            (Expr.Eval, "OP_54(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9DBE',
    )

    PlayChrAnimeClip(0xFFFE, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_9DF5')

    def _loc_9DBE(): pass

    label('loc_9DBE')

    If(
        (
            (Expr.Eval, "OP_54(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9DF5',
    )

    PlayChrAnimeClip(0xFFFE, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_9DF5(): pass

    label('loc_9DF5')

    OP_3F(0xFFFE)
    OP_38(0xFFFE, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x002E offset: 0x9E08
@scena.Code('AniSquat')
def AniSquat():
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_9E4E',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_9F07')

    def _loc_9E4E(): pass

    label('loc_9E4E')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_9EB9',
    )

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'SQUAT', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_9F07')

    def _loc_9EB9(): pass

    label('loc_9EB9')

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_9F07(): pass

    label('loc_9F07')

    Return()

# id: 0x002F offset: 0x9F08
@scena.Code('AniFall')
def AniFall():
    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0030 offset: 0x9F38
@scena.Code('AniLand')
def AniLand():
    OP_80(0.05)
    PlayChrAnimeClip(0xFFFE, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    ExecExpressionWithReg(
        0x06,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_38(0xFFFE, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0031 offset: 0x9F84
@scena.Code('AniIdle')
def AniIdle():
    SetEndhookFunction('DefaultFace', 0x000B)
    OP_80(0.2)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_9FF3',
    )

    OP_3B(0x32, (0xFF, 0x1761, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_A036')

    def _loc_9FF3(): pass

    label('loc_9FF3')

    OP_3B(0x32, (0xFF, 0x1762, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_A036(): pass

    label('loc_A036')

    SetChrFace(0x03, 0xFFFE, '000G1G0000000000000000000000000000000G11G0', '0[autoM0]', '000003333333333333333333333333333333333700000', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'IDLE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'DefaultFace')

    Return()

# id: 0x0032 offset: 0xA0F8
@scena.Code('AniFieldAttack')
def AniFieldAttack():
    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(0xFFFE, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_80(0.1)
    PlayChrAnimeClip(0xFFFE, 'FATTACK1', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, 30.0667, -1.0, -1.0, 0x00, 0x00)
    Sleep(133)
    PlayEffect(0xFFFE, (0xFF, 0x83, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F5D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(66)
    MoveChr(0xFFFE, 0xFE00, 0.0, 0.0, 0.85, 6.5, 0x00, 0x0000)
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1711, 0x0), (0xFF, 0x1712, 0x0), (0xFF, 0x1713, 0x0), (0xFF, 0x0, 0x0))
    Sleep(66)
    PlayEffect(0xFFFE, (0xFF, 0x82, 0x0), 0xFFFE, 0x00000023, (0xDD, ''), (0xEE, 0.3499999940395355, 0x0), (0xEE, 1.0, 0x0), (0xEE, 0.5, 0x0), -5.0, 0.0, 155.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    CameraCtrl(0x0A, 0.0, 0.1, 1.0, 0x001E, 0x0064, 0x001E, 0x0000, 0x0000, 0x00)
    Sleep(66)
    OP_41(0xFFFE, 0x01)
    Sleep(200)
    OP_AD(0x01, 0x01)
    Sleep(333)
    OP_AD(0x00, 0x01)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0033 offset: 0xA2D8
@scena.Code('AniFieldAttack2')
def AniFieldAttack2():
    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'FATTACK2', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, 33.3667, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '6', '1', '', '#b', '0')
    ChrSetPhysicsFlags(0xFFFE, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    Sleep(200)
    Sleep(100)
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1711, 0x0), (0xFF, 0x1712, 0x0), (0xFF, 0x1713, 0x0), (0xFF, 0x0, 0x0))
    PlayEffect(0xFFFE, (0xFF, 0x84, 0x0), 0xFFFE, 0x00000023, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    OP_3B(0x00, (0xFF, 0x8F5D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -0.3, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F07, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.0, 0.1, 1.0, 0x001E, 0x010E, 0x001E, 0x0000, 0x0000, 0x00)
    Sleep(66)
    OP_41(0xFFFE, 0x01)
    Sleep(266)
    OP_AD(0x00, 0x01)
    OP_AD(0x01, 0x01)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0034 offset: 0xA460
@scena.Code('AniAssaultAttack')
def AniAssaultAttack():
    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    ChrSetPhysicsFlags(0xFFFE, 0x00000010)
    SetEndhookFunction('BtlDefaultFace', 0x000B)
    OP_4C(0xFFFE, 0.5, 0.7, 1.0, 0x0000, 0x03)
    OP_4C(0xFFFE, 0.0, 0.0, 0.0, 0x012C, 0x03)
    OP_3B(0x00, (0xFF, 0xFC0, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_80(0.1)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 36.6667, 37.0667, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)
    PlayEffect(0xFFFE, (0xFF, 0x86, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x1063, 0x0), 0.6, (0xFF, 0xC8, 0x0), 0.0, -5.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x10BC, 0x0), 0.7, (0xFF, 0xC8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Sleep(66)
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1714, 0x0), (0xFF, 0x1715, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 37.1, 39.4, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 2.0)
    Sleep(33)
    EffectCtrl(0x17, 0xFFFE, 0x02, 8.0)
    PlayEffect(0xFFFE, (0xFF, 0x87, 0x0), 0xFFFE, 0x00000023, (0xDD, ''), (0xEE, 0.3499999940395355, 0x0), (0xEE, 1.5, 0x0), (0xEE, 0.5, 0x0), 0.0, 0.0, 155.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    OP_3B(0x00, (0xFF, 0x8F91, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F6A, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.0, 0.2, 0.0, 0x003C, 0x0001, 0x0190, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0003, 0.75, 0x003C, 0x0001, 0x012C, 0.2, 0xFFFE, 0.0, 1.0, 0.0)
    Sleep(33)
    MoveChr(0xFFFE, 0xFE00, 0.0, 0.0, 0.85, 6.5, 0x00, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Sleep(100)
    OP_41(0xFFFE, 0x01)
    OP_AD(0x01, 0x01)
    OP_AD(0x00, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0035 offset: 0xA798
@scena.Code('AniFieldAttackEnd')
def AniFieldAttackEnd():
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'DefaultFace')
    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x753A, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(500)
    ChrClearPhysicsFlags(0xFFFE, 0x00000010)
    OP_AD(0x00, 0x01)
    OP_3B(0x00, (0xFF, 0x7536, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7537, 0x0), 0.3, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(766)
    Call(ScriptId.Current, 'AniFieldAttackEnd_endHook')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0036 offset: 0xA914
@scena.Code('AniFieldAttackEnd_endHook')
def AniFieldAttackEnd_endHook():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(0xFFFE, 0x00000010)

    Return()

# id: 0x0037 offset: 0xA93C
@scena.Code('AniFieldAttackEndShort')
def AniFieldAttackEndShort():
    SetEndhookFunction('AniFieldAttackEnd_endHook', 0x000B)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'DefaultFace')
    ChrClearPhysicsFlags(0xFFFE, 0x00000010)
    PlayChrAnimeClip(0xFFFE, 'DISARM', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, 27.1667, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x7536, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7537, 0x0), 0.3, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(933)
    Call(ScriptId.Current, 'EraseEquip')

    Return()

# id: 0x0038 offset: 0xAA40
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320')
    AttachEquip(0xFFFE, 'C_EQU320', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)

    Return()

# id: 0x0039 offset: 0xAA9C
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_54(0x0B, 0xFFFE)

    Return()

# id: 0x003A offset: 0xAAE4
@scena.Code('AniHorse')
def AniHorse():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x003B offset: 0xAB20
@scena.Code('AniHorse2')
def AniHorse2():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x003C offset: 0xAB5C
@scena.Code('AniHorseWalk')
def AniHorseWalk():
    PlayChrAnimeClip(0xFFFE, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003D offset: 0xAB8C
@scena.Code('AniHorseRun')
def AniHorseRun():
    PlayChrAnimeClip(0xFFFE, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003E offset: 0xABBC
@scena.Code('AniHorseDash')
def AniHorseDash():
    PlayChrAnimeClip(0xFFFE, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003F offset: 0xABEC
@scena.Code('AniHorseStop')
def AniHorseStop():
    PlayChrAnimeClip(0xFFFE, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0040 offset: 0xAC1C
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0041 offset: 0xAC54
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x01, 0x00, 0x00, 0x01, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Return()

# id: 0x0042 offset: 0xAC88
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, 0xFFFE, '2[autoE2]', '2[autoM2]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0043 offset: 0xACB0
@scena.Code('AniBtlInit')
def AniBtlInit():
    If(
        (
            (Expr.Eval, "BattleCtrl(0x62, 0xFFFE, 0x12)"),
            Expr.Return,
        ),
        'loc_ACBD',
    )

    Return()

    def _loc_ACBD(): pass

    label('loc_ACBD')

    ReleaseEffect(0xFFFE, 0x8A)
    ReleaseEffect(0xFFFE, 0x8B)
    LoadEffect(0xFFFE, 0x8A, 'battle_sys/sysspark2.eff')
    LoadEffect(0xFFFE, 0x8B, 'battle_sys/sysrelease.eff')
    ReleaseEffect(0xFFFE, 0x80)
    LoadEffect(0xFFFE, 0x80, 'battle/moncharge.eff')
    Call(ScriptId.BtlCom, 'AniBtlInit')

    Return()

# id: 0x0044 offset: 0xAD34
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x384),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD8E',
    )

    OP_3B(0x32, (0xFF, 0x1758, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x39, 0xFFFE)

    Jump('loc_AFFE')

    def _loc_AD8E(): pass

    label('loc_AD8E')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x1F4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ADE8',
    )

    OP_3B(0x32, (0xFF, 0x1759, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x39, 0xFFFE)

    Jump('loc_AFFE')

    def _loc_ADE8(): pass

    label('loc_ADE8')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x391),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AE42',
    )

    OP_3B(0x32, (0xFF, 0x175A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x39, 0xFFFE)

    Jump('loc_AFFE')

    def _loc_AE42(): pass

    label('loc_AE42')

    If(
        (
            (Expr.Eval, "BattleCtrl(0x5C, 0x06)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AE9A',
    )

    OP_3B(0x32, (0xFF, 0x1735, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_AFFE')

    def _loc_AE9A(): pass

    label('loc_AE9A')

    If(
        (
            (Expr.Eval, "BattleCtrl(0x5C, 0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            (Expr.Eval, "BattleCtrl(0x5C, 0x06)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Or,
            (Expr.Eval, "BattleCtrl(0x5C, 0x06)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_AF08',
    )

    OP_3B(0x32, (0xFF, 0x1734, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_AFFE')

    def _loc_AF08(): pass

    label('loc_AF08')

    If(
        (
            (Expr.Eval, "BattleCtrl(0x5C, 0x06)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AF60',
    )

    OP_3B(0x32, (0xFF, 0x1737, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_AFFE')

    def _loc_AF60(): pass

    label('loc_AF60')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_AFBB',
    )

    OP_3B(0x32, (0xFF, 0x1732, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_AFFE')

    def _loc_AFBB(): pass

    label('loc_AFBB')

    OP_3B(0x32, (0xFF, 0x1733, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_AFFE(): pass

    label('loc_AFFE')

    Return()

# id: 0x0045 offset: 0xB000
@scena.Code('AniBtlReady')
def AniBtlReady():
    If(
        (
            (Expr.Eval, "BattleCtrl(0x62, 0xFFFE, 0x07)"),
            Expr.Return,
        ),
        'loc_B02D',
    )

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x170F, 0x0), (0xFF, 0x1710, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    Jump('loc_B049')

    def _loc_B02D(): pass

    label('loc_B02D')

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x170C, 0x0), (0xFF, 0x170D, 0x0), (0xFF, 0x170E, 0x0), (0xFF, 0x0, 0x0))

    def _loc_B049(): pass

    label('loc_B049')

    Return()

# id: 0x0046 offset: 0xB04C
@scena.Code('AniBtlChain')
def AniBtlChain():
    OP_3B(0x32, (0xFF, 0x1736, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Return()

# id: 0x0047 offset: 0xB090
@scena.Code('VoiceWin_select')
def VoiceWin_select():
    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x01,
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 3, 0x42B)),
            Expr.Return,
        ),
        'loc_B0BB',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0xA),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B0E0')

    def _loc_B0BB(): pass

    label('loc_B0BB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_B0D7',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B0E0')

    def _loc_B0D7(): pass

    label('loc_B0D7')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B0E0(): pass

    label('loc_B0E0')

    Return()

# id: 0x0048 offset: 0xB0E4
@scena.Code('VoiceWin_play')
def VoiceWin_play():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B13A',
    )

    OP_3B(0x32, (0xFF, 0x1739, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_B1D3')

    def _loc_B13A(): pass

    label('loc_B13A')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B190',
    )

    OP_3B(0x32, (0xFF, 0x1738, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_B1D3')

    def _loc_B190(): pass

    label('loc_B190')

    OP_3B(0x32, (0xFF, 0x1739, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_B1D3(): pass

    label('loc_B1D3')

    Return()

# id: 0x0049 offset: 0xB1D4
@scena.Code('AniBtlWin')
def AniBtlWin():
    CameraCtrl(0x00)
    CameraCtrl(0x0B, 0x03, 40.0, 0x0000)
    CameraCtrl(0x03, 0x03, 0xFFFE, '', 0.3, 1.16, 0.09, 0x0000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 4.0, -15.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.6, 0)
    CameraCtrl(0x0B, 0x03, 40.0, 0x0000)
    CameraCtrl(0x14, 0x02, 0xFFFE, '', 0.2, 1.35, 0.3, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x02, 8.0, -8.0, 0.0, 4000, 0x01)
    CameraCtrl(0x05, 0x02, 1.9, 4000)
    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '', '#b', '0')
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'ShowEquip')
    Call(ScriptId.Current, 'VoiceWin_select')
    PlayChrAnimeClip(0xFFFE, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(600)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B384',
    )

    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    Sleep(200)
    Call(ScriptId.Current, 'VoiceWin_play')
    SetChrFace(0x03, 0xFFFE, '3', '2', '', '#b', '0')
    OP_3B(0x00, (0xFF, 0x8F74, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(900)
    SetChrFace(0x03, 0xFFFE, '2[autoE2]', '0[autoM0]', '', '#b', '0')

    Jump('loc_B418')

    def _loc_B384(): pass

    label('loc_B384')

    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    Sleep(200)
    Call(ScriptId.Current, 'VoiceWin_play')
    SetChrFace(0x03, 0xFFFE, '3', '2', '', '#b', '0')
    OP_3B(0x00, (0xFF, 0x8F74, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(900)
    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '', '#b', '0')

    def _loc_B418(): pass

    label('loc_B418')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.8)
    OP_3B(0x39, 0xFFFE)
    Sleep(600)
    Fade(0x65, 250, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.33, 0.02, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 14.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCtrl(0x0B, 0x03, 40.0, 0x0000)
    Sleep(1000)

    Return()

# id: 0x004A offset: 0xB4A0
@scena.Code('AniBtlWin_burst')
def AniBtlWin_burst():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '0', '4', '', '#b', '0')
    Sleep(700)
    SetChrFace(0x03, 0xFFFE, 'E', '', '', '#b', '0')
    OP_3B(0x00, (0xFF, 0x8F74, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(200)
    OP_3B(0x32, (0xFF, 0x1741, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(500)
    SetChrFace(0x03, 0xFFFE, '4', 'A[autoMA]', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.8)
    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '', '#b', '0')
    OP_3B(0x34, (0xFF, 0x1741, 0x0))

    Return()

# id: 0x004B offset: 0xB5E8
@scena.Code('AniBtlWin_eraseEquip')
def AniBtlWin_eraseEquip():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)
    Sleep(1000)
    Call(ScriptId.Current, 'EraseEquip')
    ChrClearPhysicsFlags(0xFFFE, 0x00000010)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x004C offset: 0xB65C
@scena.Code('AniBtlWinWait')
def AniBtlWinWait():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x004D offset: 0xB69C
@scena.Code('AniBtlWinWait_sub')
def AniBtlWinWait_sub():
    AnimeClipCtrl(0x09, 0xFFFE, 0x00)

    Return()

# id: 0x004E offset: 0xB6A4
@scena.Code('AniBtlLevelUp')
def AniBtlLevelUp():
    Call(ScriptId.BtlCom, 'AniBtlStartLevelUp')
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtLevelUp_Call')
    BattleCtrl(0x47)
    CameraCtrl(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', 0.0, -0.245, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 8.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.9, 0)
    CameraCtrl(0x0B, 0x03, 40.0, 0x0000)
    CameraCtrl(0x11, 0x03, 5.0, 8.0, 0.0, 0x2710, 0x01)
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(0xFFFE, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, 'E', '4', '', '#b', '0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_B7D8',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_3B(0x32, (0xFF, 0x1742, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_B7E1')

    def _loc_B7D8(): pass

    label('loc_B7D8')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B7E1(): pass

    label('loc_B7E1')

    Sleep(500)
    SetChrFace(0x03, 0xFFFE, '132[autoE2]', '0[autoM0]', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x004F offset: 0xB838
@scena.Code('AniBtLevelUp_Call')
def AniBtLevelUp_Call():
    Sleep(500)
    Call(ScriptId.BtlCom, 'AniBtlShowLevelUp')

    Return()

# id: 0x0050 offset: 0xB854
@scena.Code('AniBtlWait')
def AniBtlWait():
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0051 offset: 0xB88C
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCtrl(0x00)
    BattleCtrl(0x47)
    BattleCtrl(0x48, 0xFFFE)
    BattleCtrl(0x46, 0.25, 6.0, 15.0)
    BattleCtrl(0x4B, 0x01F4, 0x03)
    Call(ScriptId.CurrentCharacter, 'BtlMoveTransition')

    Return()

# id: 0x0052 offset: 0xB8C0
@scena.Code('BtlMoveTransition')
def BtlMoveTransition():
    OP_38(0xFFFE, 0x00, 0x01, 'AniTransitionMosion')
    BattleMoveToTarget()
    OP_1F(0xFFFE, 0x01)
    Call(ScriptId.CurrentCharacter, 'AniBtlWait')

    Return()

# id: 0x0053 offset: 0xB8F0
@scena.Code('AniTransitionMosion')
def AniTransitionMosion():
    If(
        (
            (Expr.Eval, "BattleCtrl(0x0D, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Ez,
            (Expr.Eval, "BattleCtrl(0x0D, 0xFFFE)"),
            (Expr.PushLong, 0x40000),
            Expr.And,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B96E',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT_MOVE', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    DebugLog(0x00, (0xFF, 0x3, 0x0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_B9C9')

    def _loc_B96E(): pass

    label('loc_B96E')

    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT_MOVE', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    DebugLog(0x00, (0xFF, 0x3, 0x0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_B9C9(): pass

    label('loc_B9C9')

    Return()

# id: 0x0054 offset: 0xB9CC
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    If(
        (
            (Expr.Eval, "OP_54(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_BA08',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_TURN_L', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_BA3F')

    def _loc_BA08(): pass

    label('loc_BA08')

    If(
        (
            (Expr.Eval, "OP_54(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_BA3F',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_TURN_R', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_BA3F(): pass

    label('loc_BA3F')

    Return()

# id: 0x0055 offset: 0xBA40
@scena.Code('AniBtlStepIn')
def AniBtlStepIn():
    Call(ScriptId.BtlCom, 'AniBtlStepIn', (0xFF, 0x172E, 0x0))

    Return()

# id: 0x0056 offset: 0xBA58
@scena.Code('AniBtlStepOut')
def AniBtlStepOut():
    Call(ScriptId.BtlCom, 'AniBtlStepOut', (0xFF, 0x172D, 0x0))

    Return()

# id: 0x0057 offset: 0xBA70
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCtrl(0x00)
    BattleCtrl(0x47)
    BattleCtrl(0x48, 0xFFFE)
    BattleCtrl(0x48, 0xFFFB)
    BattleCtrl(0x46, 0.25, 6.0, 15.0)
    BattleCtrl(0x4B, 0x00FA, 0x03)
    Call(ScriptId.CurrentCharacter, 'BtlMoveTransition')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '6', '0', '', '#b', '0')
    OP_6C(0xFFFE, 0.3)
    Sleep(166)
    OP_6C(0xFFFE, 1.0)
    Sleep(333)

    If(
        (
            (Expr.Eval, "BattleCtrl(0x62, 0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_BB27',
    )

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1711, 0x0), (0xFF, 0x1712, 0x0), (0xFF, 0x1713, 0x0), (0xFF, 0x0, 0x0))

    def _loc_BB27(): pass

    label('loc_BB27')

    PlayEffect(0xFFFE, (0xFF, 0x83, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F5D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x85, 0x0), 0xFFFE, 0x00000023, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    CameraCtrl(0x0A, 0.1, 0.2, 0.1, 0x001E, 0x0190, 0x003C, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    SetChrFace(0x03, 0xFFFE, '6', 'B', '', '#b', '0')
    BattleCtrl(0x47)
    BattleCtrl(0x48, 0xFFFB)
    BattleCtrl(0x46, 0.7, 6.0, 15.0)
    BattleCtrl(0x4B, 0x02BC, 0x03)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Sleep(66)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3F8, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x3, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))
    Sleep(1333)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0058 offset: 0xBCD0
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    OP_3B(0x32, (0xFF, 0x172A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x0059 offset: 0xBD28
@scena.Code('AniBtlDamage')
def AniBtlDamage():
    SetChrFace(0x03, 0xFFFE, 'B', '3', '', '#b', '0')

    If(
        (
            (Expr.Eval, "BattleCtrl(0xAF, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BD75',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_BD9A')

    def _loc_BD75(): pass

    label('loc_BD75')

    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_BD9A(): pass

    label('loc_BD9A')

    Sleep(833)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005A offset: 0xBDB8
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1726, 0x0), (0xFF, 0x1727, 0x0), (0xFF, 0x1728, 0x0), (0xFF, 0x0, 0x0))

    Return()

# id: 0x005B offset: 0xBDD8
@scena.Code('AniBtlSwoon')
def AniBtlSwoon():
    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_BE22',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_BE76')

    def _loc_BE22(): pass

    label('loc_BE22')

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_BE76(): pass

    label('loc_BE76')

    Return()

# id: 0x005C offset: 0xBE78
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x005D offset: 0xBEAC
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x90, 'battle_sys/tensionmax.eff')
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '2,11111133', '0000JH0', '0', '#b', '0')
    BattleCtrl(0x47)
    CameraCtrl(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.35, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, 18.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 3.25, 0)
    CameraCtrl(0x0C, 0x03, 0.0, -0.15, 0.0, 8000)
    CameraCtrl(0x11, 0x03, -5.0, 22.0, 0.0, 0x1F40, 0x01)
    CameraCtrl(0x16, 0x03, -2.0, 3000)
    BattleCtrl(0x4B, 0x1F40, 0x03)
    Sleep(1000)
    SetChrFace(0x03, 0xFFFE, '3773', '2662', '0', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_6C(0xFFFE, 1.2)
    SetChrFace(0x03, 0xFFFE, '6662', '733131313333', '0', '#b', '0')
    CameraCtrl(0x0A, 0.008, 0.008, 0.0, 0x03E8, 0x03E8, 0x01F4, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0002, 0.1, 0x00C8, 0x05DC, 0x0190, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    CameraCtrl(0x16, 0x03, 1.0, 450)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 450)
    Sleep(333)
    CameraCtrl(0x16, 0x03, 1.0, 5000)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    Sleep(1666)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'ReleaseEffect')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x005E offset: 0xC0D8
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')

    Return()

# id: 0x005F offset: 0xC0EC
@scena.Code('AniBtlDead')
def AniBtlDead():
    SetChrFace(0x03, 0xFFFE, '9', '7', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleCtrl(0x0D, 0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_C1E1',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x384),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x391),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_C196',
    )

    OP_3B(0x32, (0xFF, 0x175E, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x34, (0xFF, 0x175E, 0x0))

    Jump('loc_C1E1')

    def _loc_C196(): pass

    label('loc_C196')

    OP_3B(0x32, (0xFF, 0x1729, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x34, (0xFF, 0x1729, 0x0))

    def _loc_C1E1(): pass

    label('loc_C1E1')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0060 offset: 0xC210
@scena.Code('AniBtlAria')
def AniBtlAria():
    Call(ScriptId.BtlCom, 'AniBtlAria', (0xFF, 0x1722, 0x0), (0xFF, 0x1723, 0x0), (0xEE, -1.0, 0x0), (0xEE, 0.0, 0x0))

    Return()

# id: 0x0061 offset: 0xC238
@scena.Code('AniBtlArts')
def AniBtlArts():
    Call(ScriptId.BtlCom, 'AniBtlArts', (0xFF, 0x1724, 0x0), (0xFF, 0x1725, 0x0), (0xDD, 'NODE_R_ARM'))

    Return()

# id: 0x0062 offset: 0xC260
@scena.Code('AniBtlCharge')
def AniBtlCharge():
    If(
        (
            (Expr.Eval, "BattleCtrl(0x62, 0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_C2F7',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    PlayEffect(0xFFFE, (0xFF, 0x80, 0x0), 0xFFFE, 0x00000103, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)

    Jump('loc_C3D9')

    def _loc_C2F7(): pass

    label('loc_C2F7')

    CameraCtrl(0x00)
    BattleCtrl(0x47)
    BattleCtrl(0x48, 0xFFFE)
    BattleCtrl(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(0xFFFE, (0xFF, 0x80, 0x0), 0xFFFE, 0x00000103, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x00)
    OP_3B(0x00, (0xFF, 0xFD5, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)
    Sleep(1000)

    def _loc_C3D9(): pass

    label('loc_C3D9')

    Return()

# id: 0x0063 offset: 0xC3DC
@scena.Code('AniBtlItem')
def AniBtlItem():
    BattleTargetsIterReset(0xFF, 0xFFFE)
    CameraCtrl(0x00)
    BattleCtrl(0x47)
    BattleCtrl(0x48, 0xFFFE)
    BattleCtrl(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    Sleep(300)
    PlayChrAnimeClip(0xFFFE, 'BTL_ITEM', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)
    SetChrFace(0x03, 0xFFFE, '6', '2', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1724, 0x0), (0xFF, 0x1725, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    Sleep(400)
    PlayEffect(0xFFFE, (0xFF, 0x3F7, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_L_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8B80, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(300)
    BattleCtrl(0x07, 0x00, '')
    BattleCtrl(0x08, 0x00)
    EffectCtrl(0x12, 0xFFFE, 0x03F7)

    Return()

# id: 0x0064 offset: 0xC54C
@scena.Code('AniBtlEscapeVoice0')
def AniBtlEscapeVoice0():
    OP_3B(0x32, (0xFF, 0x172F, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Return()

# id: 0x0065 offset: 0xC590
@scena.Code('AniBtlEscapeVoice1')
def AniBtlEscapeVoice1():
    OP_3B(0x32, (0xFF, 0x1730, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Return()

# id: 0x0066 offset: 0xC5D4
@scena.Code('AniBtlEscapeVoice2')
def AniBtlEscapeVoice2():
    OP_3B(0x32, (0xFF, 0x1731, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Return()

# id: 0x0067 offset: 0xC618
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1743, 0x0), (0xFF, 0x1744, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    Return()

# id: 0x0068 offset: 0xC638
@scena.Code('AniBtlLinkChase')
def AniBtlLinkChase():
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')
    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, 0xFFFE, '6', '2', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_FRONTSTEP', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -2.0, 0.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCtrl(0x3A, 0xFFFE)
    Sleep(200)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.1, 2.0, 0x00, 0x01)
    BattleCtrl(0x3A, 0xFFFE)
    Sleep(166)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '6', '0', '', '#b', '0')
    OP_6C(0xFFFE, 0.3)
    Sleep(166)
    OP_6C(0xFFFE, 1.0)
    Sleep(333)

    If(
        (
            (Expr.Eval, "BattleCtrl(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x1F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C787',
    )

    OP_3B(0x32, (0xFF, 0x174B, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_C87C')

    def _loc_C787(): pass

    label('loc_C787')

    If(
        (
            (Expr.Eval, "BattleCtrl(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x33),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C7E0',
    )

    OP_3B(0x32, (0xFF, 0x174C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_C87C')

    def _loc_C7E0(): pass

    label('loc_C7E0')

    If(
        (
            (Expr.Eval, "BattleCtrl(0x10, 0xFFFE)"),
            (Expr.PushLong, 0x28),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C839',
    )

    OP_3B(0x32, (0xFF, 0x174C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_C87C')

    def _loc_C839(): pass

    label('loc_C839')

    OP_3B(0x32, (0xFF, 0x1745, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_C87C(): pass

    label('loc_C87C')

    PlayEffect(0xFFFE, (0xFF, 0x83, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x85, 0x0), 0xFFFE, 0x00000023, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    OP_3B(0x00, (0xFF, 0x8F5D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F6F, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.1, 0.2, 0.1, 0x001E, 0x0190, 0x003C, 0x0000, 0x0000, 0x00)
    Sleep(66)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x3F8, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCtrl(0x09, 0.01, 0.01, 0.5)
    Sleep(60)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(666)
    PlayChrAnimeClip(0xFFFE, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 2.0, 0x00, 0x01)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurEnd')
    Sleep(200)
    BattleCtrl(0x3A, 0xFFFE)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    Return()

# id: 0x0069 offset: 0xCAE4
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, 0xFFFE, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x006A offset: 0xCB20
@scena.Code('AniBtlLinkRush')
def AniBtlLinkRush():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    SetChrFace(0x03, 0xFFFE, '6', '2[autoM2]', '', '#b', '0')
    ChrClearPhysicsFlags(0xFFFE, 0x00000040)
    ChrClearPhysicsFlags(0xFFFE, 0x00000020)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)

    If(
        (
            (Expr.Eval, "BattleCtrl(0x0F, 0xFFFE, 0x0001)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CB9D',
    )

    Sleep(0)
    BattleCtrl(0x47)
    BattleCtrl(0x4A, 1.3)
    BattleCtrl(0x48, 0xFFFE)
    BattleCtrl(0x46, 0.0, -1.0, 15.0)
    BattleCtrl(0x48, 0xFFFB)
    BattleCtrl(0x46, 0.25, -1.0, 15.0)

    Jump('loc_CBFB')

    def _loc_CB9D(): pass

    label('loc_CB9D')

    If(
        (
            (Expr.Eval, "BattleCtrl(0x0F, 0xFFFE, 0x0001)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CBB8',
    )

    Sleep(200)

    Jump('loc_CBFB')

    def _loc_CBB8(): pass

    label('loc_CBB8')

    If(
        (
            (Expr.Eval, "BattleCtrl(0x0F, 0xFFFE, 0x0001)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CBD3',
    )

    Sleep(400)

    Jump('loc_CBFB')

    def _loc_CBD3(): pass

    label('loc_CBD3')

    If(
        (
            (Expr.Eval, "BattleCtrl(0x0F, 0xFFFE, 0x0001)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CBFB',
    )

    Sleep(1200)
    BattleCtrl(0x48, 0xFFFE)
    BattleCtrl(0x46, 0.5, -1.0, 15.0)

    def _loc_CBFB(): pass

    label('loc_CBFB')

    PlayChrAnimeClip(0xFFFE, 'BTL_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.5, 4.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleCtrl(0x3A, 0xFFFE)
    BattleCtrl(0x48, 0xFFFB)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '6', '0', '', '#b', '0')
    OP_6C(0xFFFE, 0.3)
    Sleep(166)
    OP_6C(0xFFFE, 1.0)
    Sleep(333)
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1770, 0x0), (0xFF, 0x1771, 0x0), (0xFF, 0x1772, 0x0), (0xFF, 0x0, 0x0))
    PlayEffect(0xFFFE, (0xFF, 0x83, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x85, 0x0), 0xFFFE, 0x00000023, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    OP_3B(0x00, (0xFF, 0x8F5D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F6F, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.1, 0.2, 0.1, 0x001E, 0x0190, 0x003C, 0x0000, 0x0000, 0x00)
    Sleep(66)
    CameraCtrl(0x09, 0.01, 0.01, 0.5)
    def _loc_CDF4(): pass

    label('loc_CDF4')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_CE77',
    )

    BattleDamage(0xFFFB, 0xFFFE, 100)
    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x3F8, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(100)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_CDF4')

    def _loc_CE77(): pass

    label('loc_CE77')

    Sleep(666)
    WaitForThreadExit(0xFFFE, 0x02)
    PlayChrAnimeClip(0xFFFE, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 0.1, 0x00, 0x00)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x006B offset: 0xCF08
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x006C offset: 0xCF1C
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x006D offset: 0xCF30
@scena.Code('AniBtlLinkUtmostAttack')
def AniBtlLinkUtmostAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x006E offset: 0xCF44
@scena.Code('AniBtlLinkHeavyCounter')
def AniBtlLinkHeavyCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x006F offset: 0xCF58
@scena.Code('AniBtlLinkRageCounter')
def AniBtlLinkRageCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0070 offset: 0xCF6C
@scena.Code('AniBtlLinkSuperCounter')
def AniBtlLinkSuperCounter():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x0071 offset: 0xCF80
@scena.Code('AniBtlLinkFirstAid')
def AniBtlLinkFirstAid():
    Return()

# id: 0x0072 offset: 0xCF84
@scena.Code('AniBtlLinkBoostArts')
def AniBtlLinkBoostArts():
    Return()

# id: 0x0073 offset: 0xCF88
@scena.Code('AniBtlLinkFirstAid2')
def AniBtlLinkFirstAid2():
    Return()

# id: 0x0074 offset: 0xCF8C
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x0075 offset: 0xCFA8
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x0076 offset: 0xCFC0
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    SetChrFace(0x03, 0xFFFE, '777776', '', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.75)

    Return()

# id: 0x0077 offset: 0xD02C
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    OP_3B(0x32, (0xFF, 0x1721, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Return()

# id: 0x0078 offset: 0xD070
@scena.Code('BtlPluralDamageAnime')
def BtlPluralDamageAnime():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3F8, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x1, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0))

    Return()

# id: 0x0079 offset: 0xD0BC
@scena.Code('BtlPluralDamage')
def BtlPluralDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3F8, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x3, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))

    Return()

# id: 0x007A offset: 0xD108
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x91, 'battle/cr021_00_1.eff')
    LoadEffect(0xFFFE, 0x92, 'battle/cr021_00_2.eff')
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleCtrl(0x8A)
    BattleCtrl(0x47)
    BattleCtrl(0x48, 0xFFFE)
    BattleCtrl(0x46, 0.25, 6.0, 15.0)
    BattleCtrl(0x4B, 0x01F4, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    SetChrFace(0x03, 0xFFFE, '0', '0', '0', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 33.3333, 34.0333, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x1063, 0x0), 0.8, (0xFF, 0x12C, 0x0), 0.0, -5.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x05DC, 0x012C, 0x0000, 0x05DC, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x10BC, 0x0), 0.7, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x05DC, 0x012C, 0x0000, 0x05DC, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1)
    BattleCtrl(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.2, -0.2, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -45.0, 7.0, 0, 0x01)
    CameraSetDistance(0x03, 4.3, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.1, 1.0, -0.2, 3000)
    CameraCtrl(0x16, 0x03, -1.75, 3000)
    CameraCtrl(0x11, 0x03, 1.0, 15.0, 1.0, 0x0BB8, 0x01)
    BattleCtrl(0x4B, 0x0BB8, 0x03)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, 0xFFFE, '1,F000221133333I22266666', '90001BA13102', '000000000000033', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 34.0667, 34.5, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F86, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x0A, 0.016, 0.01, 0.01, 0x0064, 0x0640, 0x03E8, 0x0000, 0x0000, 0x00)
    OP_6C(0xFFFE, 0.15)
    Sleep(1333)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleCtrl(0x47)
    ChrSetPhysicsFlags(0xFFFE, 0x000002A0)
    CameraCtrl(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.4, 0.1, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, 10.0, -30.0, 0, 0x01)
    CameraSetDistance(0x03, 1.2, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.6, -0.4, 3000)
    CameraCtrl(0x16, 0x03, -0.25, 3000)
    CameraCtrl(0x11, 0x03, 2.0, -10.0, 1.0, 0x0BB8, 0x01)
    SetChrFace(0x03, 0xFFFE, '2,226', '2[autoM2]', '3', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 34.1333, 34.5, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.3)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    OP_3B(0x32, (0xFF, 0x1716, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 34.5333, -1.0, -1.0, 0x00, 0x00)
    CameraCtrl(0x0A, 0.03, 0.03, 0.01, 0x001E, 0x0190, 0x03E8, 0x0000, 0x0000, 0x00)
    SetChrFace(0x03, 0xFFFE, '66222', '73110', '3', '#b', '0')
    OP_3B(0x00, (0xFF, 0x108F, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(100)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleCtrl(0x47)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    CameraCtrl(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.75, 1.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -169.0, -3.0, 0, 0x01)
    CameraSetDistance(0x03, 6.2, 0)
    CameraCtrl(0x16, 0x03, -1.5, 3000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.1, 2.5, 3000)
    CameraCtrl(0x11, 0x03, 2.0, -8.0, -1.0, 0x0BB8, 0x01)
    BattleCtrl(0x4B, 0x0BB8, 0x03)
    Fade(0xFF, 0, 0x0000)
    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, -12.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCtrl(0x0A, 0.15, 0.15, 0.01, 0x0064, 0x0258, 0x03E8, 0x0000, 0x0000, 0x00)
    OP_3B(0x00, (0xFF, 0x8F91, 0x0), 0.9, (0xFF, 0x0, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F6A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 0.7, 0.9, 0.8)
    Sleep(233)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'BtlPluralDamage')
    OP_3B(0xFF, 0.3, 0.5, 0.8)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)
    WaitForThreadExit(0xFFFE, 0x02)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    ChrClearPhysicsFlags(0xFFFE, 0x000002A0)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x007B offset: 0xD804
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x90, 'battle/cr021_01_0.eff')
    LoadEffect(0xFFFE, 0x91, 'battle/cr021_01_1.eff')
    LoadEffect(0xFFFE, 0x92, 'battle/cr021_01_2.eff')
    LoadEffect(0xFFFE, 0x93, 'battle/cr021_01_3.eff')
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleCtrl(0x8A)
    BattleCtrl(0x47)
    BattleCtrl(0x48, 0xFFFE)
    BattleCtrl(0x46, 0.25, 6.0, 15.0)
    BattleCtrl(0x4B, 0x01F4, 0x03)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleSaveChrPosition(0xFFFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    ChrSetPhysicsFlags(0xFFFE, 0x000002A0)
    SetChrFace(0x03, 0xFFFE, '2', '2[autoM2]', '0', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 26.6667, 27.1667, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x108F, 0x0), 0.7, (0xFF, 0x12C, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1)
    BattleCtrl(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.1, -0.1, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, -27.0, 8.0, 0, 0x01)
    CameraSetDistance(0x03, 3.6, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.85, -0.2, 3000)
    CameraCtrl(0x11, 0x03, 1.0, -10.0, 1.0, 0x0BB8, 0x01)
    CameraCtrl(0x16, 0x03, -1.25, 3000)
    BattleCtrl(0x4B, 0x0BB8, 0x03)
    Call(ScriptId.Current, 'SpringOff')
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x32, (0xFF, 0x1717, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 27.2, 27.4667, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(333)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 27.5, 28.1667, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.0)
    CameraCtrl(0x0A, 0.05, 0.05, 0.01, 0x001E, 0x00C8, 0x0064, 0x0000, 0x0000, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 2.0, 1.0, 5.0, 0x00, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.05000000074505806, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10F8, 0x0), 0.9, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F5A, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x01, (0xFF, 0x108F, 0x0), (0xFF, 0x1F4, 0x0))
    OP_3B(0xFF, 0.2, 0.2, 0.2)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 2.15, 0.4, 400)
    CameraCtrl(0x16, 0x03, 0.5, 400)
    Sleep(200)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleCtrl(0x47)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x01)
    BattleSetChrPosAsync(0xFFFE, 0xFFF5, 0.0, 0.0, -0.3, -1.0, 0x00, 0x01)
    ChrSetPhysicsFlags(0xFFFE, 0x000003A0)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.6)
    SetChrFace(0x03, 0xFFFE, '026', '01337', '0', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFE, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 10.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCtrl(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 4.9, 0.4, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -7.0, -15.0, -10.0, 0, 0x01)
    CameraSetDistance(0x03, 2.0, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 5.3, 0.2, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -9.0, -22.0, -10.0, 1000, 0x01)
    CameraCtrl(0x16, 0x03, -0.65, 1000)
    CameraCtrl(0x0A, 0.035, 0.02, 0.01, 0x0000, 0x05DC, 0x03E8, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0000, 0.12, 0x0000, 0x05DC, 0x03E8, 0.3, 0xFFFF, -9000.0, -9000.0, -9000.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 27.8667, 28.1333, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.5)
    Fade(0xFF, 0, 0x0000)
    Sleep(500)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 28.4, 28.8333, -1.0, 0x00, 0x00)
    Sleep(166)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleCtrl(0x47)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x01)
    BattleSetChrPosAsync(0xFFFE, 0xFFF5, 0.0, 0.0, -0.0, -1.0, 0x00, 0x01)
    EffectCtrl(0x0F, 0xFFFE, 0x0093, 0x01)
    CameraCtrl(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 4.85, 0.8, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, -150.0, 20.0, 0, 0x01)
    CameraSetDistance(0x03, 5.8, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 0.4, 600)
    CameraCtrl(0x11, 0x03, 6.0, -4.0, -2.0, 0x0258, 0x01)
    CameraCtrl(0x16, 0x03, 9.0, 600)
    BattleCtrl(0x4B, 0x0258, 0x03)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 28.2667, 28.5, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.5)
    Fade(0xFF, 0, 0x0000)
    OP_3B(0x32, (0xFF, 0x1718, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 28.5333, 28.8333, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 0.0, 3000)
    CameraCtrl(0x11, 0x03, 2.0, -4.0, -2.0, 0x0BB8, 0x01)
    CameraCtrl(0x16, 0x03, 2.0, 3000)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 28.8667, -1.0, -1.0, 0x00, 0x00)
    CameraCtrl(0x0A, 0.32, 0.22, 0.01, 0x001E, 0x05DC, 0x03E8, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0002, 0.3, 0x001E, 0x05DC, 0x03E8, 0.4, 0xFFFF, -9000.0, -9000.0, -9000.0)
    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.05000000074505806, 0x0), (0xEE, 0.5, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F07, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x010E, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F52, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x014A, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 0.7, 0.9, 0.9)
    Sleep(66)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'BtlPluralDamageAnime')
    OP_3B(0xFF, 0.3, 0.5, 0.7)
    Sleep(466)
    WaitForThreadExit(0xFFFE, 0x02)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'BtlPluralDamage')
    OP_3B(0xFF, 0.3, 0.5, 0.7)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1333)
    WaitForThreadExit(0xFFFE, 0x02)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    ChrClearPhysicsFlags(0xFFFE, 0x000003A0)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x007C offset: 0xE18C
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x90, 'battle/cr021_02_0.eff')
    BattleTargetsIterReset(0x00, 0xFFFE)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCtrl(0x47)
    CameraCtrl(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.35, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 12.0, 9.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 3.25, 0)
    CameraCtrl(0x0C, 0x03, 0.0, -0.15, 0.0, 8000)
    CameraCtrl(0x11, 0x03, -5.0, 22.0, 0.0, 0x1F40, 0x01)
    CameraCtrl(0x16, 0x03, -2.0, 3000)
    BattleCtrl(0x4B, 0x1F40, 0x03)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, 0xFFFE, '3', '2[autoM2]', '0', '#b', '0')
    Fade(0xFF, 0, 0x0000)
    SetChrFace(0x03, 0xFFFE, '3773', '2[autoM2]', '0', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F39, 0x0), 0.9, (0xFF, 0x64, 0x0), 0.0, -1.5, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x32, (0xFF, 0x1719, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1833)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.2)
    SetChrFace(0x03, 0xFFFE, '6662', '733131313333', '0', '#b', '0')
    CameraCtrl(0x0A, 0.008, 0.008, 0.0, 0x03E8, 0x03E8, 0x01F4, 0x0000, 0x0000, 0x00)
    CameraCtrl(0x16, 0x03, 1.0, 450)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 450)
    CameraCtrl(0x0A, 0.07, 0.07, 0.01, 0x0064, 0x0384, 0x04B0, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0002, 0.35, 0x003C, 0x0578, 0x0320, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    Sleep(233)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    OP_3B(0x00, (0xFF, 0x107D, 0x0), 0.9, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x0190, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x01, (0xFF, 0x8F39, 0x0), (0xFF, 0x1F4, 0x0))
    OP_3B(0x32, (0xFF, 0x171A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(233)
    CameraCtrl(0x16, 0x03, 2.0, 4000)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 4000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.1, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    Sleep(1833)
    SetChrFace(0x03, 0xFFFE, '333332', '2', '0', '#b', '0')
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x007D offset: 0xE5AC
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    AnimeClipCtrl(0x04, 0xFFFE, 'C_CHR021_SC1', '')
    BattleCtrl(0x52, 0xFFFE, 0x90)
    LoadEffect(0xFFFE, 0x91, 'battle/sc021_00_01.eff')
    LoadEffect(0xFFFE, 0x92, 'battle/sc021_00_02.eff')
    LoadEffect(0xFFFE, 0x93, 'battle/sc021_00_03.eff')
    LoadEffect(0xFFFE, 0x94, 'battle/sc021_00_04.eff')
    LoadEffect(0xFFFE, 0x95, 'battle/sc021_00_05.eff')
    LoadEffect(0xFFFE, 0x96, 'battle/sc021_00_06.eff')
    LoadEffect(0xFFFE, 0x97, 'battle/sc021_00_07.eff')
    LoadEffect(0xFFFE, 0x98, 'battle/sc021_00_08.eff')
    LoadEffect(0xFFFE, 0x99, 'battle/sc021_00_09.eff')
    LoadEffect(0xFFFE, 0x9A, 'battle/sc021_00_10.eff')
    LoadEffect(0xFFFE, 0x9B, 'battle/sc021_00_11.eff')
    LoadEffect(0xFFFE, 0x9C, 'battle/sc021_00_12.eff')
    LoadEffect(0xFFFE, 0x9D, 'battle/sc021_00_13.eff')
    LoadEffect(0xFFFE, 0x9E, 'battle/sc021_00_15.eff')
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x1012, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_C0(0x0002, 1.65)
    ChrClearPhysicsFlags(0xFFFE, 0x00000040)
    ChrClearPhysicsFlags(0xFFFE, 0x00000020)
    ChrSetPhysicsFlags(0xFFFE, 0x00000100)
    ChrSetPhysicsFlags(0xFFFE, 0x000002A0)
    ChrSetPhysicsFlags(0xFFF9, 0x000002A0)
    SetChrPos(0xFFFE, 0.0, 0.0, -50.0, 0.0)
    SetChrPos(0xFFEA, 0.0, 0.0, 0.0, 0.0)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, -1.0, 0.5)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    BattleCtrl(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000578, 0x00000000)
    BattleCreateChrDummy(0xFFFE, 3)
    AnimeClipCtrl(0x04, 0x0B5F, 'C_CHR021_SC1', '')
    AnimeClipCtrl(0x04, 0x0B60, 'C_CHR021_SC1', '')
    OP_38(0x0B5F, 0x00, 0x00, 'AniAttachMainWeapon')
    OP_38(0x0B60, 0x00, 0x00, 'AniAttachMainWeapon')
    ChrClearPhysicsFlags(0x0B68, 0x00000040)
    ChrClearPhysicsFlags(0x0B68, 0x00000020)
    ChrSetPhysicsFlags(0x0B69, 0x00000040)
    ChrSetPhysicsFlags(0x0B69, 0x00000020)
    ChrSetPhysicsFlags(0x0B6A, 0x00000040)
    ChrSetPhysicsFlags(0x0B6A, 0x00000020)
    def _loc_E8F3(): pass

    label('loc_E8F3')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_E91E',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFEA, -1.0, 0.5)
    BattleTargetsIterNext(0xFFFE)
    Sleep(1)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_E8F3')

    def _loc_E91E(): pass

    label('loc_E91E')

    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('SpringOn', 0x000B)
    Fade(0x64, 1000, 1.0, 0x0000)
    Sleep(0)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    CameraSetPos(0x03, -0.26, 1.37, -50.07, 0)
    CameraRotate(0x03, 0.0, 359.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.4, 0)
    CameraCtrl(0x0B, 0x03, 40.0, 0x0000)
    CameraCtrl(0x02, 0x02, -0.26, 1.25, -50.07, 3000)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.75)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x19B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EA35',
    )

    OP_3B(0x32, (0xFF, 0x171C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_EA78')

    def _loc_EA35(): pass

    label('loc_EA35')

    OP_3B(0x32, (0xFF, 0x171B, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_EA78(): pass

    label('loc_EA78')

    Sleep(333)
    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_L_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F96, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrFace(0x03, 0xFFFE, '3', '4[autoM4]', '', '#b', '0')
    Sleep(666)
    PlayEffect(0xFFFE, (0xFF, 0x94, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x06)
    Sleep(500)
    CameraSetPos(0x03, -0.16, 1.53, -50.03, 1000)
    CameraRotate(0x03, 354.0, 13.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 0.8, 1000)
    CameraCtrl(0x0B, 0x03, 32.0, 0x03E8)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F72, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrFace(0x03, 0xFFFE, '6', '2[autoM2]', '4', '#b', '0')
    Sleep(666)
    OP_6C(0xFFFE, 0.5)
    Sleep(333)
    CameraCtrl(0x02, 0x02, -0.56, 0.82, -50.1, 500)
    CameraCtrl(0x04, 0x02, 353.0, 342.0, 1.0, 500, 0x01)
    CameraCtrl(0x05, 0x02, 2.2, 500)
    CameraCtrl(0x0B, 0x02, 57.2, 0x01F4)
    SetChrFace(0x03, 0xFFFE, '6', '2[autoM2]', '6', '#b', '0')
    OP_6C(0xFFFE, 1.0)
    CameraCtrl(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x012C, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 0.2)
    PlayEffect(0xFFFE, (0xFF, 0x95, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F71, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F37, 0x0), 0.9, (0xFF, 0xC8, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPos(0x03, -0.14, 1.33, -50.4, 500)
    CameraRotate(0x03, 1.0, 7.0, 0.0, 500, 0x01)
    CameraSetDistance(0x03, 1.4, 500)
    CameraCtrl(0x0B, 0x03, 57.2, 0x01F4)
    SetChrFace(0x03, 0xFFFE, '6', '2[autoM2]', '5', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F2E, 0x0), 0.9, (0xFF, 0xC8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(833)
    OP_6C(0xFFFE, 0.0)
    OP_6C(0xFFFE, 1.0)
    CameraCtrl(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x012C, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 0.2)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, -0.014000000432133675, 0x0), (0xEE, 1.4559999704360962, 0x0), (0xEE, -4.0, 0x0), -1.7, -5.346, 139.852, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F02, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F62, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x32, (0xFF, 0x1771, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrFace(0x03, 0xFFFE, '6', '6[autoM6]', '0', '#b', '0')
    CameraSetPos(0x03, -0.59, 0.87, -49.3, 100)
    CameraRotate(0x03, 9.0, 22.0, 0.0, 100, 0x01)
    CameraSetDistance(0x03, 2.4, 100)
    CameraCtrl(0x0B, 0x03, 57.2, 0x0064)
    Sleep(333)
    CameraSetPos(0x03, -2.09, 0.04, -47.31, 1000)
    CameraRotate(0x03, 11.0, 18.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 4.8, 1000)
    CameraCtrl(0x0B, 0x03, 57.2, 0x03E8)
    CameraCtrl(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x012C, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 0.2)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, -0.041999999433755875, 0x0), (0xEE, 1.465000033378601, 0x0), (0xEE, -2.0, 0x0), -4.275, -0.173, 179.188, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F62, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraCtrl(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x012C, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 0.2)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, -0.0010000000474974513, 0x0), (0xEE, 1.3200000524520874, 0x0), (0xEE, 0.03099999949336052, 0x0), -4.547, 0.105, -144.138, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F62, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    EffectCtrl(0x0E, 0xFFFE, 0x06, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    CameraSetPos(0x03, 0.12, 0.59, -48.53, 0)
    CameraRotate(0x03, 8.0, 134.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 3.1, 0)
    CameraCtrl(0x0B, 0x03, 57.2, 0x0000)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    EffectCtrl(0x0F, 0xFFFE, 0x0096, 0x01)
    CameraSetPos(0x03, 0.33, 0.58, -49.26, 1000)
    ChrClearPhysicsFlags(0x0B5E, 0x00000040)
    ChrClearPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5E, 0x00000200)
    ChrSetRGBA(0x0B5E, 1.0, 1.0, 1.0, 0.0, 0, 0x03)
    BattleSetChrPosAsync(0x0B5E, 0xFFFF, 0.0, 0.0, -45.0, -1.0, 0x00, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0x0B5E, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F62, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_05', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F37, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(0)
    BattleSetChrPosAsync(0x0B5E, 0xFFFF, 0.0, 0.0, 0.0, 5.0, 0x03, 0x01)
    OP_6C(0xFFFE, 0.4)
    Sleep(833)
    CameraCtrl(0x02, 0x02, 0.18, 1.05, -50.15, 700)
    CameraCtrl(0x04, 0x02, 357.0, 85.0, 0.0, 700, 0x01)
    CameraCtrl(0x05, 0x02, 1.1, 700)
    CameraCtrl(0x0B, 0x02, 38.9, 0x02BC)
    SetChrAniFunction(0xFFFE, 0x00, 'AniEvSCraft00_6', -1.0, 1.0, 0x00000000)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x97, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 0.5, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.5, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 2.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10F8, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F28, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x32, (0xFF, 0x171D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(250)
    CameraSetPos(0x03, -0.26, 1.05, -55.21, 700)
    CameraRotate(0x03, 357.0, 85.0, 0.0, 700, 0x01)
    CameraSetDistance(0x03, 11.0, 700)
    CameraCtrl(0x0B, 0x03, 38.9, 0x02BC)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, -50.0, -1.0, 0x01, 0x01)
    BattleSetChrPosAsync(0x0B5E, 0x0B5E, 0.0, 0.0, 0.0, 0.0, 0x00, 0x01)
    SetChrPos(0x0B5E, 0.0, 1.0, -30.0, 0.0)
    BattleSetChrPosAsync(0x0B5E, 0x0B5E, 0.0, 0.0, -70.0, 7.0, 0x00, 0x01)
    Sleep(350)
    PlayEffect(0xFFFE, (0xFF, 0x97, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(350)
    CameraSetPos(0x03, 0.43, 1.09, -42.0, 500)
    CameraRotate(0x03, 1.0, 174.0, 0.0, 600, 0x01)
    CameraSetDistance(0x03, 3.7, 600)
    CameraCtrl(0x0B, 0x03, 22.8, 0x0258)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_07', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, 18.8333, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F2E, 0x0), 0.9, (0xFF, 0xC8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_6C(0xFFFE, 0.5)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, 0.0, 7.0, 0x01, 0x01)
    Sleep(400)
    CameraCtrl(0x02, 0x01, -0.25, 0.49, 0.0, 800)
    Sleep(400)
    CameraRotate(0x03, 4.0, 69.0, 0.0, 1500, 0x01)
    CameraSetDistance(0x03, 30.5, 1500)
    CameraCtrl(0x0B, 0x03, 22.8, 0x05DC)
    ChrClearPhysicsFlags(0x0B5F, 0x00000040)
    ChrClearPhysicsFlags(0x0B5F, 0x00000020)
    ChrClearPhysicsFlags(0x0B60, 0x00000040)
    ChrClearPhysicsFlags(0x0B60, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetPhysicsFlags(0x0B60, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000200)
    ChrSetPhysicsFlags(0x0B60, 0x00000200)
    BattleSetChrPosAsync(0x0B5F, 0xFFFF, 0.0, 0.0, -26.0, -1.0, 0x00, 0x01)
    BattleSetChrPosAsync(0x0B60, 0xFFFF, 0.0, 0.0, -25.0, -1.0, 0x00, 0x01)
    BattleTurnChrDirection(0x0B5F, 0xFFFF, -1.0, 0.5)
    BattleTurnChrDirection(0x0B60, 0xFFFF, -1.0, 0.5)
    ChrSetRGBA(0x0B5F, 0.7, 0.8, 1.0, 0.7, 0, 0x03)
    ChrSetRGBA(0x0B60, 0.7, 0.8, 1.0, 0.7, 0, 0x03)
    PlayChrAnimeClip(0x0B5F, 'BTL_S_CRAFT00_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B60, 'BTL_S_CRAFT00_09', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    OP_6C(0x0B60, 2.0)
    Sleep(0)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, -2.0, 5.0, 0x00, 0x01)
    BattleSetChrPosAsync(0x0B5F, 0xFFFF, 0.0, 0.0, 20.0, 9.0, 0x00, 0x01)
    BattleSetChrPosAsync(0x0B60, 0xFFFF, 0.0, 0.0, 19.0, 8.0, 0x00, 0x01)
    Sleep(166)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlSCraft00_sub2')
    Sleep(100)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_07', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -0.0333333, -0.0333333, 0.5, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F07, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    BattleCtrl(0x3A, 0xFFFE)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 0.0, 20.0, 5.0, 0x02, 0x01)
    Sleep(300)
    CameraSetDistance(0x03, 40.5, 500)
    BattleSetChrPos(0x0B5E, 0xFFFF, 0.0, 0.0, -20.0, 0.0, 0x00, 0x01)
    BattleSetChrPosAsync(0x0B5E, 0xFFFF, 0.0, 0.0, 0.0, 10.0, 0x00, 0x01)
    BattleCtrl(0x3A, 0x0B5E)
    EffectCtrl(0x0F, 0xFFFE, 0x0092, 0x01)
    CameraCtrl(0x0A, 1.0, 1.4, 0.0, 0x0000, 0x00C8, 0x012C, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 0.6)
    PlayEffect(0xFFFE, (0xFF, 0x9A, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, -0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.2999999523162842, 0x0), (0xEE, 1.2999999523162842, 0x0), (0xEE, 1.2999999523162842, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F1C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F83, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1000)
    CameraSetPos(0x03, -1.06, 0.58, 9.45, 0)
    CameraRotate(0x03, 351.0, 158.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.4, 0)
    CameraCtrl(0x0B, 0x03, 22.8, 0x0000)
    ChrSetPhysicsFlags(0x0B5E, 0x00000040)
    ChrSetPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000040)
    ChrSetPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetPhysicsFlags(0x0B60, 0x00000040)
    ChrSetPhysicsFlags(0x0B60, 0x00000020)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, 8.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, 0.0, -1.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x9C, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_UP'), (0xEE, 0.0, 0x0), (0xEE, 0.4000000059604645, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 0.0, -3.0, 0.75, 0x02, 0x01)
    OP_6C(0xFFFE, 0.666)
    Sleep(333)
    OP_3B(0x00, (0xFF, 0x8F7A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(666)
    OP_6C(0xFFFE, 0.0)
    EffectCtrl(0x0F, 0xFFFE, 0x0099, 0x01)
    CameraCtrl(0x02, 0x02, -0.61, -1.6, 9.13, 1000)
    CameraCtrl(0x04, 0x02, 327.0, 195.0, 0.0, 1000, 0x01)
    CameraCtrl(0x05, 0x02, 13.6, 1000)
    CameraCtrl(0x0B, 0x02, 22.8, 0x03E8)
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 90.0, 0.0, 0.0, (0xEE, 0.5, 0x0), (0xEE, 0.5, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_6C(0xFFFE, 1.5)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    PlayEffect(0xFFFE, (0xFF, 0x9B, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10ED, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x32, (0xFF, 0x171E, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_11', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.0)
    Sleep(300)
    OP_3B(0x00, (0xFF, 0x8F02, 0x0), 0.8, (0xFF, 0x12C, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    EffectCtrl(0x0F, 0xFFFE, 0x0099, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    OP_3B(0x00, (0xFF, 0x8B7D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(500)
    ChrSetPhysicsFlags(0xFFFE, 0x00000200)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 40.0, 10.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, 0.0, -1.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.43, 1.68, 2.3, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -27.0, 21.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 7.3, 0)
    CameraCtrl(0x0B, 0x03, 22.8, 0x0000)
    ReleaseEffect(0xFFFE, 0x95)
    LoadEffect(0xFFFE, 0x95, 'battle/sc021_00_16.eff')
    ReleaseEffect(0xFFFE, 0x93)
    LoadEffect(0xFFFE, 0x93, 'battle/sc021_00_14.eff')
    Sleep(1000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.43, 1.68, 2.3, 1500)
    CameraRotateByTarget(0xFFFE, '', 0x03, -27.0, 21.0, 0.0, 1500, 0x01)
    CameraSetDistance(0x03, 2.4, 1500)
    CameraCtrl(0x0B, 0x03, 22.8, 0x05DC)
    SetChrFace(0x03, 0xFFFE, '6[autoE6]', '6[autoM6]', '0', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_12', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x9D, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 1.5, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F1A, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, 4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x017C, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    OP_3B(0x32, (0xFF, 0x171F, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    EffectCtrl(0x0F, 0xFFFE, 0x0099, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), -90.0, 0.0, 0.0, (0xEE, 2.0, 0x0), (0xEE, 2.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F39, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x10E8, 0x0), 1.0, (0xFF, 0xC8, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrFace(0x03, 0xFFFE, '6[autoE6]', '137', '5', '#b', '0')
    CameraCtrl(0x00)
    CameraCtrl(0x14, 0x02, 0xFFFE, '', 0.39, 1.72, 2.27, 500)
    CameraRotateByTarget(0xFFFE, '', 0x02, -26.0, 28.0, 0.0, 500, 0x01)
    CameraCtrl(0x05, 0x02, 0.8, 500)
    CameraCtrl(0x0B, 0x02, 22.8, 0x01F4)
    Sleep(400)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.82, 1.44, 2.82, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 62.0, 140.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 1.5, 1000)
    CameraCtrl(0x0B, 0x03, 64.3, 0x03E8)
    OP_5C(0xFFFE, 0x00, 'Root')
    OP_5D(0xFFFE, 'Root', 0.0, 0.0, 0.0, 90.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x05DC, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x97, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 90.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x06)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_13', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Sleep(500)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlSCraft00_sub1')
    CameraCtrl(0x05, 0x00, 1.0, 1200)
    CameraCtrl(0x0A, 0.0, 0.1, 0.0, 0x0064, 0x03E8, 0x0064, 0x0000, 0x0000, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 10.0, 10.0, 5.0, 0x01, 0x01)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x97, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 90.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(250)
    OP_3B(0x32, (0xFF, 0x1720, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    BattleCtrl(0x3A, 0xFFFE)
    OP_1F(0xFFFE, 0x02)
    BattleSetChrPosAsync(0xFFFE, 0xFFFF, 0.0, 0.0, 20.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, 0.0, -1.0)
    OP_5C(0xFFFE, 0x01, 'Root')
    CameraCtrl(0x00)
    CameraSetPos(0x03, -0.47, 0.63, 17.46, 0)
    CameraRotate(0x03, 342.0, 172.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.3, 0)
    CameraCtrl(0x0B, 0x03, 64.3, 0x0000)
    CameraCtrl(0x0A, 0.0, 0.0, 0.0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_14', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x95, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.39800000190734863, 0x0), (0xEE, 0.0, 0x0), (0xEE, 2.993000030517578, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(333)
    OP_3B(0xFF, 0.7, 1.0, 0.6)
    CameraCtrl(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x0064, 0x0000, 0x0000, 0x00)
    OP_3B(0x00, (0xFF, 0x8F07, 0x0), 1.2, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0708, 0x012C, 0x0000, 0x0708, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x108E, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(266)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 1.23, 0.74, 3.28, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -9.0, 140.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.6, 0)
    CameraCtrl(0x0B, 0x03, 39.7, 0x0000)
    CameraCtrl(0x14, 0x02, 0xFFFE, '', 0.82, 0.74, 3.25, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x02, -8.0, 164.0, 0.0, 4000, 0x01)
    CameraCtrl(0x05, 0x02, 2.6, 4000)
    CameraCtrl(0x0B, 0x02, 39.7, 0x0FA0)
    PlayEffect(0xFFFE, (0xFF, 0x9E, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_UP'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F4B, 0x0), 0.7, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    EffectCtrl(0x0F, 0xFFFE, 0x0099, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 2.0, 0x0), 0xFF)
    OP_3B(0xFF, 0.7, 1.0, 0.8)
    CameraCtrl(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x08FC, 0x03E8, 0x0000, 0x0000, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlSCraftDamage')
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_14a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0xFF, 0.7, 1.0, 0.8)
    Sleep(600)
    OP_3B(0x00, (0xFF, 0x8FAC, 0x0), 0.55, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0708, 0x010E, 0x0000, 0x0708, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x10FA, 0x0), 0.7, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x0190, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F52, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x05DC, 0x012C, 0x0000, 0x05DC, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0x03, 2000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    OP_04(0x0B, 'AniBtlSCraft00_finish')

    Return()

# id: 0x007E offset: 0x10850
@scena.Code('AniBtlSCraft00_finish')
def AniBtlSCraft00_finish():
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(0xFFFE, 0x02)
    Call(ScriptId.Current, 'BtlDefaultFace')
    AnimeClipCtrl(0x05, 0xFFFE, 'C_CHR021_SC1', '')
    ChrClearPhysicsFlags(0xFFFE, 0x00000100)
    ChrClearPhysicsFlags(0xFFFE, 0x000002A0)
    ChrClearPhysicsFlags(0xFFF9, 0x000002A0)
    ReleaseEffect(0xFFFE, 0x90)
    ReleaseEffect(0xFFFE, 0x91)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    Call(ScriptId.Current, 'SpringOn')
    OP_5C(0xFFFE, 0x01, 'Root')
    CameraCtrl(0x10)
    BattleDeleteTempChar(0xFFFF)
    BattleCtrl(0x18)
    BattleCtrl(0x6C, 0x0001)
    Sleep(1)
    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x007F offset: 0x10924
@scena.Code('AniBtlSCraftDamage')
def AniBtlSCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3F8, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x1, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))

    Return()

# id: 0x0080 offset: 0x10970
@scena.Code('AniBtlSCraft00_sub1')
def AniBtlSCraft00_sub1():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_10997',
    )

    CameraCtrl(0x14, 0x00, 0xFFFE, '', 0.82, 1.44, 2.82, 1)
    Sleep(0)

    Jump('AniBtlSCraft00_sub1')

    def _loc_10997(): pass

    label('loc_10997')

    Return()

# id: 0x0081 offset: 0x10998
@scena.Code('AniBtlSCraft00_sub2')
def AniBtlSCraft00_sub2():
    Sleep(266)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, -0.057999998331069946, 0x0), (0xEE, 1.2910000085830688, 0x0), (0xEE, 0.45899999141693115, 0x0), 1.802, -1.003, 144.012, (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), 0xFF)
    Sleep(66)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0x0B5F, 0x00000003, (0xDD, ''), (0xEE, -0.07900000363588333, 0x0), (0xEE, 1.4220000505447388, 0x0), (0xEE, 0.8799999952316284, 0x0), 0.543, 0.372, 38.043, (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), 0xFF)
    Sleep(66)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0x0B60, 0x00000003, (0xDD, ''), (0xEE, -0.029999999329447746, 0x0), (0xEE, 1.2289999723434448, 0x0), (0xEE, 0.6159999966621399, 0x0), -4.536, 0.728, -179.979, (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), 0xFF)
    Sleep(33)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0x0B60, 0x00000003, (0xDD, ''), (0xEE, -0.029999999329447746, 0x0), (0xEE, 1.2289999723434448, 0x0), (0xEE, 0.6159999966621399, 0x0), -175.464, -0.728, 0.021, (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), (0xEE, 2.5, 0x0), 0xFF)
    OP_04(0x0B, 'AniBtlSCraftDamage')

    Return()

# id: 0x0082 offset: 0x10AC8
@scena.Code('AniEvIdle')
def AniEvIdle():
    PlayChrAnimeClip(0xFFFE, 'IDLE', 0x00, 0x01, 0x00, 0x01, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0083 offset: 0x10B10
@scena.Code('AniEvWait')
def AniEvWait():
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0084 offset: 0x10B38
@scena.Code('AniEvWalk')
def AniEvWalk():
    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0085 offset: 0x10B60
@scena.Code('AniEvRun')
def AniEvRun():
    PlayChrAnimeClip(0xFFFE, 'RUN', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0086 offset: 0x10B88
@scena.Code('AniEvDash')
def AniEvDash():
    PlayChrAnimeClip(0xFFFE, 'DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0087 offset: 0x10BB8
@scena.Code('AniEvSquat')
def AniEvSquat():
    Call(ScriptId.CurrentCharacter, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_10C27',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_10CD4')

    def _loc_10C27(): pass

    label('loc_10C27')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_10C86',
    )

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'SQUAT', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_10CD4')

    def _loc_10C86(): pass

    label('loc_10C86')

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'SQUAT', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SQUATa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_10CD4(): pass

    label('loc_10CD4')

    Return()

# id: 0x0088 offset: 0x10CD8
@scena.Code('AniEvFall')
def AniEvFall():
    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'FALL', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0089 offset: 0x10D08
@scena.Code('AniEvLand')
def AniEvLand():
    OP_80(0.05)
    PlayChrAnimeClip(0xFFFE, 'LAND', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x008A offset: 0x10D54
@scena.Code('AniEvFieldAttackEnd')
def AniEvFieldAttackEnd():
    PlayChrAnimeClip(0xFFFE, 'DISARM', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x753A, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(666)
    OP_3B(0x00, (0xFF, 0x7536, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7537, 0x0), 0.3, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(600)
    ChrClearPhysicsFlags(0xFFFE, 0x00000010)
    Call(ScriptId.Current, 'EraseEquip')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x008B offset: 0x10E84
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x008C offset: 0x10EC0
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x008D offset: 0x10EEC
@scena.Code('AniEvBtlDash')
def AniEvBtlDash():
    PlayChrAnimeClip(0xFFFE, 'BTL_DASH', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x008E offset: 0x10F20
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x008F offset: 0x10F4C
@scena.Code('AniEvAttack')
def AniEvAttack():
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0090 offset: 0x10FA8
@scena.Code('AniEvDamage')
def AniEvDamage():
    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0091 offset: 0x11004
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0092 offset: 0x1107C
@scena.Code('AniEvGuard')
def AniEvGuard():
    PlayChrAnimeClip(0xFFFE, 'BTL_GUARD', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0093 offset: 0x110AC
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(0xFFFE, 'BTL_ARIA', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0094 offset: 0x110D8
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTS', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTSa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0095 offset: 0x11130
@scena.Code('AniEvBackStep')
def AniEvBackStep():
    PlayChrAnimeClip(0xFFFE, 'BTL_BACKSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0096 offset: 0x1118C
@scena.Code('AniEvDead')
def AniEvDead():
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0097 offset: 0x111E4
@scena.Code('AniEvDead1')
def AniEvDead1():
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

@scena.Code('AniEvDead2')
def AniEvDead2():
    Call(ScriptId.Current, 'AniDetachMainWeapon')
    Call(ScriptId.Current, 'SpringOff')
    # SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'EV79000', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0098 offset: 0x11214
@scena.Code('AniEvItem')
def AniEvItem():
    PlayChrAnimeClip(0xFFFE, 'BTL_ITEM', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0099 offset: 0x1126C
@scena.Code('AniEvFrontStep')
def AniEvFrontStep():
    PlayChrAnimeClip(0xFFFE, 'BTL_FRONTSTEP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x009A offset: 0x112C8
@scena.Code('AniEvBtlSleep')
def AniEvBtlSleep():
    PlayChrAnimeClip(0xFFFE, 'BTL_SLEEP', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x009B offset: 0x112F8
@scena.Code('AniEvWeak')
def AniEvWeak():
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x009C offset: 0x11324
@scena.Code('AniEvWin')
def AniEvWin():
    PlayChrAnimeClip(0xFFFE, 'BTL_WIN', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(800)
    PlayEffect(0xFFFE, (0xFF, 0x85, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, -0.20000000298023224, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.8999999761581421, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WINa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.6, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.8)

    Return()

# id: 0x009D offset: 0x113C0
@scena.Code('AniEvLevelUp')
def AniEvLevelUp():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_LEVELUP', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_LEVELUPa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x009E offset: 0x11430
@scena.Code('AniEvHorseWait')
def AniEvHorseWait():
    PlayChrAnimeClip(0xFFFE, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x009F offset: 0x11454
@scena.Code('AniEvHorseWalk')
def AniEvHorseWalk():
    PlayChrAnimeClip(0xFFFE, 'HORSE_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A0 offset: 0x1147C
@scena.Code('AniEvHorseRun')
def AniEvHorseRun():
    PlayChrAnimeClip(0xFFFE, 'HORSE_RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A1 offset: 0x114A4
@scena.Code('AniEvHorseStop')
def AniEvHorseStop():
    PlayChrAnimeClip(0xFFFE, 'HORSE_STOP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A2 offset: 0x114F4
@scena.Code('AniEvHorseTurnRight')
def AniEvHorseTurnRight():
    PlayChrAnimeClip(0xFFFE, 'HORSE_TURN_R', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A3 offset: 0x11544
@scena.Code('AniEvHorseTurnLeft')
def AniEvHorseTurnLeft():
    PlayChrAnimeClip(0xFFFE, 'HORSE_TURN_L', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'HORSE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A4 offset: 0x11594
@scena.Code('AniEvHorseDash')
def AniEvHorseDash():
    PlayChrAnimeClip(0xFFFE, 'HORSE_DASH', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x00A5 offset: 0x115BC
@scena.Code('AniEvSCraft00')
def AniEvSCraft00():
    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'ShowEquip')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A6 offset: 0x11618
@scena.Code('AniEvSCraft00_1')
def AniEvSCraft00_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A7 offset: 0x1169C
@scena.Code('AniEvSCraft00_2')
def AniEvSCraft00_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A8 offset: 0x116EC
@scena.Code('AniEvSCraft00_3')
def AniEvSCraft00_3():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00A9 offset: 0x1173C
@scena.Code('AniEvSCraft00_4')
def AniEvSCraft00_4():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AA offset: 0x1178C
@scena.Code('AniEvSCraft00_5')
def AniEvSCraft00_5():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_05', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AB offset: 0x117DC
@scena.Code('AniEvSCraft00_6')
def AniEvSCraft00_6():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AC offset: 0x11860
@scena.Code('AniEvSCraft00_7')
def AniEvSCraft00_7():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_07', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AD offset: 0x118B0
@scena.Code('AniEvSCraft00_8')
def AniEvSCraft00_8():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AE offset: 0x11900
@scena.Code('AniEvSCraft00_9')
def AniEvSCraft00_9():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_09', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00AF offset: 0x11950
@scena.Code('AniEvSCraft00_10')
def AniEvSCraft00_10():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_10', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_10a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B0 offset: 0x119D4
@scena.Code('AniEvSCraft00_11')
def AniEvSCraft00_11():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_11', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B1 offset: 0x11A24
@scena.Code('AniEvSCraft00_12')
def AniEvSCraft00_12():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_12', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B2 offset: 0x11A74
@scena.Code('AniEvSCraft00_13')
def AniEvSCraft00_13():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_13', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B3 offset: 0x11AC4
@scena.Code('AniEvSCraft00_14')
def AniEvSCraft00_14():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_14', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_14a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B4 offset: 0x11B48
@scena.Code('AniEvCraft00')
def AniEvCraft00():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 33.3333, 34.5, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B5 offset: 0x11B94
@scena.Code('AniEvCraft00_1')
def AniEvCraft00_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 34.5333, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B6 offset: 0x11C14
@scena.Code('AniEvCraft01')
def AniEvCraft01():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 26.6667, 27.4667, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B7 offset: 0x11C60
@scena.Code('AniEvCraft01_1')
def AniEvCraft01_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 27.5, 28.2, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B8 offset: 0x11CAC
@scena.Code('AniEvCraft01_2')
def AniEvCraft01_2():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 28.2333, 28.3667, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00B9 offset: 0x11D2C
@scena.Code('AniEvCraft02')
def AniEvCraft02():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BA offset: 0x11D78
@scena.Code('AniEvCraft02_1')
def AniEvCraft02_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BB offset: 0x11DF8
@scena.Code('AniBtlCrucifixion')
def AniBtlCrucifixion():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BC offset: 0x11E2C
@scena.Code('AniBtlFloat')
def AniBtlFloat():
    OP_45(0xFFFE, 0.0, 60.0, 0.0, 0x012C, 0x0000)
    SetEndhookFunction('AniBtlFloat_End', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_FLOAT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00BD offset: 0x11E80
@scena.Code('AniBtlFloat_End')
def AniBtlFloat_End():
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)

    Return()

# id: 0x00BE offset: 0x11EB0
@scena.Code('SitWaitSwitch')
def SitWaitSwitch():
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x01, 0.4, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x02)

    Return()

# id: 0x00BF offset: 0x11ED4
@scena.Code('AniEvSitMegane')
def AniEvSitMegane():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000B)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_11F93',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_MEGANE_sa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_120FE')

    def _loc_11F93(): pass

    label('loc_11F93')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_12022',
    )

    OP_80(0.3)
    PlayChrAnimeClip(0xFFFE, 'EV_MEGANE_sb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_120FE')

    def _loc_12022(): pass

    label('loc_12022')

    OP_80(0.4)
    PlayChrAnimeClip(0xFFFE, 'EV_MEGANE_s', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Ez,
            Expr.Return,
        ),
        'loc_120C7',
    )

    Sleep(500)
    OP_3B(0x00, (0xFF, 0x7551, 0x0), 0.3, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_120C7(): pass

    label('loc_120C7')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_MEGANE_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_120FE(): pass

    label('loc_120FE')

    Return()

# id: 0x00C0 offset: 0x12100
@scena.Code('AniEvSitSian')
def AniEvSitSian():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000B)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_121BD',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_SIAN_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_122CD')

    def _loc_121BD(): pass

    label('loc_121BD')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_1224A',
    )

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'EV_SIAN_sb', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_122CD')

    def _loc_1224A(): pass

    label('loc_1224A')

    OP_80(0.4)
    PlayChrAnimeClip(0xFFFE, 'EV_SIAN_s', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_SIAN_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_122CD(): pass

    label('loc_122CD')

    Return()

# id: 0x00C1 offset: 0x122D0
@scena.Code('AniEvSitSianTeburi')
def AniEvSitSianTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0)
    OP_80(0.2)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'EV_SIAN_st', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_SIAN_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C2 offset: 0x12388
@scena.Code('AniEvSitUdegumi')
def AniEvSitUdegumi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000B)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12448',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMI_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_12560')

    def _loc_12448(): pass

    label('loc_12448')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_124D7',
    )

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMI_s', 0x00, 0x01, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_12560')

    def _loc_124D7(): pass

    label('loc_124D7')

    OP_80(0.4)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMI_s', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMI_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_12560(): pass

    label('loc_12560')

    Return()

# id: 0x00C3 offset: 0x12564
@scena.Code('AniEvSitUdegumiTeburi')
def AniEvSitUdegumiTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0)
    OP_80(0.2)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMI_st', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMI_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C4 offset: 0x12624
@scena.Code('AniEvUdegumiF')
def AniEvUdegumiF():
    Call(ScriptId.Current, 'SpringEvOff')
    SetEndhookFunction('StopAnimeSlot1', 0x000B)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_126F0',
    )

    OP_80(0.0)
    OP_8A(0xFF, 0xFFFE, 'M_himo01', 0.0)
    OP_8A(0xFF, 0xFFFE, 'M_himo02', 0.0)
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIFa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT_D', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_128A4')

    def _loc_126F0(): pass

    label('loc_126F0')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_127FF',
    )

    OP_80(0.2)
    OP_8A(0xFE, 0xFFFE, 'M_himo01', 0.4)
    OP_8A(0xFE, 0xFFFE, 'M_himo02', 0.4)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIF', 0x00, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    If(
        (
            (Expr.Eval, "ChrPhysicsCtrl(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_127AE',
    )

    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_127FA')

    def _loc_127AE(): pass

    label('loc_127AE')

    PlayChrAnimeClip(0xFFFE, 'PRE_WAIT_U', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_127FA(): pass

    label('loc_127FA')

    Jump('loc_128A4')

    def _loc_127FF(): pass

    label('loc_127FF')

    OP_80(0.4)
    OP_8A(0xFF, 0xFFFE, 'M_himo01', 0.4)
    OP_8A(0xFF, 0xFFFE, 'M_himo02', 0.4)
    PlayChrAnimeClip(0xFFFE, 'WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, 0.3, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIF', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIFa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_128A4(): pass

    label('loc_128A4')

    Return()

# id: 0x00C5 offset: 0x128A8
@scena.Code('AniEvSitUdegumiF')
def AniEvSitUdegumiF():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000B)

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_12969',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIF_sa', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_12A85')

    def _loc_12969(): pass

    label('loc_12969')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_129FA',
    )

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIF_sb', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_12A85')

    def _loc_129FA(): pass

    label('loc_129FA')

    OP_80(0.4)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIF_s', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.333333, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIF_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_12A85(): pass

    label('loc_12A85')

    Return()

# id: 0x00C6 offset: 0x12A88
@scena.Code('AniEvSitUdegumiFTeburi')
def AniEvSitUdegumiFTeburi():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    OP_B5(0xFFFE, 0x01, 0.0, 0.0, 0.0)
    OP_80(0.2)
    SetEndhookFunction('StopSitAnimeSlot1', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT_D', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x01, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIF_st', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV_UDEGUMIF_sa', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00C7 offset: 0x12B48
@scena.Code('StopAnimeSlot1')
def StopAnimeSlot1():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)
    Call(ScriptId.CurrentCharacter, 'SpringOn')

    Return()

# id: 0x00C8 offset: 0x12B78
@scena.Code('StopSitAnimeSlot1')
def StopSitAnimeSlot1():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)

    Return()

# id: 0x00C9 offset: 0x12B9C
@scena.Code('StopChrAnimeClip')
def StopChrAnimeClip():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x01, 0x00)

    Return()

# id: 0x00CA offset: 0x12BC0
@scena.Code('AniEv02025')
def AniEv02025():
    Call(ScriptId.Current, 'EraseEquip')
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'EV02025', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CB offset: 0x12C14
@scena.Code('AniEv02045')
def AniEv02045():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev02045', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev02045a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CC offset: 0x12C84
@scena.Code('AniEv05500')
def AniEv05500():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x0010)
    OP_80(0.0)
    def _loc_12CA2(): pass

    label('loc_12CA2')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12DB2',
    )

    PlayChrAnimeClip(0xFFFE, 'EV05500', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500c', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_12CA2')

    def _loc_12DB2(): pass

    label('loc_12DB2')

    Return()

# id: 0x00CD offset: 0x12DB4
@scena.Code('AniEv05503')
def AniEv05503():
    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'EV05503', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00CE offset: 0x12DE4
@scena.Code('AniEv05505')
def AniEv05505():
    OP_80(0.0)
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(0xFFFE, 'EV05505', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.266667, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    def _loc_12E56(): pass

    label('loc_12E56')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_12F66',
    )

    PlayChrAnimeClip(0xFFFE, 'EV05500a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500c', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05500', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_12E56')

    def _loc_12F66(): pass

    label('loc_12F66')

    Return()

# id: 0x00CF offset: 0x12F68
@scena.Code('AniEv05510')
def AniEv05510():
    Call(ScriptId.CurrentCharacter, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x0010)
    PlayChrAnimeClip(0xFFFE, 'EV05510', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'EV05510a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D0 offset: 0x12FD8
@scena.Code('AniEv30000')
def AniEv30000():
    PlayChrAnimeClip(0xFFFE, 'ev30000', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D1 offset: 0x13004
@scena.Code('AniEv30005')
def AniEv30005():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev30005', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev30005a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D2 offset: 0x13074
@scena.Code('AniEv30185')
def AniEv30185():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev30185', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev30185a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D3 offset: 0x130E4
@scena.Code('AniEv30185b')
def AniEv30185b():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev30185b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D4 offset: 0x1314C
@scena.Code('AniEv33000')
def AniEv33000():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev33000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev33000a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D5 offset: 0x131BC
@scena.Code('AniEv33005')
def AniEv33005():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev33005', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D6 offset: 0x13224
@scena.Code('AniEv34085')
def AniEv34085():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev34085', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D7 offset: 0x13268
@scena.Code('AniEv35000')
def AniEv35000():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    OP_3B(0x00, (0xFF, 0x7534, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(666)
    OP_6C(0xFFFE, 0.4)
    Sleep(666)
    OP_6C(0xFFFE, 0.7)
    Sleep(333)
    OP_3B(0x00, (0xFF, 0x75BC, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x7537, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_6C(0xFFFE, 0.5)
    Sleep(333)
    OP_6C(0xFFFE, 0.25)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x00D8 offset: 0x133D0
@scena.Code('AniEv45000')
def AniEv45000():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev45000', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x00D9 offset: 0x13420
@scena.AnimeClips('_AniAttachMainWeapon')
def _AniAttachMainWeapon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU076',
        ),
    )

# id: 0x00DA offset: 0x13480
@scena.AnimeClips('_OnCostumeIn3_2')
def _OnCostumeIn3_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001742,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x00DB offset: 0x13530
@scena.AnimeClips('_AniFieldChange')
def _AniFieldChange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000170C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000170D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000170E,
            name   = '',
        ),
    )

# id: 0x00DC offset: 0x135E0
@scena.AnimeClips('_AniWait')
def _AniWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_STOP_RUN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_STOP_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'STOP_RUN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'STOP_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'PRE_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x00DD offset: 0x13870
@scena.AnimeClips('_AniWalk')
def _AniWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x00DE offset: 0x13940
@scena.AnimeClips('_AniRun')
def _AniRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_MOVE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'RUN',
        ),
    )

# id: 0x00DF offset: 0x139F0
@scena.AnimeClips('_AniDash')
def _AniDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DASH',
        ),
    )

# id: 0x00E0 offset: 0x13A70
@scena.AnimeClips('_AniBack')
def _AniBack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x00E1 offset: 0x13AD0
@scena.AnimeClips('_AniDamage')
def _AniDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001726,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
    )

# id: 0x00E2 offset: 0x13B80
@scena.AnimeClips('_AniTurn')
def _AniTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'TURN_LEFT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'TURN_RIGHT',
        ),
    )

# id: 0x00E3 offset: 0x13C50
@scena.AnimeClips('_AniSquat')
def _AniSquat():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUATa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUAT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUAT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUATa',
        ),
    )

# id: 0x00E4 offset: 0x13D50
@scena.AnimeClips('_AniFall')
def _AniFall():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FALL',
        ),
    )

# id: 0x00E5 offset: 0x13DB0
@scena.AnimeClips('_AniLand')
def _AniLand():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'LAND',
        ),
    )

# id: 0x00E6 offset: 0x13E10
@scena.AnimeClips('_AniIdle')
def _AniIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001761,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001762,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x00E7 offset: 0x13EE0
@scena.AnimeClips('_AniFieldAttack')
def _AniFieldAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001711,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001712,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001713,
            name   = '',
        ),
    )

# id: 0x00E8 offset: 0x13FE0
@scena.AnimeClips('_AniFieldAttack2')
def _AniFieldAttack2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FATTACK2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001711,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001712,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001713,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F07,
            name   = '',
        ),
    )

# id: 0x00E9 offset: 0x14100
@scena.AnimeClips('_AniAssaultAttack')
def _AniAssaultAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FC0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001063,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010BC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001714,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001715,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F91,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6A,
            name   = '',
        ),
    )

# id: 0x00EA offset: 0x142A0
@scena.AnimeClips('_AniFieldAttackEnd')
def _AniFieldAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000753A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007537,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x00EB offset: 0x143A0
@scena.AnimeClips('_AniFieldAttackEndShort')
def _AniFieldAttackEndShort():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007537,
            name   = '',
        ),
    )

# id: 0x00EC offset: 0x14450
@scena.AnimeClips('_AniAttachPhone')
def _AniAttachPhone():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU320',
        ),
    )

# id: 0x00ED offset: 0x144B0
@scena.AnimeClips('_AniHorse')
def _AniHorse():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x00EE offset: 0x14510
@scena.AnimeClips('_AniHorse2')
def _AniHorse2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x00EF offset: 0x14570
@scena.AnimeClips('_AniHorseWalk')
def _AniHorseWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_WALK',
        ),
    )

# id: 0x00F0 offset: 0x145D0
@scena.AnimeClips('_AniHorseRun')
def _AniHorseRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_RUN',
        ),
    )

# id: 0x00F1 offset: 0x14630
@scena.AnimeClips('_AniHorseDash')
def _AniHorseDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_DASH',
        ),
    )

# id: 0x00F2 offset: 0x14690
@scena.AnimeClips('_AniHorseStop')
def _AniHorseStop():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_STOP',
        ),
    )

# id: 0x00F3 offset: 0x146F0
@scena.AnimeClips('_AniSitWait')
def _AniSitWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
    )

# id: 0x00F4 offset: 0x14750
@scena.AnimeClips('_AniWait1')
def _AniWait1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
    )

# id: 0x00F5 offset: 0x147B0
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/sysspark2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/sysrelease.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/moncharge.eff',
        ),
    )

# id: 0x00F6 offset: 0x14860
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001758,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001759,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000175A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001735,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001734,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001737,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001732,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001733,
            name   = '',
        ),
    )

# id: 0x00F7 offset: 0x149D0
@scena.AnimeClips('_AniBtlReady')
def _AniBtlReady():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000170F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001710,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000170C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000170D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000170E,
            name   = '',
        ),
    )

# id: 0x00F8 offset: 0x14AD0
@scena.AnimeClips('_AniBtlChain')
def _AniBtlChain():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001736,
            name   = '',
        ),
    )

# id: 0x00F9 offset: 0x14B30
@scena.AnimeClips('_VoiceWin_play')
def _VoiceWin_play():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001739,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001738,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001739,
            name   = '',
        ),
    )

# id: 0x00FA offset: 0x14BE0
@scena.AnimeClips('_AniBtlWin')
def _AniBtlWin():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F74,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F74,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x00FB offset: 0x14CB0
@scena.AnimeClips('_AniBtlWin_burst')
def _AniBtlWin_burst():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F74,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001741,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x00FC offset: 0x14D80
@scena.AnimeClips('_AniBtlWin_eraseEquip')
def _AniBtlWin_eraseEquip():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x00FD offset: 0x14E00
@scena.AnimeClips('_AniBtlWinWait')
def _AniBtlWinWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x00FE offset: 0x14E60
@scena.AnimeClips('_AniBtlLevelUp')
def _AniBtlLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001742,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x00FF offset: 0x14F10
@scena.AnimeClips('_AniBtlWait')
def _AniBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0100 offset: 0x14F70
@scena.AnimeClips('_AniTransitionMosion')
def _AniTransitionMosion():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_MOVE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT_MOVE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
    )

# id: 0x0101 offset: 0x15040
@scena.AnimeClips('_AniBtlTurn')
def _AniBtlTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_TURN_R',
        ),
    )

# id: 0x0102 offset: 0x150C0
@scena.AnimeClips('_AniBtlAttack')
def _AniBtlAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001711,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001712,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001713,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0103 offset: 0x151E0
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000172A,
            name   = '',
        ),
    )

# id: 0x0104 offset: 0x15240
@scena.AnimeClips('_AniBtlDamage')
def _AniBtlDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
    )

# id: 0x0105 offset: 0x152C0
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001726,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001727,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001728,
            name   = '',
        ),
    )

# id: 0x0106 offset: 0x15370
@scena.AnimeClips('_AniBtlSwoon')
def _AniBtlSwoon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0107 offset: 0x15420
@scena.AnimeClips('_AniBtlWeak')
def _AniBtlWeak():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x0108 offset: 0x15480
@scena.AnimeClips('_AniBtlTensionMax')
def _AniBtlTensionMax():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionmax.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
    )

# id: 0x0109 offset: 0x15500
@scena.AnimeClips('_AniBtlDead')
def _AniBtlDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000175E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001729,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x010A offset: 0x155D0
@scena.AnimeClips('_AniBtlCharge')
def _AniBtlCharge():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FD5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x010B offset: 0x15680
@scena.AnimeClips('_AniBtlItem')
def _AniBtlItem():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ITEM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001724,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001725,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B80,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x010C offset: 0x15780
@scena.AnimeClips('_AniBtlEscapeVoice0')
def _AniBtlEscapeVoice0():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000172F,
            name   = '',
        ),
    )

# id: 0x010D offset: 0x157E0
@scena.AnimeClips('_AniBtlEscapeVoice1')
def _AniBtlEscapeVoice1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001730,
            name   = '',
        ),
    )

# id: 0x010E offset: 0x15840
@scena.AnimeClips('_AniBtlEscapeVoice2')
def _AniBtlEscapeVoice2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001731,
            name   = '',
        ),
    )

# id: 0x010F offset: 0x158A0
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001743,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001744,
            name   = '',
        ),
    )

# id: 0x0110 offset: 0x15920
@scena.AnimeClips('_AniBtlLinkChase')
def _AniBtlLinkChase():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000174B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000174C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000174C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001745,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
    )

# id: 0x0111 offset: 0x15AC0
@scena.AnimeClips('_AniBtlLinkRushStart')
def _AniBtlLinkRushStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0112 offset: 0x15B20
@scena.AnimeClips('_AniBtlLinkRush')
def _AniBtlLinkRush():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001770,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001771,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001772,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0113 offset: 0x15CC0
@scena.AnimeClips('_AniBtlBraveOrderAnime')
def _AniBtlBraveOrderAnime():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSa',
        ),
    )

# id: 0x0114 offset: 0x15D40
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001721,
            name   = '',
        ),
    )

# id: 0x0115 offset: 0x15DA0
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr021_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr021_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001063,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010BC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F86,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001716,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F91,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00a',
        ),
    )

# id: 0x0116 offset: 0x16000
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr021_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr021_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr021_01_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr021_01_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001717,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F5A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001718,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F07,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F52,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
    )

# id: 0x0117 offset: 0x16380
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr021_02_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F39,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001719,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000107D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000171A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01a',
        ),
    )

# id: 0x0118 offset: 0x164F0
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_01.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_03.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_04.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_05.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_06.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_07.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_08.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_09.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_15.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001012,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000171C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000171B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F96,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F72,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F71,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F37,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F02,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F62,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001771,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F62,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F62,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F62,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F37,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F28,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000171D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F07,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F83,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F7A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010ED,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000171E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F02,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_16.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc021_00_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_12',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x0000171F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F39,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001720,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F07,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000108E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F4B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010FA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F52,
            name   = '',
        ),
    )

# id: 0x0119 offset: 0x17040
@scena.AnimeClips('_AniBtlSCraft00_finish')
def _AniBtlSCraft00_finish():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x011A offset: 0x170A0
@scena.AnimeClips('_AniEvIdle')
def _AniEvIdle():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'IDLE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x011B offset: 0x17120
@scena.AnimeClips('_AniEvWait')
def _AniEvWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x011C offset: 0x17180
@scena.AnimeClips('_AniEvWalk')
def _AniEvWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x011D offset: 0x171E0
@scena.AnimeClips('_AniEvRun')
def _AniEvRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'RUN',
        ),
    )

# id: 0x011E offset: 0x17240
@scena.AnimeClips('_AniEvDash')
def _AniEvDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DASH',
        ),
    )

# id: 0x011F offset: 0x172A0
@scena.AnimeClips('_AniEvSquat')
def _AniEvSquat():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUATa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUAT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUAT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SQUATa',
        ),
    )

# id: 0x0120 offset: 0x173A0
@scena.AnimeClips('_AniEvFall')
def _AniEvFall():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'FALL',
        ),
    )

# id: 0x0121 offset: 0x17400
@scena.AnimeClips('_AniEvLand')
def _AniEvLand():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'LAND',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0122 offset: 0x17480
@scena.AnimeClips('_AniEvFieldAttackEnd')
def _AniEvFieldAttackEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DISARM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000753A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007536,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007537,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0123 offset: 0x17580
@scena.AnimeClips('_AniEvBtlWait')
def _AniEvBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0124 offset: 0x175E0
@scena.AnimeClips('_AniEvBtlMove')
def _AniEvBtlMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
    )

# id: 0x0125 offset: 0x17640
@scena.AnimeClips('_AniEvBtlDash')
def _AniEvBtlDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DASH',
        ),
    )

# id: 0x0126 offset: 0x176A0
@scena.AnimeClips('_AniEvBtlWalk')
def _AniEvBtlWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
    )

# id: 0x0127 offset: 0x17700
@scena.AnimeClips('_AniEvAttack')
def _AniEvAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0128 offset: 0x17780
@scena.AnimeClips('_AniEvDamage')
def _AniEvDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0129 offset: 0x17800
@scena.AnimeClips('_AniEvWeakDamage')
def _AniEvWeakDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x012A offset: 0x17880
@scena.AnimeClips('_AniEvGuard')
def _AniEvGuard():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_GUARD',
        ),
    )

# id: 0x012B offset: 0x178E0
@scena.AnimeClips('_AniEvAria')
def _AniEvAria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x012C offset: 0x17940
@scena.AnimeClips('_AniEvArts')
def _AniEvArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSa',
        ),
    )

# id: 0x012D offset: 0x179C0
@scena.AnimeClips('_AniEvBackStep')
def _AniEvBackStep():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_BACKSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x012E offset: 0x17A40
@scena.AnimeClips('_AniEvDead')
def _AniEvDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x012F offset: 0x17AC0
@scena.AnimeClips('_AniEvDead1')
def _AniEvDead1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD1',
        ),
    )

# id: 0x0130 offset: 0x17B20
@scena.AnimeClips('_AniEvItem')
def _AniEvItem():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ITEM',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0131 offset: 0x17BA0
@scena.AnimeClips('_AniEvFrontStep')
def _AniEvFrontStep():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FRONTSTEP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0132 offset: 0x17C20
@scena.AnimeClips('_AniEvBtlSleep')
def _AniEvBtlSleep():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_SLEEP',
        ),
    )

# id: 0x0133 offset: 0x17C80
@scena.AnimeClips('_AniEvWeak')
def _AniEvWeak():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x0134 offset: 0x17CE0
@scena.AnimeClips('_AniEvWin')
def _AniEvWin():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WIN',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WINa',
        ),
    )

# id: 0x0135 offset: 0x17D60
@scena.AnimeClips('_AniEvLevelUp')
def _AniEvLevelUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_LEVELUPa',
        ),
    )

# id: 0x0136 offset: 0x17DE0
@scena.AnimeClips('_AniEvHorseWait')
def _AniEvHorseWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x0137 offset: 0x17E40
@scena.AnimeClips('_AniEvHorseWalk')
def _AniEvHorseWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_WALK',
        ),
    )

# id: 0x0138 offset: 0x17EA0
@scena.AnimeClips('_AniEvHorseRun')
def _AniEvHorseRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_RUN',
        ),
    )

# id: 0x0139 offset: 0x17F00
@scena.AnimeClips('_AniEvHorseStop')
def _AniEvHorseStop():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_STOP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x013A offset: 0x17F80
@scena.AnimeClips('_AniEvHorseTurnRight')
def _AniEvHorseTurnRight():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_TURN_R',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x013B offset: 0x18000
@scena.AnimeClips('_AniEvHorseTurnLeft')
def _AniEvHorseTurnLeft():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_TURN_L',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE',
        ),
    )

# id: 0x013C offset: 0x18080
@scena.AnimeClips('_AniEvHorseDash')
def _AniEvHorseDash():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'HORSE_DASH',
        ),
    )

# id: 0x013D offset: 0x180E0
@scena.AnimeClips('_AniEvSCraft00')
def _AniEvSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
        ),
    )

# id: 0x013E offset: 0x18140
@scena.AnimeClips('_AniEvSCraft00_1')
def _AniEvSCraft00_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01a',
        ),
    )

# id: 0x013F offset: 0x181C0
@scena.AnimeClips('_AniEvSCraft00_2')
def _AniEvSCraft00_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
    )

# id: 0x0140 offset: 0x18220
@scena.AnimeClips('_AniEvSCraft00_3')
def _AniEvSCraft00_3():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03',
        ),
    )

# id: 0x0141 offset: 0x18280
@scena.AnimeClips('_AniEvSCraft00_4')
def _AniEvSCraft00_4():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04',
        ),
    )

# id: 0x0142 offset: 0x182E0
@scena.AnimeClips('_AniEvSCraft00_5')
def _AniEvSCraft00_5():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05',
        ),
    )

# id: 0x0143 offset: 0x18340
@scena.AnimeClips('_AniEvSCraft00_6')
def _AniEvSCraft00_6():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06a',
        ),
    )

# id: 0x0144 offset: 0x183C0
@scena.AnimeClips('_AniEvSCraft00_7')
def _AniEvSCraft00_7():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07',
        ),
    )

# id: 0x0145 offset: 0x18420
@scena.AnimeClips('_AniEvSCraft00_8')
def _AniEvSCraft00_8():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08',
        ),
    )

# id: 0x0146 offset: 0x18480
@scena.AnimeClips('_AniEvSCraft00_9')
def _AniEvSCraft00_9():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09',
        ),
    )

# id: 0x0147 offset: 0x184E0
@scena.AnimeClips('_AniEvSCraft00_10')
def _AniEvSCraft00_10():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_10a',
        ),
    )

# id: 0x0148 offset: 0x18560
@scena.AnimeClips('_AniEvSCraft00_11')
def _AniEvSCraft00_11():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_11',
        ),
    )

# id: 0x0149 offset: 0x185C0
@scena.AnimeClips('_AniEvSCraft00_12')
def _AniEvSCraft00_12():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_12',
        ),
    )

# id: 0x014A offset: 0x18620
@scena.AnimeClips('_AniEvSCraft00_13')
def _AniEvSCraft00_13():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_13',
        ),
    )

# id: 0x014B offset: 0x18680
@scena.AnimeClips('_AniEvSCraft00_14')
def _AniEvSCraft00_14():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_14a',
        ),
    )

# id: 0x014C offset: 0x18700
@scena.AnimeClips('_AniEvCraft00')
def _AniEvCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
    )

# id: 0x014D offset: 0x18760
@scena.AnimeClips('_AniEvCraft00_1')
def _AniEvCraft00_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00a',
        ),
    )

# id: 0x014E offset: 0x187E0
@scena.AnimeClips('_AniEvCraft01')
def _AniEvCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
    )

# id: 0x014F offset: 0x18840
@scena.AnimeClips('_AniEvCraft01_1')
def _AniEvCraft01_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
    )

# id: 0x0150 offset: 0x188A0
@scena.AnimeClips('_AniEvCraft01_2')
def _AniEvCraft01_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
    )

# id: 0x0151 offset: 0x18920
@scena.AnimeClips('_AniEvCraft02')
def _AniEvCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
    )

# id: 0x0152 offset: 0x18980
@scena.AnimeClips('_AniEvCraft02_1')
def _AniEvCraft02_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01a',
        ),
    )

# id: 0x0153 offset: 0x18A00
@scena.AnimeClips('_AniBtlCrucifixion')
def _AniBtlCrucifixion():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRUCIFIXION',
        ),
    )

# id: 0x0154 offset: 0x18A60
@scena.AnimeClips('_AniBtlFloat')
def _AniBtlFloat():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_FLOAT',
        ),
    )

# id: 0x0155 offset: 0x18AC0
@scena.AnimeClips('_SitWaitSwitch')
def _SitWaitSwitch():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
    )

# id: 0x0156 offset: 0x18B20
@scena.AnimeClips('_AniEvSitMegane')
def _AniEvSitMegane():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MEGANE_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MEGANE_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MEGANE_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007551,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_MEGANE_sa',
        ),
    )

# id: 0x0157 offset: 0x18CC0
@scena.AnimeClips('_AniEvSitSian')
def _AniEvSitSian():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_sa',
        ),
    )

# id: 0x0158 offset: 0x18E30
@scena.AnimeClips('_AniEvSitSianTeburi')
def _AniEvSitSianTeburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_st',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_SIAN_sa',
        ),
    )

# id: 0x0159 offset: 0x18EE0
@scena.AnimeClips('_AniEvSitUdegumi')
def _AniEvSitUdegumi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMI_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMI_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMI_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMI_sa',
        ),
    )

# id: 0x015A offset: 0x19050
@scena.AnimeClips('_AniEvSitUdegumiTeburi')
def _AniEvSitUdegumiTeburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMI_st',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMI_sa',
        ),
    )

# id: 0x015B offset: 0x19100
@scena.AnimeClips('_AniEvUdegumiF')
def _AniEvUdegumiF():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIFa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIFa',
        ),
    )

# id: 0x015C offset: 0x192C0
@scena.AnimeClips('_AniEvSitUdegumiF')
def _AniEvSitUdegumiF():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_sa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_sb',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_s',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_sa',
        ),
    )

# id: 0x015D offset: 0x19430
@scena.AnimeClips('_AniEvSitUdegumiFTeburi')
def _AniEvSitUdegumiFTeburi():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_st',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_UDEGUMIF_sa',
        ),
    )

# id: 0x015E offset: 0x194E0
@scena.AnimeClips('_AniEv02025')
def _AniEv02025():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV02025',
        ),
    )

# id: 0x015F offset: 0x19540
@scena.AnimeClips('_AniEv02045')
def _AniEv02045():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev02045',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev02045a',
        ),
    )

# id: 0x0160 offset: 0x195C0
@scena.AnimeClips('_AniEv05500')
def _AniEv05500():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500c',
        ),
    )

# id: 0x0161 offset: 0x196E0
@scena.AnimeClips('_AniEv05503')
def _AniEv05503():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05503',
        ),
    )

# id: 0x0162 offset: 0x19740
@scena.AnimeClips('_AniEv05505')
def _AniEv05505():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05505',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500c',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05500',
        ),
    )

# id: 0x0163 offset: 0x198B0
@scena.AnimeClips('_AniEv05510')
def _AniEv05510():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05510',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV05510a',
        ),
    )

# id: 0x0164 offset: 0x19930
@scena.AnimeClips('_AniEv30000')
def _AniEv30000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30000',
        ),
    )

# id: 0x0165 offset: 0x19990
@scena.AnimeClips('_AniEv30005')
def _AniEv30005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30005',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30005a',
        ),
    )

# id: 0x0166 offset: 0x19A10
@scena.AnimeClips('_AniEv30185')
def _AniEv30185():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30185',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30185a',
        ),
    )

# id: 0x0167 offset: 0x19A90
@scena.AnimeClips('_AniEv30185b')
def _AniEv30185b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30185b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0168 offset: 0x19B10
@scena.AnimeClips('_AniEv33000')
def _AniEv33000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev33000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev33000a',
        ),
    )

# id: 0x0169 offset: 0x19B90
@scena.AnimeClips('_AniEv33005')
def _AniEv33005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev33005',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x016A offset: 0x19C10
@scena.AnimeClips('_AniEv34085')
def _AniEv34085():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev34085',
        ),
    )

# id: 0x016B offset: 0x19C70
@scena.AnimeClips('_AniEv35000')
def _AniEv35000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev35000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007534,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000075BC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00007537,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x016C offset: 0x19D70
@scena.AnimeClips('_AniEv45000')
def _AniEv45000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45000',
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
