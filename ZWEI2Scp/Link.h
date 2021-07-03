#include <string.h>
#include <malloc.h>

typedef char SElemtype;
typedef struct Line
{
	char *text;
	unsigned line;
	struct Line *next;
}Line,*Link;

void Link_Pushback(Link &L,const unsigned &LineNum,const char *text)
{
	Link pl = L;
	if (NULL == L)
	{
		L = pl = (Link)malloc(sizeof(Line));
	}
	else
	{
		while (pl->next)
			pl = pl->next;
		pl->next = (Link)malloc(sizeof(Line));
		pl = pl->next;
	}
	pl->line = LineNum;
	pl->text = (char*)malloc(sizeof(char) * strlen(text) + 1);
	strcpy(pl->text,text);
	pl->text[strlen(text)] = 0;
	pl->next = NULL;
}