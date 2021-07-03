#ifndef _PEEKTEXT_H_
#define _PEEKTEXT_H_

#pragma warning(disable:4530)

#include <Windows.h>
#include <stdio.h>
#include "my_common.h"
#include <vector>
#include <string>

using std::vector;
using std::string;

enum SCRIPT_TYPE
{
    None, 
    ItemTable, 
    StageTable, 
    ShopTable, 
    CharNoteTable, 
    MailTable, 
    NikkiTable, 
    MapTable, 
    CCTable, 
    LVTable, 
    TAKARATable, 
    CharTable, 
    ScriptTable, 
    CharMotTable, 
    EndOfTable, 
};

class CRipZwei2Text
{
public:
    CRipZwei2Text();
    ~CRipZwei2Text();

public:
    Bool  Open(char *szFileName);
    Bool  GetAllText(vector<string> &vec);

protected:
    Void  Free();
    u32   CheckScriptType();
    char *GetCommentEndPos(char *pLine);
    Void  GetColumnText(vector<string> &vec, char *pLine, u32 uColumn);
    char *GetNextLinePos();

    Void  RipItemTable    (vector<string> &vec, char *pLine);
    Void  RipStageTable   (vector<string> &vec, char *pLine);
    Void  RipCharNoteTable(vector<string> &vec, char *pLine);
    Void  RipMailTable    (vector<string> &vec, char *pLine);
    Void  RipNikkiTable   (vector<string> &vec, char *pLine);
    Void  RipMapTable     (vector<string> &vec, char *pLine);
    Void  RipTAKARATable  (vector<string> &vec, char *pLine);
    Void  RipCharTable    (vector<string> &vec, char *pLine);
    Void  RipScripTable   (vector<string> &vec, char *pLine);
    Void  RipCharMotTable (vector<string> &vec, char *pLine);


protected:
    Bool  m_bEndOfScp, m_bMultiLineComment;
    u32   m_u32ScpSize, m_u32ScpType, m_u32Cursor;
    char *m_pScpBuffer, *m_pEndOfScript;
};

#endif /* _PEEKTEXT_H_ */