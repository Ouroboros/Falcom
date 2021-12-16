import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED83.Parser.scena_writer_helper import *

scena = createScenaWriter('chr501.dat')

# id: 0x0000 offset: 0xAC0
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            flags = 0x00000001,
            model      = 'C_CHR032_DF1',
            animeClip  = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000001,
            model      = 'C_CHR032_DF1',
            animeClip  = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000001,
            model      = 'C_CHR032_DF1',
            animeClip  = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000001,
            model      = 'C_CHR032_DF1',
            animeClip  = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000001,
            model      = 'C_CHR032_DF1',
            animeClip  = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000001,
            model      = 'C_CHR032_DF1',
            animeClip  = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_POWERUP',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_POWERUPa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT00_01a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT00_02a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT02_00a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000100,
            model      = 'C_CHR032_BT1',
            animeClip  = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'WAIT1_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'EV_DEAD1',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_DF1',
            animeClip  = 'SIT_WAIT-2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_DF1',
            animeClip  = 'SIT_WAIT-1',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_DF1',
            animeClip  = 'SIT_WAIT+1',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_DF1',
            animeClip  = 'SIT_WAIT+2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_AKIRE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_AKIREa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_AKIREb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_AKUBI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_AKUBI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ASENUGUI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ASENUGUIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ASENUGUIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ATAMAKAKI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ATAMAKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_BYE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_BYEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_BYEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_BYEBYE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_BYEBYEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_BYEBYEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_BYE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK+1',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK+2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK+3',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK-1',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK-2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_AGO',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_PEN',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_PEN_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_PEN_MOVEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_PEN_2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_PEN_3',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_RYOTE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_DESK_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_FALL',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GAKKARI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GAKKARIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GAKKARIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GAKKARI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GAKKARI_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GAKKARI_sb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GOUREIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HAKUSHU',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HAKUSHUa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HAKUSHUb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HAKUSHUc',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HAKUSHU_2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HAKUSHU_2a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HAKUSHU_2b',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HAKUSHU_2c',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HANASIKAKE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HANASIKAKEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HANASIKAKEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HITEI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HITEI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_GLASS',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_GLASS_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_GLASSc',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_GLASSc_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_GLASS_w',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_CUP_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_CUPc_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_JOKKI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_JOKKI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_JOKKI_w',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOLD_JOKKIc_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOOKAKI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_HOOKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_INORI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_INORIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KABEMOTARE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAIWA',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAMIHARAI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KANGEI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KANGEIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KANGEIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KANGEI2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KANGEI2a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KANGEI2b',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYOb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYO_2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYO_2a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYO_2b',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYO_3',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYO_3a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KAZETUYO_3b',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KEIREI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KEIREIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KEIREIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KEYBOARD_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KEYBOARD_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KEYBOARD_sb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_KUZUSISUWARI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_MEGANE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_MEGANEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_MEGANEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_MOKUREI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_MOKUREIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_MOKUREIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ODOROKIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_ODOROKI_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_OJIGI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_OJIGI_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_OJIGIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_OJIGIa_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_OJIGIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_OJIGIb_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_HOLD',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_HOLDa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_HOLD_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_HOLD_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_LOOK',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_LOOKa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_LOOK_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_LOOK_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_MISERU',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_MISERUa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_SOUSA',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_SOUSAa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_SOUSA_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_SOUSA_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_TALK',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_TALKa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_TALK_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_PHONE_TALK_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_REI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_REI_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_REIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_REIa_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_REIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_REIb_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTEBURI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_GYU',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'EV_RYOTE_ATAMA',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'EV_RYOTE_ATAMAa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'EV_RYOTE_ATAMAb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'EV_RYOTE_ATAMA_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_AWASE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_AWASEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_AWASEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_KOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_MAE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_MAE_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_SIRIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_RYOTE_SIRI_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SEKI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SEKI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SIANb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SIAN_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SIT_JIMEN',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SIT_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SLEEP',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SLEEPa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SLEEP_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SLEEP_GAKEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SLEEP_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TAORE_1',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TAORE_2',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TAORE_3',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TAORE_4',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEBURI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEKOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'EV_TEMUNE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'EV_TEMUNEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEMUNE_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEMUNE_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEMUNE_sb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEUKASE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEUKASEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TEUKASEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TORIDASI_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TORIDASI_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TORIDASI_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_TORIDASI_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_UDEGUMI_t',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_UKETORI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_UKETORIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_UKETORIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASU',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASUa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASUb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASU_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASU_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASU_KAMIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASU_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASU_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_WATASU_KAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YAA',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YAAa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YAAb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YAREYARE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YARUKI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YARUKIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YARUKIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YASUME',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YASUME_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YASUMEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YASUMEa_U',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YORIKAKARIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_MAE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_UE',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_UEa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_UEb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_MIGI',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_MIGIa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_MIGIb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_LEFTa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_LEFTb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_SITA',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_SITAa',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHRX00_EV',
            animeClip  = 'EV_YUBISASI_SITAb',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'ev00070',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'ev00070a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'ev50525',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'ev50525a',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'DROPCLOTHES_01',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'DROPCLOTHES_02',
        ),
        ScenaAnimeClipTableEntry(
            flags = 0x00000002,
            model      = 'C_CHR032_EV',
            animeClip  = 'DROPCLOTHES_03',
        ),
    )

# id: 0x0001 offset: 0x5EFC
@scena.Code('Init')
def Init():
    Call(0x0B, 'AniAttachMainWeapon')
    ChrAnimeClipCtrl(0x06, 0xFFFE, 0x00000100)
    OP_04(0x0B, 'AniWait')

    Return()

# id: 0x0002 offset: 0x5F28
@scena.Code('DefaultFace')
def DefaultFace():
    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0003 offset: 0x5F50
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    ChrAnimeClipCtrl(0x06, 0xFFFE, 0x00000002)

    Return()

# id: 0x0004 offset: 0x5F5C
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    ChrAnimeClipCtrl(0x06, 0xFFFE, 0x00000100)

    Return()

# id: 0x0005 offset: 0x5F68
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    ChrAnimeClipCtrl(0x06, 0xFFFE, 0x00000010)

    Return()

# id: 0x0006 offset: 0x5F74
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    ChrAnimeClipCtrl(0x07, 0xFFFE, 0x00000002)

    Return()

# id: 0x0007 offset: 0x5F80
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    ChrAnimeClipCtrl(0x07, 0xFFFE, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0008 offset: 0x5F94
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    ChrAnimeClipCtrl(0x07, 0xFFFE, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0009 offset: 0x5FA8
@scena.Code('AniReset')
def AniReset():
    Call(0x0B, 'DefaultFace')
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1, -1, -1, 0x00, 0x00)

    Return()

# id: 0x000A offset: 0x5FD8
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    Return()

# id: 0x000B offset: 0x5FDC
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB01', 0.2)

    Return()

# id: 0x000C offset: 0x6024
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB01', 0.2)

    Return()

# id: 0x000D offset: 0x606C
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x000E offset: 0x6070
@scena.Code('AniTurn')
def AniTurn():
    If(
        (
            (Expr.Eval, "OP_35(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_60AD',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    Jump('loc_60CC')

    def _loc_60AD(): pass

    label('loc_60AD')

    PlayChrAnimeClip(0xFFFE, 'WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    def _loc_60CC(): pass

    label('loc_60CC')

    Sleep(250)
    OP_38(0xFFFE, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x000F offset: 0x60E0
@scena.Code('AniWait')
def AniWait():
    If(
        (
            (Expr.Eval, "OP_35(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_6130',
    )

    Call(0x0B, 'EraseEquip')
    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_61A9')

    def _loc_6130(): pass

    label('loc_6130')

    If(
        (
            (Expr.Eval, "OP_35(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_6182',
    )

    Call(0x0B, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_61A9')

    def _loc_6182(): pass

    label('loc_6182')

    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_61A9(): pass

    label('loc_61A9')

    Return()

# id: 0x0010 offset: 0x61AC
@scena.Code('AniWalk')
def AniWalk():
    Call(0x0B, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_35(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_6203',
    )

    Call(0x0B, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    Jump('loc_6222')

    def _loc_6203(): pass

    label('loc_6203')

    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    def _loc_6222(): pass

    label('loc_6222')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0011 offset: 0x622C
@scena.Code('AniRun')
def AniRun():
    Call(0x0B, 'SpringOff')

    If(
        (
            (Expr.Eval, "OP_35(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_6276',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    Jump('loc_6294')

    def _loc_6276(): pass

    label('loc_6276')

    PlayChrAnimeClip(0xFFFE, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    def _loc_6294(): pass

    label('loc_6294')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0012 offset: 0x62A0
@scena.Code('AniSitWait')
def AniSitWait():
    Call(0x0B, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    Return()

# id: 0x0013 offset: 0x62D8
@scena.Code('AniWait1')
def AniWait1():
    Call(0x0B, 'SpringOn')
    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x01, 0x00, 0x00, 0x01, -2, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Return()

# id: 0x0014 offset: 0x6308
@scena.Code('StopAnimeSlot1')
def StopAnimeSlot1():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1, -1, -1, 0x01, 0x00)
    Call(0x10, 'SpringOn')

    Return()

# id: 0x0015 offset: 0x6338
@scena.Code('StopSitAnimeSlot1')
def StopSitAnimeSlot1():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1, -1, -1, 0x01, 0x00)

    Return()

# id: 0x0016 offset: 0x635C
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Return()

# id: 0x0017 offset: 0x6360
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    Return()

# id: 0x0018 offset: 0x6364
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    OP_31(0x00, 'C_EQU320')
    AttachEquip(0xFFFE, 'C_EQU320', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)

    Return()

# id: 0x0019 offset: 0x63C0
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    OP_31(0x01, 'C_EQU320')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_54(0x0B, 0xFFFE)

    Return()

# id: 0x001A offset: 0x6408
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, 0xFFFE, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x001B offset: 0x6430
@scena.Code('AniBtlInit')
def AniBtlInit():
    Call(0x13, 'AniBtlInit')
    EffectCtrl(0x0B, 0xFFFE, 0x8D)
    EffectCtrl(0x0B, 0xFFFE, 0x8E)
    LoadEffect(0xFFFE, 0x8D, 'battle/cr032_02_1.eff')
    LoadEffect(0xFFFE, 0x8E, 'battle/cr032_02_2.eff')
    EffectCtrl(0x0B, 0xFFFE, 0x82)
    EffectCtrl(0x0B, 0xFFFE, 0x83)
    EffectCtrl(0x0B, 0xFFFE, 0x84)
    LoadEffect(0xFFFE, 0x82, 'battle/atk032_0.eff')
    LoadEffect(0xFFFE, 0x83, 'battle/atk032_1.eff')
    LoadEffect(0xFFFE, 0x84, 'battle/atk032_2.eff')
    PlayEffect(0xFFFE, (0xFF, 0x82, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x84, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    EffectCtrl(0x0B, 0xFFFE, 0x80)
    LoadEffect(0xFFFE, 0x80, 'battle/moncharge.eff')

    Return()

# id: 0x001C offset: 0x6588
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_arm_point', 0x01)

    Return()

# id: 0x001D offset: 0x65B0
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_arm_point', 0x01)

    Return()

# id: 0x001E offset: 0x65D8
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x131),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_662E',
    )

    OP_3B(0x32, (0xFF, 0x1C20, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_667F')

    def _loc_662E(): pass

    label('loc_662E')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x133),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_667F',
    )

    OP_3B(0x32, (0xFF, 0x1C22, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_667F(): pass

    label('loc_667F')

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x001F offset: 0x6684
@scena.Code('AniBtlReady')
def AniBtlReady():
    Return()

# id: 0x0020 offset: 0x6688
@scena.Code('AniBtlWait')
def AniBtlWait():
    OP_80(0.2)
    Call(0x0B, 'BtlDefaultFace')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6765',
    )

    PlayEffect(0xFFFE, (0xFF, 0x82, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x84, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)

    Jump('loc_67C0')

    def _loc_6765(): pass

    label('loc_6765')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_67C0',
    )

    PlayEffect(0xFFFE, (0xFF, 0x82, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)

    def _loc_67C0(): pass

    label('loc_67C0')

    OP_0A(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0021 offset: 0x67CC
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCtrl(0x00)
    OP_33(0x47)
    OP_33(0x48, 0xFFFE)
    OP_33(0x46, 0.25, 6.0, 15)
    OP_33(0x3C, 0xFFFE, 0xFFF5, 0.0, 0.5)
    Call(0x13, 'AniBtlMove')

    Return()

# id: 0x0022 offset: 0x6800
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)

    Return()

# id: 0x0023 offset: 0x6824
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCtrl(0x00)
    OP_33(0x47)
    OP_33(0x48, 0xFFFE)
    OP_33(0x48, 0xFFFB)
    OP_33(0x46, 0.25, 6.0, 15)
    Call(0x13, 'AniBtlMove')
    OP_33(0x3C, 0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '6', 'A', '', '#b', '0')
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_33(0x62, 0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_68BE',
    )

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1C24, 0x0), (0xFF, 0x1C25, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    def _loc_68BE(): pass

    label('loc_68BE')

    Sleep(550)
    SetChrFace(0x03, 0xFFFE, '6', 'B', '', '#b', '0')
    Sleep(130)
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x83, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, -0.019999999552965164, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FB3, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_33(0x47)
    OP_33(0x48, 0xFFFB)
    OP_33(0x46, 0.5, 6.0, 15)
    Sleep(100)
    Sleep(400)
    CameraCtrl(0x0A, 0.07, 0.05, 0.01, 0x001E, 0x014A, 0x0096, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    Call(0x13, 'AniBtlDamageTargets', (0xFF, 0x3F8, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x1, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))
    OP_3B(0x00, (0xFF, 0x10F3, 0x0), 1.0, (0xFF, 0x64, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(200)
    Call(0x13, 'AniBtlDamageTargets', (0xFF, 0x3F8, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x3, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))
    OP_3B(0x00, (0xFF, 0x10F3, 0x0), 1.0, (0xFF, 0x64, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x01, (0xFF, 0x8FB3, 0x0), (0xFF, 0x7D0, 0x0))
    Sleep(100)
    SetChrFace(0x03, 0xFFFE, '6', '8', '', '#b', '0')
    Sleep(150)
    SetChrFace(0x03, 0xFFFE, '6', '0', '', '#b', '0')
    Sleep(100)
    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x82, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0024 offset: 0x6BA0
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    OP_3B(0x32, (0xFF, 0x1C38, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Call(0x13, 'AniBtlCounter')

    Return()

# id: 0x0025 offset: 0x6BF8
@scena.Code('AniBtlDamage')
def AniBtlDamage():
    SetChrFace(0x03, 0xFFFE, 'B', '3', '', '#b', '0')

    If(
        (
            (Expr.Eval, "OP_33(0xAF, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6C45',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)

    Jump('loc_6C6A')

    def _loc_6C45(): pass

    label('loc_6C45')

    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)

    def _loc_6C6A(): pass

    label('loc_6C6A')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0026 offset: 0x6C74
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "OP_33(0xB7, 0x05, 0xFFFE, 0x00000000, 0x00000000, 0x00000000, 0x00)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_6CDB',
    )

    OP_3B(0x32, (0xFF, 0x1C37, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_6CF7')

    def _loc_6CDB(): pass

    label('loc_6CDB')

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1C35, 0x0), (0xFF, 0x1C36, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    def _loc_6CF7(): pass

    label('loc_6CF7')

    Return()

# id: 0x0027 offset: 0x6CF8
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    OP_3B(0x32, (0xFF, 0x1C33, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Return()

# id: 0x0028 offset: 0x6D3C
@scena.Code('AniBtlSwoon')
def AniBtlSwoon():
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)
    EffectCtrl(0x0F, 0xFFFE, 0x0084, 0x01)

    OP_0A(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_6D9D',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    Jump('loc_6DF1')

    def _loc_6D9D(): pass

    label('loc_6D9D')

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)

    def _loc_6DF1(): pass

    label('loc_6DF1')

    Return()

# id: 0x0029 offset: 0x6DF4
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    OP_80(0.2)
    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)

    Return()

# id: 0x002A offset: 0x6E2C
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(0x13, 'AniBtlCraftBegin')
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)

    OP_0A(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    LoadEffect(0xFFFE, 0x90, 'battle_sys/tensionmax.eff')
    LoadEffect(0xFFFE, 0x91, 'battle_sys/tensionup.eff')
    Call(0x0B, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1, -1, -1, 0x00, 0x00)
    OP_6C(0xFFFE, 0.7)
    SetChrFace(0x03, 0xFFFE, 'F2', '0[autoM0]', '0', '#b', '0')
    OP_33(0x47)
    CameraCtrl(0x00)
    CameraCtrl(0x14, 0x03, 0xFFFE, '', 0.0, 1.35, 0.0, 0x0000)
    CameraCtrl(0x13, 0xFFFE, '', 0x03, 6.0, 8.0, 6.0, 0x0000, 0x01)
    CameraSetDistance(3.25, 0)
    CameraCtrl(0x0C, 0x03, 0.0, -0.15, 0.0, 0x1F40)
    CameraCtrl(0x11, 0x03, -5, 22, 0.0, 0x1F40, 0x01)
    CameraCtrl(0x16, 0x03, -1.2, 0x0BB8)
    OP_33(0x4B, 0x1F40, 0x03)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F2E, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_6C(0xFFFE, 0.4)
    CameraCtrl(0x0A, 0.02, 0.02, 0.0, 0x01F4, 0x07D0, 0x01F4, 0x0000, 0x0000, 0x00)
    Sleep(500)
    OP_3B(0x32, (0xFF, 0x1C32, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '1', '4[autoM4]', '0', '#b', '0')
    Sleep(666)
    OP_6C(0xFFFE, 0.2)
    Sleep(666)
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '3773', '2662', '0', '#b', '0')
    EffectCtrl(0x10, 0xFFFE, 0x0091, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F00, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F78, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    SetChrFace(0x03, 0xFFFE, '6', '73', '0', '#b', '0')
    CameraCtrl(0x0A, 0.1, 0.1, 0.0, 0x001E, 0x0258, 0x01F4, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0002, 0.1, 0x001E, 0x0258, 0x0190, 0.0, 0xFFFF, -9000, -9000, -9000)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    CameraCtrl(0x16, 0x03, 1.3, 0x01C2)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 0x01C2)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '2[autoE2]', '4[autoM4]', '0', '#b', '0')
    CameraCtrl(0x16, 0x03, 1.0, 0x1388)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 0x1388)
    OP_33(0x00, 0xFFFB, 0xFFFE, 0x64)
    Sleep(766)
    Call(0x0B, 'SpringOn')
    Call(0x0B, 'BtlDefaultFace')
    Call(0x13, 'ReleaseEffect')
    Call(0x13, 'AniBtlCraftFinish')

    Return()

# id: 0x002B offset: 0x7260
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(0x0B, 'AniBtlDamage')
    Sleep(1000)

    Return()

# id: 0x002C offset: 0x7274
@scena.Code('AniBtlDead')
def AniBtlDead():
    If(
        (
            (Expr.Eval, "OP_33(0x0D, 0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_72C9',
    )

    OP_3B(0x32, (0xFF, 0x1C34, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_72C9(): pass

    label('loc_72C9')

    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    OP_6C(0xFFFE, 0.5)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Sleep(500)

    Return()

# id: 0x002D offset: 0x7310
@scena.Code('AniBtlAria')
def AniBtlAria():
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)

    OP_0A(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_33(0x62, 0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_73BA',
    )

    OP_33(0x3C, 0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(0xFFFE, (0xFF, 0x7D9, 0x0), 0xFFFE, 0x00000021, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1, -1, -1, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '7', '0', '', '#b', '0')

    Jump('loc_74C9')

    def _loc_73BA(): pass

    label('loc_73BA')

    CameraCtrl(0x00)
    OP_33(0x47)
    OP_33(0x48, 0xFFFE)
    OP_33(0x46, 0.25, 6.0, 15)
    OP_33(0x3C, 0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(0xFFFE, (0xFF, 0x7D9, 0x0), 0xFFFE, 0x00000021, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x00)
    OP_3B(0x00, (0xFF, 0x8B7E, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1C2C, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    SetChrFace(0x03, 0xFFFE, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1, -1, -1, 0x00, 0x00)
    Sleep(1500)
    SetChrFace(0x03, 0xFFFE, '7', '0', '', '#b', '0')

    def _loc_74C9(): pass

    label('loc_74C9')

    Return()

# id: 0x002E offset: 0x74CC
@scena.Code('AniBtlArts')
def AniBtlArts():
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)

    OP_0A(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraCtrl(0x00)
    OP_33(0x47)
    OP_33(0x48, 0xFFFE)
    OP_33(0x46, 0.25, 6.0, 15)
    OP_33(0x4B, 0x00FA, 0x03)
    OP_33(0x3C, 0xFFFE, 0xFFF5, 0.0, 0.5)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    Sleep(400)
    SetChrFace(0x03, 0xFFFE, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1C2D, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x7DB, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8B7F, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(500)
    CameraCtrl(0x00)
    OP_33(0x47)
    OP_33(0x05, 0x00, '')
    OP_33(0x06, 0x00)
    SetChrFace(0x03, 0xFFFE, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    EffectCtrl(0x12, 0xFFFE, 0x07DB)

    Return()

# id: 0x002F offset: 0x766C
@scena.Code('AniBtlCharge')
def AniBtlCharge():
    If(
        (
            (Expr.Eval, "OP_33(0x62, 0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_7703',
    )

    OP_33(0x3C, 0xFFFE, 0xFFFB, 0.0, -1)
    PlayEffect(0xFFFE, (0xFF, 0x80, 0x0), 0xFFFE, 0x00000103, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)

    Jump('loc_77E5')

    def _loc_7703(): pass

    label('loc_7703')

    CameraCtrl(0x00)
    OP_33(0x47)
    OP_33(0x48, 0xFFFE)
    OP_33(0x46, 0.25, 6.0, 15)
    OP_33(0x3C, 0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(0xFFFE, (0xFF, 0x80, 0x0), 0xFFFE, 0x00000103, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x00)
    OP_3B(0x00, (0xFF, 0xFD5, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)
    Sleep(1000)

    def _loc_77E5(): pass

    label('loc_77E5')

    Return()

# id: 0x0030 offset: 0x77E8
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(0x13, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x90, 'battle/cr032_00_0.eff')
    LoadEffect(0xFFFE, 0x98, 'battle/cr032_00_1.eff')
    LoadEffect(0xFFFE, 0x91, 'battle/cr032_00_10.eff')
    LoadEffect(0xFFFE, 0x92, 'battle/cr032_00_20.eff')
    LoadEffect(0xFFFE, 0x93, 'battle/cr032_00_30.eff')
    LoadEffect(0xFFFE, 0x94, 'battle/cr032_00_40.eff')
    LoadEffect(0xFFFE, 0x95, 'battle/cr032_00_50.eff')
    LoadEffect(0xFFFE, 0x96, 'battle/cr032_00_60.eff')
    LoadEffect(0xFFFE, 0x97, 'battle/cr032_00_70.eff')
    OP_33(0x04, 0x00)
    Call(0x0B, 'SpringOff')
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)

    OP_0A(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_33(0x47)
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)
    OP_33(0x3C, 0xFFFE, 0xFFF5, 0.0, -1)
    CameraCtrl(0x14, 0x03, 0xFFFE, '', 1.4, 1.25, -1.95, 0x0000)
    CameraCtrl(0x13, 0xFFFE, '', 0x03, 7.0, -35, 0.0, 0x0000, 0x01)
    CameraSetDistance(4.5, 0)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1, -1, -1, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '1', '4545454', '', '#b', '0')
    OP_6C(0xFFFE, 1.0)
    Sleep(200)
    OP_3B(0x32, (0xFF, 0x1C26, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    Sleep(500)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x0000000C, (0xDD, 'NODE_L_ARM'), (0xEE, 0.0, 0x0), (0xEE, -0.5, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 0.800000011920929, 0x0), (0xEE, 0.800000011920929, 0x0), (0xEE, 0.800000011920929, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FBC, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x9078, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x16, 0x03, -1, 0x0190)
    CameraCtrl(0x0C, 0x03, 0.0, 0.0, 0.1, 0x0190)
    CameraCtrl(0x11, 0x03, 0.0, 2.0, -2, 0x0190, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    Sleep(233)
    SetChrFace(0x03, 0xFFFE, '2', '545454', '2', '#b', '0')
    Sleep(233)
    OP_3B(0x00, (0xFF, 0x10DF, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x9079, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(166)
    OP_5E(0x00, 0x0003, 0.5, 0x0032, 0x0096, 0x0064, 0.2, 0xFFFF, -9000, -9000, -9000)
    OP_33(0x47)
    OP_33(0x48, 0xFFFE)
    OP_33(0x48, 0xFFF9)
    OP_33(0x46, 0.0, 6.0, 15)
    OP_33(0x47)
    CameraCtrl(0x0C, 0x03, 0.0, 0.25, 0.0, 0x00FA)
    CameraCtrl(0x11, 0x03, 5.0, 20, 0.0, 0x1F40, 0x01)
    CameraCtrl(0x16, 0x03, 3.0, 0x00FA)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x94, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x95, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x97, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10E3, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '2', '14', '2', '#b', '0')
    OP_4E(1.5, 0.0, 0x03)
    Sleep(1500)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.7, -1, -1, -1, 0x00, 0x00)
    Sleep(1000)
    OP_3B(0x00, (0xFF, 0x10EE, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x9064, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F6B, 0x0), 0.5, (0xFF, 0xC8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0708, 0x012C, 0x0000, 0x0708, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x01, (0xFF, 0x10E3, 0x0), (0xFF, 0x3E8, 0x0))
    Sleep(100)
    CameraCtrl(0x00)
    CameraCtrl(0x0C, 0x02, 0.0, 4.0, 0.0, 0x02EE)
    CameraCtrl(0x11, 0x02, -15, 0.0, 0.0, 0x02EE, 0x01)
    CameraCtrl(0x07, 0x00BF)
    EffectCtrl(0x0B, 0xFFFE, 0x91)
    EffectCtrl(0x0B, 0xFFFE, 0x92)
    EffectCtrl(0x0B, 0xFFFE, 0x93)
    EffectCtrl(0x0B, 0xFFFE, 0x94)
    EffectCtrl(0x0B, 0xFFFE, 0x95)
    EffectCtrl(0x0B, 0xFFFE, 0x96)
    EffectCtrl(0x0B, 0xFFFE, 0x97)
    EffectCtrl(0x0B, 0xFFFE, 0x98)
    LoadEffect(0xFFFE, 0x91, 'battle/cr032_00_11.eff')
    LoadEffect(0xFFFE, 0x92, 'battle/cr032_00_21.eff')
    LoadEffect(0xFFFE, 0x93, 'battle/cr032_00_31.eff')
    LoadEffect(0xFFFE, 0x94, 'battle/cr032_00_41.eff')
    LoadEffect(0xFFFE, 0x95, 'battle/cr032_00_51.eff')
    LoadEffect(0xFFFE, 0x96, 'battle/cr032_00_61.eff')
    LoadEffect(0xFFFE, 0x97, 'battle/cr032_00_71.eff')
    LoadEffect(0xFFFE, 0x98, 'battle/cr032_00_9.eff')
    Sleep(66)
    CameraCtrl(0x00)
    CameraCtrl(0x0C, 0x01, 0.0, -4, 0.0, 0x02BC)
    CameraCtrl(0x11, 0x01, 15, 0.0, 0.0, 0x02BC, 0x01)
    CameraCtrl(0x16, 0x01, -3, 0x02BC)
    Sleep(333)
    OP_4E(1.0, 0.0, 0x03)
    OP_3B(0x32, (0xFF, 0x1C27, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    OP_0A(
        0x01,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_81EE(): pass

    label('loc_81EE')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_89E1',
    )

    Call(0x0B, 'AniBtlCraft00_getTarget')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8325',
    )

    PlayEffect(0xFFFE, (0xFF, 0x97, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCtrl(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCtrl(0x14, 0xFFFE, 0x03, 0.95, 0.85, 1.0, 1.0, 0x0000, 0x03)

    Jump('loc_8998')

    def _loc_8325(): pass

    label('loc_8325')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8439',
    )

    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCtrl(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCtrl(0x14, 0xFFFE, 0x03, 0.6, 0.68, 0.35, 1.0, 0x0000, 0x03)

    Jump('loc_8998')

    def _loc_8439(): pass

    label('loc_8439')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_854D',
    )

    PlayEffect(0xFFFE, (0xFF, 0x95, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCtrl(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCtrl(0x14, 0xFFFE, 0x03, 0.65, 0.4, 0.8, 1.0, 0x0000, 0x03)

    Jump('loc_8998')

    def _loc_854D(): pass

    label('loc_854D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8661',
    )

    PlayEffect(0xFFFE, (0xFF, 0x94, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCtrl(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCtrl(0x14, 0xFFFE, 0x03, 0.45, 0.8, 0.39, 1.0, 0x0000, 0x03)

    Jump('loc_8998')

    def _loc_8661(): pass

    label('loc_8661')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8775',
    )

    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCtrl(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCtrl(0x14, 0xFFFE, 0x03, 0.8, 0.3, 0.3, 1.0, 0x0000, 0x03)

    Jump('loc_8998')

    def _loc_8775(): pass

    label('loc_8775')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8889',
    )

    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCtrl(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCtrl(0x14, 0xFFFE, 0x03, 0.25, 0.525, 0.75, 1.0, 0x0000, 0x03)

    Jump('loc_8998')

    def _loc_8889(): pass

    label('loc_8889')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8998',
    )

    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCtrl(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(250)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCtrl(0x14, 0xFFFE, 0x03, 0.85, 0.65, 0.2, 1.0, 0x0000, 0x03)

    def _loc_8998(): pass

    label('loc_8998')

    OP_33(0x00, 0xFFFB, 0xFFFE, 0x64)
    OP_33(0x01, 0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    OP_5E(0x00, 0x0000, 0.5, 0x0032, 0x0096, 0x0064, 0.2, 0xFFFF, -9000, -9000, -9000)
    Sleep(30)

    OP_0A(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_81EE')

    def _loc_89E1(): pass

    label('loc_89E1')

    CameraCtrl(0x07, 0x00BF)
    CameraCtrl(0x00)
    CameraCtrl(0x16, 0x03, -0.2, 0x0BB8)
    CameraCtrl(0x0C, 0x03, 0.0, 0.0, 0.1, 0x0BB8)
    CameraCtrl(0x11, 0x03, 0.0, 5.0, -2, 0x0BB8, 0x01)
    Sleep(1500)
    Call(0x0B, 'SpringOn')
    Call(0x0B, 'BtlDefaultFace')
    Call(0x13, 'AniBtlCraftFinish')

    Return()

# id: 0x0031 offset: 0x8A4C
@scena.Code('AniBtlCraft00_getTarget')
def AniBtlCraft00_getTarget():
    OP_33(0x02, 0x00, 0xFFFE)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8A81',
    )

    OP_0A(
        0x00,
        (
            Expr.Rand,
            (Expr.PushReg, 0x0),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8A67(): pass

    label('loc_8A67')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_8A81',
    )

    OP_33(0x03, 0xFFFE)

    OP_0A(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_8A67')

    def _loc_8A81(): pass

    label('loc_8A81')

    Return()

# id: 0x0032 offset: 0x8A84
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(0x13, 'AniBtlCraftBegin')
    Call(0x0B, 'SpringOff')
    LoadEffect(0xFFFE, 0x90, 'battle/cr032_01_0.eff')
    LoadEffect(0xFFFE, 0x91, 'battle/cr032_01_1.eff')
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    OP_35(0x00, 0xFFF9, 0x00000040)
    OP_35(0x00, 0xFFF9, 0x00000020)
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)

    OP_0A(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_33(0x47)
    CameraCtrl(0x14, 0x03, 0xFFFE, '', 0.4, 1.5, -3, 0x0000)
    CameraCtrl(0x13, 0xFFFE, '', 0x03, -8, -6, 0.0, 0x0000, 0x01)
    CameraSetDistance(5.5, 0)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 0x1388)
    CameraCtrl(0x11, 0x03, 2.0, -0, 0.0, 0x1388, 0x01)
    CameraCtrl(0x16, 0x03, 0.5, 0x1388)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1, -1, -1, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '1', '4[autoM4]', '', '#b', '0')
    OP_3B(0x32, (0xFF, 0x1C28, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1500)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F1A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(300)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10EB, 0x0), 0.8, (0xFF, 0x190, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x9067, 0x0), 0.6, (0xFF, 0x64, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(750)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '2', '5[autoM4]', '', '#b', '0')
    OP_5E(0x00, 0x0000, 0.7, 0x0064, 0x00FA, 0x0064, 0.2, 0xFFFF, -9000, -9000, -9000)
    OP_3B(0x00, (0xFF, 0x10E0, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x9059, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x01, (0xFF, 0x10EB, 0x0), (0xFF, 0x3E8, 0x0))
    OP_3B(0x01, (0xFF, 0x9067, 0x0), (0xFF, 0x3E8, 0x0))
    Sleep(333)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCtrl(0x00)
    OP_33(0x47)
    CameraCtrl(0x0C, 0x03, 0.0, -1.2, 0.0, 0x0000)
    CameraCtrl(0x11, 0x03, 20, 0.0, 0.0, 0x0000, 0x01)
    Sleep(1)
    OP_33(0x48, 0xFFFE)
    OP_33(0x48, 0xFFF9)
    OP_33(0x46, 0.5, 6.0, 15)
    OP_35(0x01, 0xFFF9, 0x00000040)
    OP_35(0x01, 0xFFF9, 0x00000020)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    OP_3B(0x32, (0xFF, 0x1C29, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_33(0x04, 0x00)
    OP_33(0x02, 0x00, 0xFFFE)
    def _loc_8F44(): pass

    label('loc_8F44')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_9008',
    )

    OP_33(0x01, 0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x1106, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(30)
    OP_35(0x00, 0xFFFB, 0x00000040)
    OP_35(0x00, 0xFFFB, 0x00000020)
    OP_33(0x03, 0xFFFE)

    OP_0A(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_8F44')

    def _loc_9008(): pass

    label('loc_9008')

    Sleep(1000)
    OP_33(0x47)
    OP_33(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000003, 0x00000000, 0x00000000)
    OP_33(0x47)
    OP_33(0x48, 0xFFF9)
    OP_33(0x46, 0.25, 6.0, 15)
    OP_33(0x02, 0x00, 0xFFFE)
    def _loc_903A(): pass

    label('loc_903A')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_9113',
    )

    OP_33(0x3C, 0xFFFB, 0xFFDD, 0.0, -1)
    OP_33(0x01, 0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    OP_33(0x00, 0xFFFB, 0xFFFE, 0x64)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x1107, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(30)
    OP_35(0x01, 0xFFFB, 0x00000040)
    OP_35(0x01, 0xFFFB, 0x00000020)
    OP_33(0x03, 0xFFFE)

    OP_0A(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_903A')

    def _loc_9113(): pass

    label('loc_9113')

    Sleep(1000)
    OP_33(0x02, 0x00, 0xFFFE)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1, -1, -1, 0x00, 0x00)
    Call(0x0B, 'SpringOn')
    Call(0x0B, 'BtlDefaultFace')
    PlayEffect(0xFFFE, (0xFF, 0x82, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    Call(0x13, 'AniBtlCraftFinish')

    Return()

# id: 0x0033 offset: 0x91C0
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(0x13, 'AniBtlCraftBegin')
    Call(0x0B, 'SpringOff')
    LoadEffect(0xFFFE, 0x90, 'battle/cr032_02_0.eff')
    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)

    OP_0A(
        0x02,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EffectCtrl(0x0F, 0xFFFE, 0x0082, 0x01)
    OP_33(0x47)
    CameraCtrl(0x14, 0x03, 0xFFFE, '', 0.0, 1.0, 0.0, 0x0000)
    CameraCtrl(0x13, 0xFFFE, '', 0x03, -10, 0.0, 0.0, 0x0000, 0x01)
    CameraSetDistance(2.7, 0)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 0x0FA0)
    CameraCtrl(0x11, 0x03, 10, -10, 0.0, 0x0FA0, 0x01)
    CameraCtrl(0x16, 0x03, 0.5, 0x0FA0)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '1', '4', '', '#b', '0')
    Sleep(500)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    Sleep(233)
    OP_3B(0x00, (0xFF, 0xFFFF, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x905B, 0x0), 1.0, (0xFF, 0x64, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(266)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '12', '15', '5', '#b', '0')
    Sleep(100)
    CameraCtrl(0x00)
    CameraCtrl(0x16, 0x03, 1.0, 0x015E)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 0x015E)
    CameraCtrl(0x11, 0x03, 20, 0.0, 0.0, 0x015E, 0x01)
    OP_5E(0x00, 0x0000, 0.7, 0x0064, 0x00FA, 0x0064, 0.2, 0xFFFF, -9000, -9000, -9000)
    OP_3B(0x00, (0xFF, 0x8FAC, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCtrl(0x07, 0x00BF)
    CameraCtrl(0x00)
    CameraCtrl(0x16, 0x03, 0.5, 0x0FA0)
    CameraCtrl(0x0C, 0x03, 0.0, 0.1, 0.0, 0x0FA0)
    CameraCtrl(0x11, 0x03, 5.0, 0.0, 0.0, 0x0FA0, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    Sleep(500)
    OP_33(0x00, 0xFFFE, 0xFFFE, 0x64)
    EffectCtrl(0x12, 0xFFFE, 0x0090)
    Call(0x0B, 'SpringOn')
    Call(0x0B, 'BtlDefaultFace')
    PlayEffect(0xFFFE, (0xFF, 0x82, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_ARM'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    Call(0x13, 'AniBtlCraftFinish')

    Return()

# id: 0x0034 offset: 0x9580
@scena.Code('AniBtlConditionExchange')
def AniBtlConditionExchange():
    OP_3B(0x32, (0xFF, 0x1C2A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x1106, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Return()

# id: 0x0035 offset: 0x9608
@scena.Code('AniBtlConditionExchangeEnd')
def AniBtlConditionExchangeEnd():
    OP_3B(0x32, (0xFF, 0x1C2B, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Return()

# id: 0x0036 offset: 0x964C
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(0x0B, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0037 offset: 0x9688
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0038 offset: 0x96B4
@scena.Code('AniEvAttack')
def AniEvAttack():
    Call(0x0B, 'SpringOff')
    OP_AE('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0039 offset: 0x9728
@scena.Code('AniEvDamage')
def AniEvDamage():
    Call(0x0B, 'SpringOff')
    OP_AE('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003A offset: 0x979C
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    Call(0x0B, 'SpringOff')
    OP_AE('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003B offset: 0x9814
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(0xFFFE, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003C offset: 0x9840
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003D offset: 0x9898
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003E offset: 0x98C4
@scena.Code('AniEvWeak')
def AniEvWeak():
    Call(0x0B, 'SpringOff')
    OP_AE('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x003F offset: 0x990C
@scena.Code('AniEvPowerup')
def AniEvPowerup():
    Call(0x0B, 'SpringOff')
    OP_AE('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0040 offset: 0x9984
@scena.Code('AniEvDead')
def AniEvDead():
    Call(0x0B, 'SpringOff')
    OP_AE('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0041 offset: 0x99F8
@scena.Code('AniEvDeada')
def AniEvDeada():
    Call(0x0B, 'SpringOff')
    OP_AE('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0042 offset: 0x9A40
@scena.Code('AniEvDead1')
def AniEvDead1():
    Call(0x0B, 'SpringOff')
    OP_AE('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'EV_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0043 offset: 0x9A88
@scena.Code('AniEvCraft00')
def AniEvCraft00():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0044 offset: 0x9ABC
@scena.Code('AniEvCraft00_1')
def AniEvCraft00_1():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0045 offset: 0x9B20
@scena.Code('AniEvCraft00_2')
def AniEvCraft00_2():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0046 offset: 0x9B84
@scena.Code('AniEvCraft01')
def AniEvCraft01():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0047 offset: 0x9BB8
@scena.Code('AniEvCraft01_1')
def AniEvCraft01_1():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0048 offset: 0x9C1C
@scena.Code('AniEvCraft01_2')
def AniEvCraft01_2():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0049 offset: 0x9C80
@scena.Code('AniEvCraft02')
def AniEvCraft02():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004A offset: 0x9CB4
@scena.Code('AniEvCraft02_1')
def AniEvCraft02_1():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004B offset: 0x9D18
@scena.Code('AniEvCraft02_01')
def AniEvCraft02_01():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004C offset: 0x9D7C
@scena.Code('AniEvDropclothes_01')
def AniEvDropclothes_01():
    PlayChrAnimeClip(0xFFFE, 'DROPCLOTHES_01', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004D offset: 0x9DB0
@scena.Code('AniEvDropclothes_02')
def AniEvDropclothes_02():
    PlayChrAnimeClip(0xFFFE, 'DROPCLOTHES_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'DROPCLOTHES_03', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004E offset: 0x9E14
@scena.Code('AniEv00070')
def AniEv00070():
    PlayChrAnimeClip(0xFFFE, 'ev00070', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev00070a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004F offset: 0x9E6C
@scena.Code('AniAttachEQU417')
def AniAttachEQU417():
    OP_31(0x00, 'C_EQU417')
    AttachEquip(0xFFFE, 'C_EQU417', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    OP_76(0xFFFE, 'R_arm_point', 'equip', 0x00, 0x01, 0.0, -1, -1, -1)

    Return()

# id: 0x0050 offset: 0x9EF0
@scena.Code('AniDetachEQU417')
def AniDetachEQU417():
    OP_31(0x01, 'C_EQU417')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_54(0x0B, 0xFFFE)

    Return()

# id: 0x0051 offset: 0x9F38
@scena.Code('AniEv50525')
def AniEv50525():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev50525', 0x00, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    Sleep(166)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev50525a', 0x01, 0x00, 0x00, 0x00, 0x00, -2, -1, -1, -1, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0052 offset: 0x9FC0
@scena.AnimeClips('_AniTurn')
def _AniTurn():
    return ScenaAnimeClips(
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
            name   = 'WALK',
        ),
    )

# id: 0x0053 offset: 0xA040
@scena.AnimeClips('_AniWait')
def _AniWait():
    return ScenaAnimeClips(
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
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0054 offset: 0xA0F0
@scena.AnimeClips('_AniWalk')
def _AniWalk():
    return ScenaAnimeClips(
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
            name   = 'WALK',
        ),
    )

# id: 0x0055 offset: 0xA170
@scena.AnimeClips('_AniRun')
def _AniRun():
    return ScenaAnimeClips(
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

# id: 0x0056 offset: 0xA1F0
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

# id: 0x0057 offset: 0xA250
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

# id: 0x0058 offset: 0xA2B0
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

# id: 0x0059 offset: 0xA310
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_02_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk032_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk032_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk032_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/moncharge.eff',
        ),
    )

# id: 0x005A offset: 0xA430
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C20,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C22,
            name   = '',
        ),
    )

# id: 0x005B offset: 0xA4B0
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

# id: 0x005C offset: 0xA510
@scena.AnimeClips('_AniBtlTurn')
def _AniBtlTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
    )

# id: 0x005D offset: 0xA570
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
            dword4 = 0x00001C24,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C25,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
    )

# id: 0x005E offset: 0xA6C0
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C38,
            name   = '',
        ),
    )

# id: 0x005F offset: 0xA720
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

# id: 0x0060 offset: 0xA7A0
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C37,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C35,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C36,
            name   = '',
        ),
    )

# id: 0x0061 offset: 0xA850
@scena.AnimeClips('_AniBtlGuardBreakVoice')
def _AniBtlGuardBreakVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C33,
            name   = '',
        ),
    )

# id: 0x0062 offset: 0xA8B0
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

# id: 0x0063 offset: 0xA960
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

# id: 0x0064 offset: 0xA9C0
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
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionup.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C32,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F00,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F78,
            name   = '',
        ),
    )

# id: 0x0065 offset: 0xAB30
@scena.AnimeClips('_AniBtlDead')
def _AniBtlDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C34,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
    )

# id: 0x0066 offset: 0xABB0
@scena.AnimeClips('_AniBtlAria')
def _AniBtlAria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C2C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
    )

# id: 0x0067 offset: 0xAC80
@scena.AnimeClips('_AniBtlArts')
def _AniBtlArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C2D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0068 offset: 0xAD80
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

# id: 0x0069 offset: 0xAE30
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_20.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_30.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_40.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_50.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_60.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_70.eff',
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
            dword4 = 0x00001C26,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009078,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010DF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009079,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010EE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009064,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_21.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_31.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_41.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_51.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_61.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_71.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C27,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
    )

# id: 0x006A offset: 0xB480
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_01_1.eff',
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
            dword4 = 0x00001C28,
            name   = '',
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
            dword4 = 0x00008F1A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010EB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009067,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009059,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C29,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001106,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001107,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x006B offset: 0xB760
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_02_0.eff',
        ),
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
            name   = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000FFFF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000905B,
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
            dword4 = 0x00008FAC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01a',
        ),
    )

# id: 0x006C offset: 0xB8D0
@scena.AnimeClips('_AniBtlConditionExchange')
def _AniBtlConditionExchange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C2A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001106,
            name   = '',
        ),
    )

# id: 0x006D offset: 0xB950
@scena.AnimeClips('_AniBtlConditionExchangeEnd')
def _AniBtlConditionExchangeEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001C2B,
            name   = '',
        ),
    )

# id: 0x006E offset: 0xB9B0
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

# id: 0x006F offset: 0xBA10
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

# id: 0x0070 offset: 0xBA70
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

# id: 0x0071 offset: 0xBAF0
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

# id: 0x0072 offset: 0xBB70
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

# id: 0x0073 offset: 0xBBF0
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

# id: 0x0074 offset: 0xBC50
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

# id: 0x0075 offset: 0xBCD0
@scena.AnimeClips('_AniEvBtlWalk')
def _AniEvBtlWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0076 offset: 0xBD30
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

# id: 0x0077 offset: 0xBD90
@scena.AnimeClips('_AniEvPowerup')
def _AniEvPowerup():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa',
        ),
    )

# id: 0x0078 offset: 0xBE10
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

# id: 0x0079 offset: 0xBE90
@scena.AnimeClips('_AniEvDeada')
def _AniEvDeada():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x007A offset: 0xBEF0
@scena.AnimeClips('_AniEvDead1')
def _AniEvDead1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DEAD1',
        ),
    )

# id: 0x007B offset: 0xBF50
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

# id: 0x007C offset: 0xBFB0
@scena.AnimeClips('_AniEvCraft00_1')
def _AniEvCraft00_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01a',
        ),
    )

# id: 0x007D offset: 0xC030
@scena.AnimeClips('_AniEvCraft00_2')
def _AniEvCraft00_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02a',
        ),
    )

# id: 0x007E offset: 0xC0B0
@scena.AnimeClips('_AniEvCraft01')
def _AniEvCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
    )

# id: 0x007F offset: 0xC110
@scena.AnimeClips('_AniEvCraft01_1')
def _AniEvCraft01_1():
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

# id: 0x0080 offset: 0xC190
@scena.AnimeClips('_AniEvCraft01_2')
def _AniEvCraft01_2():
    return ScenaAnimeClips(
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
            name   = 'BTL_CRAFT01_01a',
        ),
    )

# id: 0x0081 offset: 0xC210
@scena.AnimeClips('_AniEvCraft02')
def _AniEvCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
    )

# id: 0x0082 offset: 0xC270
@scena.AnimeClips('_AniEvCraft02_1')
def _AniEvCraft02_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00a',
        ),
    )

# id: 0x0083 offset: 0xC2F0
@scena.AnimeClips('_AniEvCraft02_01')
def _AniEvCraft02_01():
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

# id: 0x0084 offset: 0xC370
@scena.AnimeClips('_AniEvDropclothes_01')
def _AniEvDropclothes_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DROPCLOTHES_01',
        ),
    )

# id: 0x0085 offset: 0xC3D0
@scena.AnimeClips('_AniEvDropclothes_02')
def _AniEvDropclothes_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DROPCLOTHES_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DROPCLOTHES_03',
        ),
    )

# id: 0x0086 offset: 0xC450
@scena.AnimeClips('_AniEv00070')
def _AniEv00070():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00070',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00070a',
        ),
    )

# id: 0x0087 offset: 0xC4D0
@scena.AnimeClips('_AniAttachEQU417')
def _AniAttachEQU417():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU417',
        ),
    )

# id: 0x0088 offset: 0xC530
@scena.AnimeClips('_AniEv50525')
def _AniEv50525():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev50525',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev50525a',
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
