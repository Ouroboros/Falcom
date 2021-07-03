struct StringData
{
    char*   str;
    int     id;
};

struct ArrayData
{
    int         count;
    StringData* buffer;
};

struct TableData
{
    void*           vtable;
    void*           buffer;
    char*           tableData;
    uint16_t        entryCount;
    int             tableCount;
    ArrayData       tableName;
    _BYTE           gap30[8];
    unsigned int    unsigned38;
    _DWORD          dword3C;
    char*           tableArray;
};

struct NameTableEntry
{
    _WORD charId;
    _BYTE gap2[6];
    char* name;
    char* C_CHR;
    char* CHR_FC;
    char* chr;
    char* FC_CHR;
    char* name2;
    _DWORD dword38;
    _DWORD dword3C;
    _DWORD dword40;
    _WORD word44;
    _WORD word46;
    _BYTE byte48;
    _WORD word4A;
};
